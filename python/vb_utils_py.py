"""
Utility Functions for VI1 Python Implementation
Provides: Archive management, Parquet I/O, Plotting helpers

Date: 2026-03-05
"""

import numpy as np
import polars as pl
from pathlib import Path
from datetime import datetime
import shutil
import matplotlib.pyplot as plt
from scipy import stats


def create_archive_structure(timestamp=None):
    """
    Create timestamped archive folder structure.
    
    Returns:
        dict: Paths to archive directories
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d%H%M")
    
    archive_base = Path("..") / "archive" / timestamp
    archive_figs = archive_base / "figs"
    archive_results = archive_base / "results"
    archive_python = archive_base / "python"
    
    # Create directories
    archive_figs.mkdir(parents=True, exist_ok=True)
    archive_results.mkdir(parents=True, exist_ok=True)
    archive_python.mkdir(parents=True, exist_ok=True)
    
    return {
        'timestamp': timestamp,
        'base': archive_base,
        'figs': archive_figs,
        'results': archive_results,
        'python': archive_python
    }


def save_results_parquet(data, filename, archive_paths):
    """
    Save results to parquet (in archive and main results folder).
    
    Args:
        data: dict or polars DataFrame
        filename: str, must end with '_py.parquet'
        archive_paths: dict from create_archive_structure()
    """
    if not filename.endswith('_py.parquet'):
        raise ValueError("Filename must end with '_py.parquet' to avoid R file conflicts")
    
    # Convert dict to polars DataFrame if needed
    if isinstance(data, dict):
        df = pl.DataFrame(data)
    else:
        df = data
    
    # Save to archive
    archive_file = archive_paths['results'] / filename
    df.write_parquet(archive_file)
    
    # Copy to main results folder
    main_results = Path("..") / "results"
    main_results.mkdir(parents=True, exist_ok=True)
    shutil.copy2(archive_file, main_results / filename)
    
    print(f"Saved: {filename}")
    return archive_file


def save_python_source(source_files, archive_paths):
    """
    Save Python source code to archive for reproducibility.
    
    Args:
        source_files: list of str or Path objects (relative to python folder)
        archive_paths: dict from create_archive_structure()
    """
    python_dir = Path(".")  # Current directory should be python/
    
    for source_file in source_files:
        source_path = python_dir / source_file
        if source_path.exists():
            dest_path = archive_paths['python'] / source_file
            shutil.copy2(source_path, dest_path)
    
    print(f"Copied {len(source_files)} Python source file(s) to archive")


def save_plot(fig, filename, archive_paths, dpi=300):
    """
    Save plot to PNG (in archive and main figs folder).
    
    Args:
        fig: matplotlib figure
        filename: str, must end with '_py.png'
        archive_paths: dict from create_archive_structure()
        dpi: int, resolution (default 300 for publication quality)
    """
    if not filename.endswith('_py.png'):
        raise ValueError("Filename must end with '_py.png' to avoid R file conflicts")
    
    # Save to archive
    archive_file = archive_paths['figs'] / filename
    fig.savefig(archive_file, dpi=dpi, bbox_inches='tight', pad_inches=0.05)
    
    # Copy to main figs folder
    main_figs = Path("..") / "figs"
    main_figs.mkdir(parents=True, exist_ok=True)
    shutil.copy2(archive_file, main_figs / filename)
    
    print(f"Saved: {filename}")
    plt.close(fig)
    return archive_file


def load_results_parquet(filename, from_archive=False, timestamp=None):
    """
    Load results from parquet file.
    
    Args:
        filename: str, parquet filename
        from_archive: bool, if True load from archive
        timestamp: str, archive timestamp (if from_archive=True)
    
    Returns:
        polars DataFrame
    """
    if from_archive:
        if timestamp is None:
            raise ValueError("Must provide timestamp to load from archive")
        file_path = Path("..") / "archive" / timestamp / "results" / filename
    else:
        file_path = Path("..") / "results" / filename
    
    return pl.read_parquet(file_path)


def plot_convergence_trace(history, param_name, true_value=None, 
                           title=None, figsize=(8, 5)):
    """
    Plot parameter convergence trace.
    
    Args:
        history: np.array of parameter values over iterations
        param_name: str, parameter name for labels
        true_value: float, true parameter value (optional, for reference line)
        title: str, plot title
        figsize: tuple, figure size
    
    Returns:
        matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    iterations = np.arange(1, len(history) + 1)
    ax.plot(iterations, history, 'b-', linewidth=1.5, label=f'E[{param_name}]')
    
    if true_value is not None:
        ax.axhline(y=true_value, color='red', linestyle='--', 
                  linewidth=1.5, label=f'True {param_name}')
    
    ax.set_xlabel('Iteration', fontsize=11)
    ax.set_ylabel(f'E[{param_name}]', fontsize=11)
    if title:
        ax.set_title(title, fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    return fig


def plot_elbo_trace(elbo_history, title=None, figsize=(8, 5)):
    """
    Plot ELBO (Evidence Lower Bound) convergence.
    
    Args:
        elbo_history: np.array of ELBO values over iterations
        title: str, plot title
        figsize: tuple, figure size
    
    Returns:
        matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    iterations = np.arange(1, len(elbo_history) + 1)
    ax.plot(iterations, elbo_history, color='darkgreen', linewidth=1.5)
    
    ax.set_xlabel('Iteration', fontsize=11)
    ax.set_ylabel('ELBO', fontsize=11)
    if title:
        ax.set_title(title, fontsize=12)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_posterior_comparison(param_name, vb_dist, gibbs_samples=None, 
                              true_value=None, sd_ratio=None,
                              figsize=(6, 5)):
    """
    Plot VB vs Gibbs posterior comparison for a single parameter.
    
    Args:
        param_name: str, parameter name for title/labels
        vb_dist: dict with 'type' ('normal' or 'gamma'), 'mean', 'sd' (or 'shape', 'rate')
        gibbs_samples: np.array, Gibbs posterior samples (optional)
        true_value: float, true parameter value (optional)
        sd_ratio: float, VB_SD / Gibbs_SD (optional, for under-dispersion detection)
        figsize: tuple, figure size
    
    Returns:
        matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot Gibbs density if available
    if gibbs_samples is not None:
        ax.hist(gibbs_samples, bins=30, density=True, alpha=0.4, 
               color='#E7298A', label='Gibbs', edgecolor='#E7298A', linewidth=1.5)
    
    # Plot VB density
    if vb_dist['type'] == 'normal':
        x_range = vb_dist['mean'] + np.array([-4, 4]) * vb_dist['sd']
        if gibbs_samples is not None:
            x_range = np.array([
                min(x_range[0], gibbs_samples.min()),
                max(x_range[1], gibbs_samples.max())
            ])
        x = np.linspace(x_range[0], x_range[1], 200)
        y = stats.norm.pdf(x, vb_dist['mean'], vb_dist['sd'])
        ax.plot(x, y, 'k-', linewidth=2, label='VB')
        
    elif vb_dist['type'] == 'gamma':
        x_range = stats.gamma.ppf([0.001, 0.999], vb_dist['shape'], scale=1/vb_dist['rate'])
        if gibbs_samples is not None:
            x_range = np.array([
                max(0.001, min(x_range[0], gibbs_samples.min())),
                max(x_range[1], gibbs_samples.max())
            ])
        x = np.linspace(x_range[0], x_range[1], 200)
        y = stats.gamma.pdf(x, vb_dist['shape'], scale=1/vb_dist['rate'])
        ax.plot(x, y, 'k-', linewidth=2, label='VB')
    
    # True value line
    if true_value is not None:
        ax.axvline(x=true_value, color='blue', linestyle='--', 
                  linewidth=1.5, label='True')
    
    # Title with SD ratio if available
    title = param_name
    if sd_ratio is not None:
        title += f' (SD ratio: {sd_ratio:.3f})'
    ax.set_title(title, fontsize=12)
    
    ax.set_xlabel(param_name, fontsize=11)
    ax.set_ylabel('Density', fontsize=11)
    ax.legend(frameon=True, fontsize=10)
    ax.grid(True, alpha=0.2)
    
    plt.tight_layout()
    return fig


def create_multipanel_comparison(param_list, nrows=2, ncols=2, figsize=(12, 10)):
    """
    Create multi-panel posterior comparison plot.
    
    Args:
        param_list: list of dicts, each with:
            - 'name': parameter name
            - 'vb_dist': VB distribution dict
            - 'gibbs_samples': Gibbs samples (optional)
            - 'true_value': true value (optional)
            - 'sd_ratio': SD ratio (optional)
        nrows: int, number of rows
        ncols: int, number of columns
        figsize: tuple, overall figure size
    
    Returns:
        matplotlib figure
    """
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    axes = axes.flatten() if isinstance(axes, np.ndarray) else [axes]
    
    for idx, param_info in enumerate(param_list):
        if idx >= len(axes):
            break
        
        ax = axes[idx]
        plt.sca(ax)
        
        # Gibbs histogram
        gibbs_samples = param_info.get('gibbs_samples')
        if gibbs_samples is not None:
            ax.hist(gibbs_samples, bins=30, density=True, alpha=0.4,
                   color='#E7298A', label='Gibbs', edgecolor='#E7298A', linewidth=1.2)
        
        # VB density
        vb_dist = param_info['vb_dist']
        if vb_dist['type'] == 'normal':
            x_range = vb_dist['mean'] + np.array([-4, 4]) * vb_dist['sd']
            if gibbs_samples is not None:
                x_range = np.array([
                    min(x_range[0], gibbs_samples.min()),
                    max(x_range[1], gibbs_samples.max())
                ])
            x = np.linspace(x_range[0], x_range[1], 200)
            y = stats.norm.pdf(x, vb_dist['mean'], vb_dist['sd'])
            ax.plot(x, y, 'k-', linewidth=1.5, label='VB')
            
        elif vb_dist['type'] == 'gamma':
            x_range = stats.gamma.ppf([0.001, 0.999], vb_dist['shape'], scale=1/vb_dist['rate'])
            if gibbs_samples is not None:
                x_range = np.array([
                    max(0.001, min(x_range[0], gibbs_samples.min())),
                    max(x_range[1], gibbs_samples.max())
                ])
            x = np.linspace(x_range[0], x_range[1], 200)
            y = stats.gamma.pdf(x, vb_dist['shape'], scale=1/vb_dist['rate'])
            ax.plot(x, y, 'k-', linewidth=1.5, label='VB')
        
        # True value
        true_value = param_info.get('true_value')
        if true_value is not None:
            ax.axvline(x=true_value, color='blue', linestyle='--', 
                      linewidth=1.2, label='True')
        
        # Title with SD ratio
        title = param_info['name']
        sd_ratio = param_info.get('sd_ratio')
        if sd_ratio is not None:
            title += f'\n(SD ratio: {sd_ratio:.3f})'
        ax.set_title(title, fontsize=10)
        
        ax.set_xlabel(param_info['name'], fontsize=9)
        ax.set_ylabel('Density', fontsize=9)
        if idx == 0:  # Legend only on first plot
            ax.legend(frameon=True, fontsize=9, loc='best')
        ax.grid(True, alpha=0.2)
    
    # Hide unused subplots
    for idx in range(len(param_list), len(axes)):
        axes[idx].axis('off')
    
    plt.tight_layout()
    return fig


def print_summary_statistics(results_dict, title="Summary Statistics"):
    """
    Print formatted summary statistics.
    
    Args:
        results_dict: dict with parameter names as keys, values as dicts with 'mean', 'sd', etc.
        title: str, section title
    """
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)
    
    for param_name, param_stats in results_dict.items():
        print(f"\n{param_name}:")
        for stat_name, stat_value in param_stats.items():
            if isinstance(stat_value, (int, float, np.number)):
                print(f"  {stat_name}: {stat_value:.6f}")
            elif isinstance(stat_value, np.ndarray) and stat_value.size <= 10:
                print(f"  {stat_name}: {stat_value}")
    
    print("=" * 70 + "\n")


