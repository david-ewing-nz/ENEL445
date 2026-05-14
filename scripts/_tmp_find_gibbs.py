import json
nb = json.load(open('python/linear_run.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    src = ''.join(c.get('source', []))
    if 'gibbs' in src.lower() and c['cell_type'] == 'code':
        print(f'\n=== Cell {i} (id={c.get("id")}) ===')
        print(src[:400])
        print('---')
