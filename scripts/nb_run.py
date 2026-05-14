"""
nb_run.py - Execute a Jupyter notebook by extracting code cells and running them.
Usage: python scripts/nb_run.py python/<notebook>.ipynb
"""
import json
import sys
import subprocess
import tempfile
from pathlib import Path


PREAMBLE = """\
import matplotlib
matplotlib.use('Agg')   # non-interactive backend — no GUI windows
import builtins
# Mock IPython display functions
def _display(*args, **kwargs): pass
builtins.display = _display
try:
    from IPython.display import display as _ipy_display, HTML
    import IPython.display
    IPython.display.display = _display
except ImportError:
    pass
"""

def extract_code(nb_path):
    nb = json.loads(nb_path.read_text(encoding='utf-8'))
    lines = [PREAMBLE]
    for c in nb['cells']:
        if c['cell_type'] != 'code':
            continue
        src = ''.join(c.get('source', []))
        if src.strip():
            lines.append(f'# ── cell {c.get("id","?")} ──')
            lines.append(src)
            lines.append('')
    return '\n'.join(lines)


def main():
    if len(sys.argv) < 2:
        print('Usage: python scripts/nb_run.py python/<notebook>.ipynb')
        sys.exit(1)
    root = Path(__file__).parent.parent
    nb_path = (root / sys.argv[1]).resolve()
    if not nb_path.exists():
        print(f'Error: {nb_path} not found.')
        sys.exit(1)

    code = extract_code(nb_path)

    # Write to temp file and run from python/ dir
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py',
                                     dir=root / 'python',
                                     delete=False, encoding='utf-8') as f:
        f.write(code)
        tmp = Path(f.name)

    print(f'Running {nb_path.name} ({tmp.name}) ...')
    try:
        result = subprocess.run(
            [sys.executable, str(tmp)],
            cwd=str(root / 'python'),
        )
    finally:
        tmp.unlink(missing_ok=True)

    sys.exit(result.returncode)


if __name__ == '__main__':
    main()
