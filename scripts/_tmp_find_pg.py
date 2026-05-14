import json
nb = json.load(open('python/hierarchical_logistic_run.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    src = ''.join(c.get('source', []))
    if 'polyagamma' in src.lower() or 'pg(' in src.lower() or 'polya' in src.lower():
        print(f'\n=== CS5 Cell {i} (id={c.get("id")}) ===')
        print(src[:400])
        print('---')
