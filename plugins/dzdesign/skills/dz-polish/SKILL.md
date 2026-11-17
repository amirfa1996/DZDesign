---
name: dz-polish
description: "Critique, refine, polish or audit an existing interface in Codex using Impeccable playbooks and its optional verified engine."
---

# DZ Polish
Choose a concrete target and inspect its current state. Preserve layout, factual copy and brand for a refinement; agree a direction for a redesign.
Run `python <plugin-root>/scripts/tools.py prepare impeccable` and read the selected playbook under `.agents/skills/impeccable/reference/` in the returned source tree. Use critique, audit, polish, adapt, harden or a named design operation as appropriate.
Optional engine: `python <plugin-root>/scripts/tools.py engine --help`. Engine downloads are explicit and verified against the checksum manifest inside the pinned upstream source. Then use `python <plugin-root>/scripts/tools.py run impeccable context --target <file>` or another documented verb. Read relevant playbook files before applying an operation.
No host hooks or other-agent setup is installed. DZDesign forces `IMPECCABLE_LIVE_COPY_AGENT=off` when it launches the engine, preventing automatic fallback to an agent with bypassed approvals. Never invoke a bypass mode as a workaround. Live editing is local only; do not inject overlays into production. Report if an engine/browser operation is unavailable.
