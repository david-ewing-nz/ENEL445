"""
Regenerate only the vb_gibbs density figures (with prior overlay) for CS1, CS4, CS5.
Loads saved results from parquet/pkl; does NOT re-run MCMC or optimisers.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats
import polars as pl

ROOT  = Path(__file__).parent.parent
FIGS  = ROOT / 'figs'
DATA  = ROOT / 'results' / 'data'
sys.path.insert(0, str(ROOT / 'python'))
from vb_utils_py import set_pub_style
set_pub_style()

def save_fig(fig, name):
    path = FIGS / name
    fig.savefig(path, dpi=300, bbox_inches='tight', pad_inches=0.05)
    print(f'  Saved: {path.name}')
    plt.close(fig)

method_colors = {
    'CAVI':            'steelblue',
    'Gradient Ascent': 'darkorange',
    "Newton's Method": 'forestgreen',
    'BFGS':            'purple',
}

# ════════════════════════════════════════════════════════════════════════════
# CS1 — linear
# ════════════════════════════════════════════════════════════════════════════
print('\n── CS1: linear ──')
import pickle, os

cs1_pkl = DATA / 'linear_results.pkl'
if not cs1_pkl.exists():
    print(f'  Missing {cs1_pkl} — re-running CAVI only for CS1 figures')
    from vb_algorithms_py import SimpleLinearVB
    df = pl.read_parquet(DATA / 'linear_data.parquet')
    X  = np.column_stack([df['X0'].to_numpy(), df['X1'].to_numpy()])
    y  = df['y'].to_numpy()
    beta_true  = np.array([2.0, 1.5])
    tau_e_true = 4.0
    n, p = X.shape
    vb = SimpleLinearVB(X, y)
    res = vb.fit(max_iter=500, tol=1e-8)
    methods = {'CAVI': {'mu': res['mu_beta'], 'Sigma': res['Sigma_beta'],
                        'a': res['a_e'], 'b': res['b_e']}}
    # Gibbs samples not available without pkl — skip
    print('  No Gibbs samples available; skipping CS1 vb_gibbs figures.')
else:
    with open(cs1_pkl, 'rb') as f:
        d = pickle.load(f)
    methods   = d['methods']
    samples   = d['samples']       # (n_samples, n_params)
    beta_true   = d['beta_true']
    tau_e_true  = d['tau_e_true']
    p           = len(beta_true)

    prior_beta_mu    = 0.0
    prior_beta_sigma = np.sqrt(10.0)

    for col_idx, pname in enumerate(['beta0', 'beta1', 'tau_e']):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(samples[:, col_idx], bins=50, density=True,
                color='#E7298A', alpha=0.35, label='Gibbs', edgecolor='none')
        x_lo = samples[:, col_idx].min()
        x_hi = samples[:, col_idx].max()
        xv = np.linspace(x_lo, x_hi, 300)
        if col_idx < p:
            yd_prior = stats.norm.pdf(xv, prior_beta_mu, prior_beta_sigma)
            ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                    label=r'Prior $\beta \sim \mathcal{N}(0,10)$')
        for mname, mp in methods.items():
            if col_idx < p:
                sd = np.sqrt(mp['Sigma'][col_idx, col_idx])
                yd = stats.norm.pdf(xv, mp['mu'][col_idx], sd)
            else:
                yd = stats.gamma.pdf(xv, mp['a'], scale=1.0/mp['b'])
            ax.plot(xv, yd, lw=1.5, color=method_colors[mname], label=mname)
        tv = beta_true[col_idx] if col_idx < p else tau_e_true
        ax.axvline(tv, color='black', lw=1.2, ls=':', label='True')
        ax.set_xlabel(pname); ax.set_ylabel('Density')
        ax.set_title(f'VB vs Gibbs posterior: {pname}')
        ax.legend(fontsize=8)
        plt.tight_layout()
        save_fig(fig, f'linear_vb_gibbs_{pname}.png')

# ════════════════════════════════════════════════════════════════════════════
# CS4 — hierarchical linear
# ════════════════════════════════════════════════════════════════════════════
print('\n── CS4: hierarchical linear ──')
cs4_pkl = DATA / 'hierarchical_linear_results.pkl'
if not cs4_pkl.exists():
    print(f'  Missing {cs4_pkl} — skipping CS4 vb_gibbs figures.')
else:
    import pickle
    with open(cs4_pkl, 'rb') as f:
        d = pickle.load(f)
    methods_vb      = d['methods_vb']
    samples         = d['samples']
    param_names     = d['param_names']
    scalar_params   = d['scalar_params']
    true_vals_scalar= d['true_vals_scalar']
    p               = d['p']
    CASE            = 'hierarchical_linear'
    LAM             = d.get('LAM', 0.1)
    ALPHA_E         = d.get('ALPHA_E', 1.0)
    GAMMA_E         = d.get('GAMMA_E', 0.1)
    ALPHA_U         = d.get('ALPHA_U', 1.0)
    GAMMA_U         = d.get('GAMMA_U', 0.1)

    prior_beta_mu    = 0.0
    prior_beta_sigma = np.sqrt(1.0 / LAM)

    for col_idx, pname in enumerate(scalar_params):
        samps_col = samples[:, param_names.index(pname)]
        fig, ax   = plt.subplots(figsize=(6, 4))
        ax.hist(samps_col, bins=50, density=True,
                color='#E7298A', alpha=0.35, label='Gibbs', edgecolor='none')
        xlo = samps_col.min();  xhi = samps_col.max()
        xv  = np.linspace(xlo, xhi, 300)
        if col_idx < p:
            yd_prior = stats.norm.pdf(xv, prior_beta_mu, prior_beta_sigma)
            ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                    label=fr'Prior $\beta \sim \mathcal{{N}}(0,{1/LAM:.0f})$')
        elif pname == 'tau_e':
            yd_prior = stats.gamma.pdf(xv, ALPHA_E, scale=1.0/GAMMA_E)
            ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                    label=f'Prior Gamma({ALPHA_E:.0f},{GAMMA_E})')
        else:
            yd_prior = stats.gamma.pdf(xv, ALPHA_U, scale=1.0/GAMMA_U)
            ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                    label=f'Prior Gamma({ALPHA_U:.0f},{GAMMA_U})')
        for mname, mp in methods_vb.items():
            if col_idx < p:
                sd = np.sqrt(mp['Sig'][col_idx, col_idx])
                yd = stats.norm.pdf(xv, mp['mu'][col_idx], sd)
            elif pname == 'tau_e':
                yd = stats.gamma.pdf(xv, mp['a_e'], scale=1.0/mp['b_e'])
            else:
                yd = stats.gamma.pdf(xv, mp['a_u'], scale=1.0/mp['b_u'])
            ax.plot(xv, yd, lw=1.5, color=method_colors[mname], label=mname)
        ax.axvline(true_vals_scalar[col_idx], color='black', lw=1.2, ls=':', label='True')
        ax.set_xlabel(pname);  ax.set_ylabel('Density')
        ax.set_title(f'VB vs Gibbs: {pname}');  ax.legend(fontsize=8)
        plt.tight_layout()
        save_fig(fig, f'{CASE}_vb_gibbs_{pname}.png')

# ════════════════════════════════════════════════════════════════════════════
# CS5 — hierarchical logistic
# ════════════════════════════════════════════════════════════════════════════
print('\n── CS5: hierarchical logistic ──')
cs5_pkl = DATA / 'hierarchical_logistic_results.pkl'
if not cs5_pkl.exists():
    print(f'  Missing {cs5_pkl} — skipping CS5 vb_gibbs figures.')
else:
    with open(cs5_pkl, 'rb') as f:
        d = pickle.load(f)
    methods_vb      = d['methods_vb']
    samples         = d['samples']
    param_names     = d['param_names']
    scalar_params   = d['scalar_params']
    true_vals_scalar= d['true_vals_scalar']
    p               = d['p']
    CASE            = 'hierarchical_logistic'
    LAM             = d.get('LAM', 0.1)
    ALPHA_U         = d.get('ALPHA_U', 1.0)
    GAMMA_U         = d.get('GAMMA_U', 0.1)

    prior_beta_mu    = 0.0
    prior_beta_sigma = np.sqrt(1.0 / LAM)

    for col_idx, pname in enumerate(scalar_params):
        samps_col = samples[:, param_names.index(pname)]
        fig, ax   = plt.subplots(figsize=(6, 4))
        ax.hist(samps_col, bins=50, density=True,
                color='#E7298A', alpha=0.35, label='PG Gibbs', edgecolor='none')
        xlo = samps_col.min();  xhi = samps_col.max()
        xv  = np.linspace(xlo, xhi, 300)
        if col_idx < p:
            yd_prior = stats.norm.pdf(xv, prior_beta_mu, prior_beta_sigma)
            ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                    label=fr'Prior $\beta \sim \mathcal{{N}}(0,{1/LAM:.0f})$')
        else:
            yd_prior = stats.gamma.pdf(xv, ALPHA_U, scale=1.0/GAMMA_U)
            ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                    label=f'Prior Gamma({ALPHA_U:.0f},{GAMMA_U})')
        for mname, mp in methods_vb.items():
            if col_idx < p:
                sd = np.sqrt(mp['Sig'][col_idx, col_idx])
                yd = stats.norm.pdf(xv, mp['mu'][col_idx], sd)
            else:
                yd = stats.gamma.pdf(xv, mp['a_u'], scale=1.0 / mp['b_u'])
            ax.plot(xv, yd, lw=1.5, color=method_colors[mname], label=mname)
        ax.axvline(true_vals_scalar[col_idx], color='black', lw=1.2, ls=':', label='True')
        ax.set_xlabel(pname);  ax.set_ylabel('Density')
        ax.set_title(f'VB vs PG Gibbs: {pname}');  ax.legend(fontsize=8)
        plt.tight_layout()
        save_fig(fig, f'{CASE}_vb_gibbs_{pname}.png')

print('\nDone.')
