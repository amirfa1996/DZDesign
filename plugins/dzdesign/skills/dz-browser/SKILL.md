---
name: dz-browser
description: "Test a local website or perform authorized browser interactions from Codex using Playwright CLI, screenshots and reproducible checks."
---

# DZ Browser
Run `python <plugin-root>/scripts/tools.py prepare playwright` for the pinned CLI documentation and `python <plugin-root>/scripts/tools.py browser-install` only when its executable dependency is needed. This installs a pinned npm CLI into the current project's `.dzdesign/browser`, not globally.
Read `skills/playwright-cli/SKILL.md` and the relevant reference in the prepared source. Invoke commands via `python <plugin-root>/scripts/tools.py run playwright <arguments>`.
Typical sequence: `open http://localhost:5173 --browser chrome`, `snapshot`, interact using current refs, `screenshot`, `close`. Use the session flag when working alongside other sessions. Inspect new snapshots before choosing targets. Preserve credentials and customer data. Publication, purchases and messages need task-specific authorization.
For QA, cover the requested primary flow, validation/error state and desktop/mobile viewport. Report exact URLs, checks and artifacts. Do not infer success from installation alone. Browser launch may be blocked by the host sandbox; report it without disabling host protections.
