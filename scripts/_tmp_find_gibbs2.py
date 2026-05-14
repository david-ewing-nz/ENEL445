import json

for nbfile, label in [
    ('python/hierarchical_linear_run.ipynb', 'CS4'),
    ('python/hierarchical_logistic_run.ipynb', 'CS5'),
]:
    nb = json.load(open(nbfile, encoding='utf-8'))
    for i, c in enumerate(nb['cells']):
        src = ''.join(c.get('source', []))
        if ('gibbs' in src.lower() or 'mcmc' in src.lower()) and c['cell_type'] == 'code' and 'n_iter' in src:
            print(f'\n=== {label} Cell {i} (id={c.get("id")}) ===')
            print(src[:600])
            break
