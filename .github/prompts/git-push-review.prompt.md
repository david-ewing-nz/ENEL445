---
name: git-push-review
mode: agent
description: "Review repository state and confirm with user before committing and pushing."
---

Before committing and pushing, perform the following checks and present findings:

1. Run `git status` — list all modified and untracked files, grouped by type (notebooks, reports, scripts, data)
2. Flag any temporary or debug files (e.g. `_tmp_*.py`) — ask whether to include or exclude
3. Flag any internal/session files (`AGENT_HANDOFF.md`, `SESSION_STATE.md`, `.github/prompts/CAPTURE_STATE.prompt.md`) — ask whether to include
4. Confirm the current branch and that `origin/main` is the correct remote target
5. Ask the user for a commit message
6. Wait for explicit user approval ("yes", "go ahead", or equivalent)

Only after approval: run `git add -A`, `git commit -m "<approved message>"`, `git push origin main`, and report the result.
