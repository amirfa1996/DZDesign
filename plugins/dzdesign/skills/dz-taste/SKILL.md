---
name: dz-taste
description: "Build a distinctive frontend or redesign a generic page in Codex using the pinned Taste design workflow."
---

# DZ Taste
Inspect actual code and collect the product, audience, content, desired action and brand constraints. Draft a specific visual direction before editing. Avoid invented client claims or fake testimonials.
1. Run `python <plugin-root>/scripts/tools.py prepare taste` when the upstream reference/runtime is needed. It prints its local path.
2. Read that directory's `skills/taste-skill/SKILL.md` body and only relevant references. Treat `<skill>` as its `skills/taste-skill` directory.
3. In Codex, skip the upstream host hooks and all setup for other agents. No hooks are installed by DZDesign. Run finish checks explicitly: `python <plugin-root>/scripts/tools.py run taste scripts/gate.mjs <local-page-or-url>`.
4. Implement the user's own identity and verify readable contrast, keyboard use, mobile overflow and real content. Use the upstream checks as evidence, not as permission to overwrite the user's brief.
The finish gate requires Node 22+ and an installed browser. A gate that could not launch is unverified, not passed.
