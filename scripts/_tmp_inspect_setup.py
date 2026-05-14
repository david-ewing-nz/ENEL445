"""
Inspect the setup cell of linear_run.ipynb to understand imports and constants.
"""
import json
nb = json.load(open('python/linear_run.ipynb', encoding='utf-8'))
# Print first few code cells
for i, c in enumerate(nb['cells']):
    if c['cell_type'] == 'code':
        src = ''.join(c.get('source', []))
        print(f'\n=== Cell {i} (id={c.get("id")}) ===')
        print(src[:500])
        print('---')
    if i > 4:
        break
