# Release and rollback
Version 0.1.0 is an experimental GitHub repository marketplace release, not an OpenAI directory submission. Publishing to GitHub was explicitly requested. Only this isolated source tree is published; no existing client repository, contract, media attachment, credentials or customer files belong in it.

Before release: run `python -m unittest discover -s tests -v`, inspect git status/diff, verify the archive and licenses. Produce the plugin ZIP from `plugins/dzdesign` only; do not include marketplace metadata in that ZIP. The whole repository remains the GitHub marketplace.

Rollback: uninstall with `codex plugin remove dzdesign@digizorg` and remove the marketplace only if no longer wanted. Project dependency cache lives under `.dzdesign` in that project. To undo a published change, create a normal revert commit rather than force-pushing or deleting the repository. Published archives can be retained for version tracing. Do not auto-delete user work.

No automatic hooks or web service is deployed. Adding hosted tools, new external services or paid models is a separate scope. An official OpenAI directory submission needs its own preparation and review; naming does not guarantee acceptance.
