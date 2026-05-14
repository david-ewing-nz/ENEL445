import json, pathlib, numpy as np

nb = json.loads(pathlib.Path('python/hierarchical_linear_run.ipynb').read_text())
for cell in nb['cells']:
    src = ''.join(cell['source'])
    outputs = cell.get('outputs', [])
    for o in outputs:
        lines = o.get('text', '') or o.get('data', {}).get('text/plain', '')
        if isinstance(lines, list):
            lines = ''.join(lines)
        if lines and ("mu_beta" in lines or "m_u" in lines or "m =" in lines or "Group" in lines):
            print("=== CELL SOURCE (first 200) ===")
            print(src[:200])
            print("=== OUTPUT ===")
            print(lines[:600])
            print()
