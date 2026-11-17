# Validation record

Checked locally on 2026-11-17 with Python 3.12.10, Node.js from `C:\Program Files\nodejs`, and Codex CLI 26.1111.2228.

- `python -m unittest discover -s tests -v`: **12 passed**. Covers manifests, Codex-only policy, six skill frontmatters, source pinning, traversal and symlink rejection, cache integrity, tool path constraints, and the read-only doctor.
- `python plugins/dzdesign/scripts/tools.py doctor`: passed. Python, Node and Codex were detected. Upstream resources and browser dependencies are intentionally fetched only on request.
- Codex plugin package install: passed with `codex plugin marketplace add <local source>` and `codex plugin add dzdesign@digizorg`; the installed package was discovered and enabled in an isolated test profile.
- Normal user-profile install: passed on 2026-11-17. `codex plugin marketplace add <local source>` and `codex plugin add dzdesign@digizorg` installed version 0.1.0 under `~/.codex/plugins/cache/digizorg/dzdesign/0.1.0`.
- Impeccable engine 0.1.25 was downloaded earlier from its official release, matched the upstream SHA-256 manifest, and answered `engine-probe`. That binary is not included in the plugin; `tools.py engine` downloads it explicitly into a project-local cache.
- Playwright CLI npm package 0.1.24 was installed earlier. Opening a browser from this restricted host failed at process startup, so live browser interaction is **not verified** here. No browser check is represented as passing.
- No OpenAI directory submission or approval was performed. This repository marketplace is a separate installation path; its GitHub publication is pending creation of the repository `amirfa1996/DZDesign`.

Re-run package checks from this repository root:

```sh
python -m unittest discover -s tests -v
python plugins/dzdesign/scripts/tools.py doctor
```
