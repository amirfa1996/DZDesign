# DZDesign
**A Codex-only design studio by DigiZorg.** Distinctive frontend design, interface refinement, browser verification, design references and procedural image-to-3D workflows.

This is an independent integration, not a claim that DigiZorg authored Taste, Impeccable, Playwright, Awesome DESIGN.md or img2threejs. See THIRD_PARTY_NOTICES.md and the immutable source lock.

```sh
codex plugin marketplace add amirfa1996/DZDesign
codex plugin add dzdesign@digizorg
```

Then select `$dzdesign` in Codex. The package contains six Codex-gated skills, an explicit Python dependency helper, portable and Codex manifests, and a repository marketplace. No other-agent directories, automatic hooks, credentials or hosted server are included. OpenAI directory approval is separate from this repository marketplace.

Resources are lazily fetched from pinned GitHub commits with archive checksums, into `.dzdesign` in your project. `prepare` downloads code; it does not execute it. Python 3.10+ is needed; Taste and browser operations need Node 22+ and Chrome/Edge. Playwright npm dependencies and the optional Impeccable engine require explicit setup commands. Do not assume all third-party services or optional plugins are free.

```sh
python plugins/dzdesign/scripts/tools.py doctor
python plugins/dzdesign/scripts/tools.py prepare library
python plugins/dzdesign/scripts/tools.py prepare taste
python plugins/dzdesign/scripts/tools.py browser-install
python plugins/dzdesign/scripts/tools.py run playwright --version
```

See docs/VALIDATION.md for actual test scope, docs/GUIDE.fa.md for Persian examples, docs/RELEASE.md for release/rollback and LICENSE for integration licensing.
