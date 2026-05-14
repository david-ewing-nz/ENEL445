import json

for nbfile, label in [
    ('python/hierarchical_linear_run.ipynb', 'CS4'),
    ('python/hierarchical_logistic_run.ipynb', 'CS5'),
]:
    nb = json.load(open(nbfile, encoding='utf-8'))
    for i, c in enumerate(nb['cells']):
        src = ''.join(c.get('source', []))
        if ('cavi' in src.lower() or 'vb_' in src.lower() or 'def elbo' in src.lower()
                or 'def run_' in src.lower() or 'variational' in src.lower()):
            if c['cell_type'] == 'code' and 'def ' in src:
                print(f'\n=== {label} Cell {i} (id={c.get("id")}) ===')
                print(src[:300])
                print('---')
