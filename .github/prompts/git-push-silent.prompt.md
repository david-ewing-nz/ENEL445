---
name: git-push-silent
mode: agent
description: "Stage all files, commit with message 'prompt push', and push to origin/main — no interaction."
---

From the project root (`d:\github\ENEL445`):

1. Run `git add -A`
2. Run `git commit -m "prompt push"`
3. Run `git push origin main`

Do not ask for confirmation. Do not prompt for a commit message. Report the final output of each command.
