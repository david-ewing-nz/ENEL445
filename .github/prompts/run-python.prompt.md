---
name: run-python
description: "Run a Python script from python/ via the archive runner. Scripts in scripts/ are exempt and run directly."
---

Run `${input:scriptPath:Path relative to project root, e.g. python/vb_algorithms_py.py}`.

Note: this runner applies only to files in `python/`. Files in `scripts/` are utility/logistics files and must NOT be passed through archive_py.py.

Run from the project root (`d:\github\ENEL445`):
```
python scripts/archive_py.py "${input:scriptPath}"
```

Confirm archive folder path, any errors, and whether figs/ and data/ were synced back (only synced on success).
