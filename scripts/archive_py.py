"""
archive_py.py - Archive runner for Python scripts in python/

Usage (from project root):
    python scripts/archive_py.py python/<script>.py [extra args...]

Behaviour:
    1. Creates archive/<YYYYMMDDHHMMSS>/python/, figs/, data/
    2. Copies the target script and top-level locally-resolved imports to archive/python/
    3. Copies figs/ and data/ (if they exist) into the archive
    4. Runs the target script (cwd = python/)
    5. Only if exit code is 0: copies archive/figs/ -> figs/ and archive/data/ -> data/
"""

import sys
import ast
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


def find_local_imports(py_file, python_dir):
    """Return top-level .py files in python_dir imported by py_file."""
    local = []
    try:
        tree = ast.parse(py_file.read_text(encoding="utf-8"))
    except SyntaxError:
        return local
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [alias.name.split(".")[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [node.module.split(".")[0]] if node.module else []
        else:
            continue
        for name in names:
            candidate = python_dir / f"{name}.py"
            if candidate.exists() and candidate.resolve() != py_file.resolve():
                if candidate not in local:
                    local.append(candidate)
    return local


def sync_dir(src, dst):
    """Copy all files from src into dst, overwriting. Creates dst if missing."""
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.rglob("*"):
        if item.is_file():
            rel = item.relative_to(src)
            dest_file = dst / rel
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_file)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/archive_py.py python/<script>.py [args...]")
        sys.exit(1)

    project_root = Path(__file__).parent.parent.resolve()
    python_dir   = project_root / "python"
    target       = (project_root / sys.argv[1]).resolve()

    if not target.exists():
        print(f"Error: {target} not found.")
        sys.exit(1)

    try:
        target.relative_to(python_dir)
    except ValueError:
        print(f"Error: target must be inside {python_dir}")
        sys.exit(1)

    timestamp    = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_base = project_root / "archive" / timestamp
    arch_python  = archive_base / "python"
    arch_figs    = archive_base / "figs"
    arch_data    = archive_base / "data"
    for d in (arch_python, arch_figs, arch_data):
        d.mkdir(parents=True, exist_ok=True)

    shutil.copy2(target, arch_python / target.name)
    print(f"Archived: {target.name}")

    for dep in find_local_imports(target, python_dir):
        shutil.copy2(dep, arch_python / dep.name)
        print(f"Archived dependency: {dep.name}")

    sync_dir(project_root / "figs", arch_figs)
    sync_dir(project_root / "data", arch_data)

    extra_args = sys.argv[2:]
    cmd = [sys.executable, str(target)] + extra_args
    print(f"\nRunning: {' '.join(cmd)}\n")
    result = subprocess.run(cmd, cwd=str(python_dir))

    if result.returncode == 0:
        sync_dir(arch_figs, project_root / "figs")
        sync_dir(arch_data, project_root / "data")
        print("figs/ and data/ synced back to project root.")
    else:
        print(f"Script exited with code {result.returncode} - figs/ and data/ NOT copied back.")

    print(f"\nArchive: {archive_base}")
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
