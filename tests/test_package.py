import hashlib, importlib.util, io, json, os, re, subprocess, sys, tempfile, unittest, zipfile
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/'plugins/dzdesign'
spec=importlib.util.spec_from_file_location('dz_tools',PLUGIN/'scripts/tools.py')
tools=importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)
def payload(entries):
    data=io.BytesIO()
    with zipfile.ZipFile(data,'w') as z:
        for name,text in entries.items(): z.writestr(name,text)
    return data.getvalue()

class PackageTests(unittest.TestCase):
    def test_manifests_match_and_are_codex_only(self):
        portable=json.loads((PLUGIN/'plugin.json').read_text())
        compat=json.loads((PLUGIN/'.codex-plugin/plugin.json').read_text())
        marketplace=json.loads((ROOT/'.agents/plugins/marketplace.json').read_text())
        self.assertEqual(portable['name'],compat['name'])
        self.assertEqual(portable['version'],compat['version'])
        self.assertEqual(portable['extensions']['com.openai']['interface'],compat['interface'])
        self.assertEqual(marketplace['plugins'][0]['policy']['products'],['CODEX'])
        self.assertEqual(marketplace['plugins'][0]['source']['path'],'./plugins/dzdesign')
        self.assertLessEqual(len(compat['interface']['shortDescription']),30)
        for k in ['logo','composerIcon']:
            self.assertTrue((PLUGIN/compat['interface'][k]).is_file())

    def test_six_native_skills(self):
        skills=list((PLUGIN/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills),6)
        for skill in skills:
            text=skill.read_text()
            self.assertTrue(text.startswith('---\n'))
            self.assertIn('name: '+skill.parent.name+'\n',text)
            match=re.search(r'^description: (.+)$',text,re.M)
            self.assertTrue(json.loads(match.group(1)))
            metadata=(skill.parent/'agents/openai.yaml').read_text()
            self.assertIn('products: [CODEX]',metadata)

    def test_no_other_host_configuration_or_secrets(self):
        for path in ROOT.rglob('*'):
            rel=path.relative_to(ROOT)
            if any(part in ('.git','.dzdesign','__pycache__') for part in rel.parts): continue
            self.assertFalse(any(part.lower() in tools.FORBIDDEN for part in rel.parts),str(rel))
            if path.is_file():
                self.assertNotEqual(path.name,'.env')
                self.assertNotEqual(path.suffix,'.exe')
                if path.suffix in ('.py','.md','.json','.yaml'):
                    self.assertNotRegex(path.read_text(encoding='utf-8'),r'(?:ghp|github_pat)_[A-Za-z0-9]{25,}')

    def test_lock_has_five_immutable_sources(self):
        lock=tools.load_lock()
        self.assertEqual(len(lock['components']),5)
        for item in lock['components'].values():
            self.assertRegex(item['commit'],r'^[a-f0-9]{40}$')
            self.assertRegex(item['sha256'],r'^[a-f0-9]{64}$')
            self.assertTrue(item['archive'].endswith(item['commit']))

    def test_read_only_doctor(self):
        with tempfile.TemporaryDirectory() as temp:
            result=subprocess.run([sys.executable,str(PLUGIN/'scripts/tools.py'),'doctor'],cwd=temp,text=True,capture_output=True,check=True)
            self.assertIn('prepared',json.loads(result.stdout))
            self.assertFalse((Path(temp)/'.dzdesign').exists())

class DependencyTests(unittest.TestCase):
    def test_sha_mismatch(self):
        with self.assertRaises(ValueError): tools.verify_digest(b'tampered','0'*64)

    def test_path_traversal(self):
        with tempfile.TemporaryDirectory() as temp:
            for name in ['../escape','repo/../../escape','/tmp/escape','repo/C:/escape']:
                with self.assertRaises(ValueError): tools.extract(payload({name:'bad'}),Path(temp))
            # ZipInfo normalizes Windows separators when a fixture is constructed.
            with self.assertRaises(ValueError): tools.relative_member('repo\\escape')

    def test_filters_other_agent_folders(self):
        data=payload({'repo/.claude/skills/a':'skip','repo/CLAUDE.md':'skip','repo/.agents/skills/a/SKILL.md':'keep','repo/forge/a.py':'print(1)'})
        with tempfile.TemporaryDirectory() as temp:
            tools.extract(data,Path(temp))
            self.assertFalse((Path(temp)/'.claude').exists())
            self.assertFalse((Path(temp)/'CLAUDE.md').exists())
            self.assertTrue((Path(temp)/'.agents/skills/a/SKILL.md').is_file())

    def test_archive_symlink_rejected(self):
        data=io.BytesIO()
        with zipfile.ZipFile(data,'w') as z:
            entry=zipfile.ZipInfo('repo/link')
            entry.create_system=3
            entry.external_attr=0o120777<<16
            z.writestr(entry,'outside')
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError): tools.extract(data.getvalue(),Path(temp))

    def test_prepare_then_detect_modified_cache(self):
        data=payload({'repo/README.md':'original'})
        digest=hashlib.sha256(data).hexdigest()
        fake={'components':{'taste':{'archive':'https://example.com/archive','sha256':digest}}}
        with tempfile.TemporaryDirectory() as temp,patch.object(tools,'runtime_root',return_value=Path(temp)/'.dzdesign'),patch.object(tools,'load_lock',return_value=fake),patch.object(tools,'download',return_value=data) as dl:
            target=tools.prepare('taste')
            self.assertEqual(tools.prepare('taste'),target)
            self.assertEqual(dl.call_count,1)
            (target/'README.md').write_text('changed')
            with self.assertRaises(ValueError): tools.prepare('taste')

    def test_engine_platform_mapping(self):
        self.assertEqual(tools.engine_asset('Windows','AMD64'),'impeccable-windows-x64.exe')
        self.assertEqual(tools.engine_asset('Darwin','arm64'),'impeccable-darwin-arm64')
        self.assertEqual(tools.engine_asset('Linux','x86_64'),'impeccable-linux-x64')
        with self.assertRaises(ValueError): tools.engine_asset('Other','x86')

    def test_run_does_not_escape_source_or_interpolate_shell(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(tools,'prepare',return_value=Path(temp)):
                with self.assertRaises(ValueError): tools.run_tool('three',['../outside.py'])

if __name__=='__main__': unittest.main()
