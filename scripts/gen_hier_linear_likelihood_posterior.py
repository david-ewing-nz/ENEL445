"""
Generate hierarchical_linear_likelihood_posterior.png
Analogous to linear_prior_likelihood_posterior.png in CS1.
Run from repo root: python scripts/gen_hier_linear_likelihood_posterior.py
"""
import sys
import numpy as np
import polars as pl
import matplotlib.pyplot as plt
from pathlib import Path

ROOT   = Path(__file__).resolve().parents[1]
FIGS   = ROOT / 'figs'
DATA   = ROOT / 'results' / 'data'
SEED   = 82171165
CASE   = 'hierarchical_linear'

sys.path.insert(0, str(ROOT / 'python'))
from vb_utils_py import set_pub_style
set_pub_style()

# ── Load saved data ───────────────────────────────────────────────────────────
df_data = pl.read_parquet(DATA / f'{CASE}_data.parquet')
x       = df_data['x'].to_numpy()
y       = df_data['y'].to_numpy()
X       = np.column_stack([df_data['X0'].to_numpy(), df_data['X1'].to_numpy()])
groups  = np.array(df_data['group'].to_list())
J       = 5
N       = len(x)
n_groups = np.array([np.sum(groups == j) for j in range(J)])

beta_true  = np.array([1.0, 2.0])
tau_e_true = 4.0

# ── Re-run CAVI (< 1 s) ───────────────────────────────────────────────────────
ALPHA_E, GAMMA_E, ALPHA_U, GAMMA_U, LAM = 1.0, 0.1, 1.0, 0.1, 0.1
mu_beta    = np.linalg.lstsq(X, y, rcond=None)[0]
Sigma_beta = 0.01 * np.eye(2)
m = np.zeros(J);  v = np.ones(J) * 0.1
a_e = 2.0;  b_e = 1.0;  a_u = 2.0;  b_u = 1.0
for _ in range(500):
    E_tau_e = a_e / b_e
    E_tau_u = a_u / b_u
    y_tilde = y - m[groups]
    Sigma_beta = np.linalg.inv(E_tau_e * X.T @ X + LAM * np.eye(2))
    mu_beta    = E_tau_e * Sigma_beta @ X.T @ y_tilde
    r = y - X @ mu_beta
    for j in range(J):
        idx_j  = groups == j
        v[j]   = 1.0 / (E_tau_e * n_groups[j] + E_tau_u)
        m[j]   = v[j] * E_tau_e * np.sum(r[idx_j])
    resid  = y - X @ mu_beta - m[groups]
    XSX    = np.einsum('ij,jk,ik->i', X, Sigma_beta, X)
    a_e    = ALPHA_E + N / 2
    b_e    = GAMMA_E + 0.5 * (np.sum(resid ** 2) + np.sum(XSX) + np.sum(v[groups]))
    a_u    = ALPHA_U + J / 2
    b_u    = GAMMA_U + 0.5 * np.sum(m ** 2 + v)

print(f'CAVI: mu_beta={mu_beta.round(4)}, E[tau_e]={a_e/b_e:.4f}')

# ── Figure ────────────────────────────────────────────────────────────────────
x_plot = np.linspace(-2, 2, 300)
X_plot = np.column_stack([np.ones(300), x_plot])

sigma_e   = 1.0 / np.sqrt(tau_e_true)
like_mean = X_plot @ beta_true
like_band = 2.0 * sigma_e

post_mean = X_plot @ mu_beta
post_var  = np.array([X_plot[i] @ Sigma_beta @ X_plot[i] for i in range(len(x_plot))])
post_band = 2.0 * np.sqrt(post_var)

group_colors = plt.cm.tab10(np.linspace(0, 0.5, J))

fig, ax = plt.subplots(figsize=(8, 5))

ax.fill_between(x_plot,
                like_mean - like_band,
                like_mean + like_band,
                alpha=0.18, color='tomato',
                label=rf'Likelihood 95% band  ($\pm 2\sigma_e={2*sigma_e:.1f}$)')
ax.plot(x_plot, like_mean, 'r--', lw=1.8,
        label=rf'Likelihood mean  $y={beta_true[0]:.1f}+{beta_true[1]:.1f}x$')

for j in range(J):
    idx_j = groups == j
    ax.scatter(x[idx_j], y[idx_j], color=group_colors[j],
               s=18, alpha=0.60, label=f'Group {j+1}')

ax.fill_between(x_plot,
                post_mean - post_band,
                post_mean + post_band,
                alpha=0.35, color='steelblue',
                label='Posterior 95% CI (CAVI)')
ax.plot(x_plot, post_mean, color='steelblue', lw=2.0,
        label=rf'Posterior mean (CAVI)  $y={mu_beta[0]:.2f}+{mu_beta[1]:.2f}x$')

y_margin = 1.0
ax.set_ylim(y.min() - y_margin, y.max() + y_margin)
ax.set_xlim(x_plot[0], x_plot[-1])
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.set_title(
    rf'Likelihood and posterior (CAVI) — $N={N}$ observations, $J={J}$ groups',
    fontsize=11)
ax.legend(fontsize=8, loc='upper left', ncol=2)
plt.tight_layout()

out = FIGS / f'{CASE}_likelihood_posterior.png'
fig.savefig(out, dpi=300, bbox_inches='tight', pad_inches=0.05)
plt.close(fig)
print(f'Saved: {out}')