def set_random_seed(seed=82171165):
    """Set random seed for reproducibility (matching R code)."""
    np.random.seed(seed)
    print(f"Random seed set to: {seed}")


# ─────────────────────────────────────────────────────────────────────────────
# Publication-quality figure style
# ─────────────────────────────────────────────────────────────────────────────

# IEEE-compatible colour cycle (colorblind-safe, distinguishable in greyscale).
# Based on Paul Tol's "bright" palette.
_PUB_COLOURS = [
    '#0077BB',   # blue         – primary lines / VB
    '#EE7733',   # orange       – second series
    '#009988',   # teal         – third series
    '#CC3311',   # red          – fourth series / error
    '#33BBEE',   # cyan         – fifth series
    '#EE3377',   # magenta      – sixth series
    '#BBBBBB',   # grey         – reference / Gibbs fill
]

# Markers matched to colours (used when lines share the same colour)
_PUB_MARKERS = ['o', 's', '^', 'D', 'v', 'P', 'X']


def set_pub_style():
    """
    Apply publication-quality matplotlib rcParams for IEEE-style figures.

    Call once per notebook before any plotting cell:

        from vb_utils_py import set_pub_style
        set_pub_style()

    Settings
    --------
    - Font: Latin Modern Roman (matches LaTeX body text); falls back to serif.
    - Font sizes: 9 pt axis labels / tick labels, 9 pt legend, 10 pt title.
      These map to ~100 % size when figures are included at full column width
      (86 mm / 3.39 in) in a two-column IEEE paper.
    - Line widths: 1.5 pt data lines, 0.8 pt axes/grid.
    - Marker size: 5 pt (visible but not dominant).
    - Grid: light grey, alpha 0.35, behind data (zorder 0).
    - Figure size default: (5.0, 3.5) inches — fits one IEEE column.
    - DPI: 300 for saved files.
    - Colour cycle: Paul Tol "bright" (colorblind-safe, greyscale-distinguishable).
    """
    plt.rcParams.update({
        # ── Font ──────────────────────────────────────────────────────────────
        'font.family':          'serif',
        'font.serif':           ['Latin Modern Roman', 'CMU Serif',
                                 'Computer Modern Roman', 'DejaVu Serif'],
        'font.size':            9,
        'axes.titlesize':       10,
        'axes.labelsize':       9,
        'xtick.labelsize':      8,
        'ytick.labelsize':      8,
        'legend.fontsize':      8,
        'legend.title_fontsize':9,
        'figure.titlesize':     11,

        # ── Lines & markers ───────────────────────────────────────────────────
        'lines.linewidth':      1.5,
        'lines.markersize':     5,
        'patch.linewidth':      0.8,

        # ── Axes ──────────────────────────────────────────────────────────────
        'axes.linewidth':       0.8,
        'axes.spines.top':      False,
        'axes.spines.right':    False,
        'axes.prop_cycle':      plt.cycler('color', _PUB_COLOURS),
        'axes.formatter.use_mathtext': True,

        # ── Grid ──────────────────────────────────────────────────────────────
        'axes.grid':            True,
        'grid.color':           '#CCCCCC',
        'grid.linewidth':       0.6,
        'grid.alpha':           0.5,
        'axes.axisbelow':       True,

        # ── Ticks ─────────────────────────────────────────────────────────────
        'xtick.major.width':    0.8,
        'ytick.major.width':    0.8,
        'xtick.minor.visible':  False,
        'ytick.minor.visible':  False,
        'xtick.direction':      'out',
        'ytick.direction':      'out',

        # ── Legend ────────────────────────────────────────────────────────────
        'legend.frameon':       True,
        'legend.framealpha':    0.9,
        'legend.edgecolor':     '#CCCCCC',
        'legend.borderpad':     0.4,
        'legend.labelspacing':  0.3,
        'legend.handlelength':  1.5,

        # ── Figure ────────────────────────────────────────────────────────────
        'figure.figsize':       (5.0, 3.5),
        'figure.dpi':           150,          # screen preview
        'savefig.dpi':          300,          # saved PNGs
        'savefig.bbox':         'tight',
        'savefig.pad_inches':   0.05,

        # ── Math text ─────────────────────────────────────────────────────────
        'mathtext.fontset':     'cm',
        'mathtext.rm':          'serif',
    })
    print("Publication style applied  (IEEE-compatible, serif fonts, 300 dpi).")


def pub_colours():
    """Return the publication colour list."""
    return list(_PUB_COLOURS)


def pub_markers():
    """Return the publication marker list."""
    return list(_PUB_MARKERS)
