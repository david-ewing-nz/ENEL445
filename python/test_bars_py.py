"""
test_bars_py.py - Minimal bar chart test.

Sequence:
  1. Resolve project root, data/, figs/ paths
  2. Create data/ and figs/ if missing
  3. If data/test_bars_py.parquet does not exist: create and save it
  4. Read the parquet file
  5. Plot a two-bar chart (one colour per bar)
  6. Save figure to figs/test_bars_py.png
"""

from pathlib import Path
import polars as pl
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -- paths
project_root = Path(__file__).parent.parent.resolve()
data_dir     = project_root / "data"
figs_dir     = project_root / "figs"
parquet_path = data_dir / "test_bars_py.parquet"
fig_path     = figs_dir / "test_bars_py.png"

# -- ensure folders exist
data_dir.mkdir(parents=True, exist_ok=True)
figs_dir.mkdir(parents=True, exist_ok=True)

# -- create parquet if not present
if not parquet_path.exists():
    df = pl.DataFrame({"label": ["Alpha", "Beta"], "value": [42, 27]})
    df.write_parquet(parquet_path)
    print(f"Created: {parquet_path}")

# -- read parquet (always)
df = pl.read_parquet(parquet_path)
print(f"Loaded:  {parquet_path}")
print(df)

# -- extract data
labels = df["label"].to_list()
values = df["value"].to_list()
colours = ["steelblue", "tomato"]

# -- plot
fig, ax = plt.subplots(figsize=(5, 4))
bars = ax.bar(labels, values, color=colours, width=0.5, edgecolor="black", linewidth=0.7)
ax.bar_label(bars, fmt="%d", padding=3)
ax.set_xlabel("Category")
ax.set_ylabel("Value")
ax.set_title("Test Bar Chart")
ax.set_ylim(0, max(values) * 1.2)
fig.tight_layout()
fig.savefig(fig_path, dpi=300)
plt.close(fig)
print(f"Figure saved: {fig_path}")
