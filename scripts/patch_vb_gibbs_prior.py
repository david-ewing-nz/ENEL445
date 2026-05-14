"""
Patch vb_gibbs density cells in CS1, CS4, CS5 notebooks
to add a prior overlay curve.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ── CS1: linear_run.ipynb  (cell id: 801792de) ──────────────────────────────
cs1_src = """\
# Per-component VB vs Gibbs overlay with prior
method_colors = {'CAVI': 'steelblue', 'Gradient Ascent': 'darkorange',
                 "Newton's Method": 'forestgreen', 'BFGS': 'purple'}

# Prior parameters (beta ~ N(0, 10*I); tau_e prior is flat -- not plotted)
prior_beta_mu    = 0.0
prior_beta_sigma = np.sqrt(10.0)

for col_idx, pname in enumerate(['beta0', 'beta1', 'tau_e']):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(samples[:, col_idx], bins=50, density=True,
            color='#E7298A', alpha=0.35, label='Gibbs', edgecolor='none')
    x_lo = samples[:, col_idx].min()
    x_hi = samples[:, col_idx].max()
    xv = np.linspace(x_lo, x_hi, 300)
    if col_idx < p:  # beta ~ N(0, 10)
        yd_prior = stats.norm.pdf(xv, prior_beta_mu, prior_beta_sigma)
        ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                label=r'Prior $\\beta \\sim \\mathcal{N}(0,10)$')
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
    plt.show()
"""

# ── CS4: hierarchical_linear_run.ipynb  (cell id: hl0027) ───────────────────
cs4_src = """\
# VB vs Gibbs posterior overlay with prior
# Prior: beta ~ N(0, 1/LAM); tau_e ~ Gamma(ALPHA_E, GAMMA_E); tau_u ~ Gamma(ALPHA_U, GAMMA_U)
prior_beta_mu    = 0.0
prior_beta_sigma = np.sqrt(1.0 / LAM)

for col_idx, pname in enumerate(scalar_params):
    samps_col = samples[:, param_names.index(pname)]
    fig, ax   = plt.subplots(figsize=(6, 4))
    ax.hist(samps_col, bins=50, density=True,
            color='#E7298A', alpha=0.35, label='Gibbs', edgecolor='none')
    xlo = samps_col.min();  xhi = samps_col.max()
    xv  = np.linspace(xlo, xhi, 300)
    # Prior overlay
    if col_idx < p:  # beta ~ N(0, 1/LAM)
        yd_prior = stats.norm.pdf(xv, prior_beta_mu, prior_beta_sigma)
        ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                label=r'Prior $\\beta \\sim \\mathcal{N}(0,' + f'{1/LAM:.0f})$')
    elif pname == 'tau_e':  # Gamma(ALPHA_E, rate=GAMMA_E)
        yd_prior = stats.gamma.pdf(xv, ALPHA_E, scale=1.0/GAMMA_E)
        ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                label=f'Prior Gamma({ALPHA_E:.0f},{GAMMA_E})')
    else:  # tau_u ~ Gamma(ALPHA_U, rate=GAMMA_U)
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
    plt.show()
"""

# ── CS5: hierarchical_logistic_run.ipynb  (cell id: hlg0028) ────────────────
cs5_src = """\
# VB vs PG Gibbs posterior overlays with prior
# Prior: beta ~ N(0, 1/LAM); tau_u ~ Gamma(ALPHA_U, rate=GAMMA_U)
prior_beta_mu    = 0.0
prior_beta_sigma = np.sqrt(1.0 / LAM)

for col_idx, pname in enumerate(scalar_params):
    samps_col = samples[:, param_names.index(pname)]
    fig, ax   = plt.subplots(figsize=(6, 4))
    ax.hist(samps_col, bins=50, density=True,
            color='#E7298A', alpha=0.35, label='PG Gibbs', edgecolor='none')
    xlo = samps_col.min();  xhi = samps_col.max()
    xv  = np.linspace(xlo, xhi, 300)
    # Prior overlay
    if col_idx < p:  # beta ~ N(0, 1/LAM)
        yd_prior = stats.norm.pdf(xv, prior_beta_mu, prior_beta_sigma)
        ax.plot(xv, yd_prior, lw=1.5, color='grey', ls='--',
                label=r'Prior $\\beta \\sim \\mathcal{N}(0,' + f'{1/LAM:.0f})$')
    else:  # tau_u ~ Gamma(ALPHA_U, rate=GAMMA_U)
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
    plt.show()
"""

def patch_cell(nb_path, cell_id, new_source):
    nb = json.loads(nb_path.read_text(encoding='utf-8'))
    patched = False
    for c in nb['cells']:
        if c.get('id') == cell_id:
            c['source'] = [line + '\n' for line in new_source.rstrip('\n').splitlines()]
            # Clear stale outputs
            if 'outputs' in c:
                c['outputs'] = []
            if 'execution_count' in c:
                c['execution_count'] = None
            patched = True
            break
    if not patched:
        raise RuntimeError(f'Cell {cell_id} not found in {nb_path}')
    nb_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
    print(f'Patched {nb_path.name} cell {cell_id}')

patch_cell(ROOT / 'python' / 'linear_run.ipynb',                '801792de', cs1_src)
patch_cell(ROOT / 'python' / 'hierarchical_linear_run.ipynb',   'hl0027',   cs4_src)
patch_cell(ROOT / 'python' / 'hierarchical_logistic_run.ipynb', 'hlg0028',  cs5_src)
print('All notebooks patched.')
