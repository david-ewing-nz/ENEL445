import polars as pl
from pathlib import Path

DATA = Path('results/data')

for name in ['linear_opt.parquet', 'linear_gibbs.parquet',
             'hierarchical_linear_opt.parquet', 'hierarchical_linear_gibbs.parquet',
             'hierarchical_logistic_opt.parquet', 'hierarchical_logistic_gibbs.parquet']:
    p = DATA / name
    if p.exists():
        df = pl.read_parquet(p)
        print(f'\n=== {name} ===')
        print(f'  shape: {df.shape}')
        print(f'  cols: {df.columns}')
        if df.shape[0] > 0:
            print(f'  head(3): {df.head(3)}')
