"""
Build python/hierarchical_logistic_run.ipynb
Run from repo root: python scripts/build_hl_logistic_notebook.py

Case Study 5: Hierarchical Bayesian Logistic Regression
Model: y_ij ~ Bernoulli(sigma(x_ij^T beta + u_j)),  u_j ~ N(0, tau_u^-1)
VB: q(beta)=N(mu,Sigma), q(u_j)=N(m_j,v_j), q(tau_u)=Gamma(a_u,b_u)
ELBO: Jaakkola-Jordan bound at optimal xi_ij
Reference sampler: Polya-Gamma blocked Gibbs
"""
import json
from pathlib import Path

OUTPUT = Path(__file__).parent.parent / 'python' / 'hierarchical_logistic_run.ipynb'

_cid = [0]

def _next_id():
    _cid[0] += 1
    return f'hlg{_cid[0]:04d}'

def split_src(s):
    # Convert multi-line string to notebook source list.
    lines = s.split('\n')
    result = [l + '\n' for l in lines]
    if result:
        result[-1] = result[-1].rstrip('\n')
    while result and result[-1] == '':
        result.pop()
    return result

def md(s):
    return {'cell_type': 'markdown', 'id': _next_id(),
            'metadata': {}, 'source': split_src(s)}

def code(s):
    return {'cell_type': 'code', 'execution_count': None, 'id': _next_id(),
            'metadata': {}, 'outputs': [], 'source': split_src(s)}

cells = []

# ── Cell 0: Title ─────────────────────────────────────────────────────────────
cells.append(md(r"""# Hierarchical Logistic Bayesian Regression — Variational Inference

Case Study 5: extends binary logistic regression with J=5 group-level random effects.

**Model:** $y_{ij} \sim \mathrm{Bernoulli}(\sigma(\mathbf{x}_{ij}^T\boldsymbol{\beta} + u_j))$,
$u_j \sim \mathcal{N}(0,\,\tau_u^{-1})$, $\boldsymbol{\beta} \sim \mathcal{N}(0,\,\lambda^{-1}I)$,
$\tau_u \sim \mathrm{Gamma}(\alpha_u,\,\gamma_u)$

**ELBO:** Jaakkola--Jordan lower bound at optimal $\xi_{ij}^* = \sqrt{\mathrm{E}[\psi_{ij}^2]}$

**Five stages:**
1. Data generation
2. ELBO evaluation + gradient verification
3. Optimisation methods (CAVI, gradient ascent, Newton, BFGS)
4. Reference sampler (Polya-Gamma blocked Gibbs)
5. Diagnostics and comparison"""))

# ── Cell 1: Setup ─────────────────────────────────────────────────────────────
cells.append(code(r"""import sys
import numpy as np
import polars as pl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from pathlib import Path
from scipy import stats
from scipy.special import digamma, gammaln, expit
from scipy.optimize import minimize
import time

ROOT   = Path('..').resolve()
FIGS   = ROOT / 'figs'
DATA   = ROOT / 'results' / 'data'
TABLES = ROOT / 'results' / 'tables'
for d in [FIGS, DATA, TABLES]:
    d.mkdir(parents=True, exist_ok=True)

SEED = 82171165
np.random.seed(SEED)

sys.path.insert(0, str(ROOT / 'python'))
from vb_utils_py import set_pub_style, pub_colours, pub_markers
set_pub_style()
COLOURS = pub_colours()
MARKERS = pub_markers()
CASE = 'hierarchical_logistic'

def save_fig(fig, name):
    path = FIGS / name
    fig.savefig(path, dpi=300, bbox_inches='tight', pad_inches=0.05)
    print(f'  Saved: {path.name}')
    plt.close(fig)
    return path

print('Setup complete. ROOT =', ROOT)"""))

# ── Stage 1 ───────────────────────────────────────────────────────────────────
cells.append(md(r"""---
## Stage 1 — Data Generation

Hierarchical logistic regression: N=150, J=5 groups (30 obs each), p=2.

$\beta_\text{true} = (-1.0,\;2.0)$, $\tau_u^\text{true}=2.0$,
$\sigma_u^\text{true} = 1/\sqrt{2} \approx 0.707$."""))

cells.append(code(r"""J           = 5
N_PER_GROUP = 30
N           = J * N_PER_GROUP
p           = 2

beta_true    = np.array([-1.0, 2.0])
tau_u_true   = 2.0
sigma_u_true = 1.0 / np.sqrt(tau_u_true)

np.random.seed(SEED)
x      = np.random.uniform(-2, 2, N)
X      = np.column_stack([np.ones(N), x])
groups = np.repeat(np.arange(J), N_PER_GROUP)
n_groups = np.array([np.sum(groups == j) for j in range(J)])

u_true = np.random.normal(0, sigma_u_true, J)
psi    = X @ beta_true + u_true[groups]
prob   = expit(psi)
y      = np.random.binomial(1, prob).astype(float)

print(f'N={N}, J={J}, p={p}')
print(f'beta_true={beta_true}, tau_u_true={tau_u_true}')
print(f'u_true={u_true.round(3)}')
print(f'y=1: {int(y.sum())},  y=0: {int((1-y).sum())}')

df_data = pl.DataFrame({'x': x, 'y': y,
                         'X0': X[:, 0], 'X1': X[:, 1],
                         'group': groups.tolist()})
df_data.write_parquet(DATA / f'{CASE}_data.parquet')
print(f'Saved: {CASE}_data.parquet')"""))

cells.append(code(r"""group_colors = plt.cm.tab10(np.linspace(0, 0.5, J))
fig, ax = plt.subplots(figsize=(7, 5))
for j in range(J):
    idx = groups == j
    ax.scatter(x[idx], y[idx] + 0.02*np.random.randn(idx.sum()),
               color=group_colors[j], s=20, alpha=0.6, label=f'Group {j+1}')
xs_line = np.linspace(-2.1, 2.1, 300)
X_line  = np.column_stack([np.ones(300), xs_line])
ax.plot(xs_line, expit(X_line @ beta_true), 'k--', lw=1.8, label='Population')
for j in range(J):
    ax.plot(xs_line, expit(X_line @ beta_true + u_true[j]),
            color=group_colors[j], lw=0.8, alpha=0.5, ls=':')
ax.set_xlabel('$x$');  ax.set_ylabel('$y$ (jittered) / $P(y=1|x,u_j)$')
ax.set_title('Hierarchical logistic: observed data by group')
ax.legend(fontsize=8, ncol=3)
plt.tight_layout()
save_fig(fig, f'{CASE}_data_scatter.png')
plt.show()"""))

# ── Stage 2 ───────────────────────────────────────────────────────────────────
cells.append(md(r"""---
## Stage 2 — ELBO Evaluation + Gradient Verification

Unconstrained parameterisation ($p=2$, $J=5$, total $D=17$):
- $\boldsymbol{\mu}_\beta \in \mathbb{R}^2$; Cholesky $\boldsymbol{\Sigma}_\beta$: 3 params
- Random effect means $\mathbf{m} \in \mathbb{R}^5$; $\log\mathbf{v} \in \mathbb{R}^5$
- $\log a_u,\,\log b_u$: 2 params

**ELBO** (Jaakkola--Jordan at optimal $\xi_{ij}^*$):
$$\mathcal{L} = \sum_{ij}\!\left[(y_{ij}-\tfrac{1}{2})\bar\psi_{ij} - \log 2 - \log\cosh\tfrac{\xi_{ij}^*}{2}\right] - \mathrm{KL}(q(\boldsymbol{\beta})\|p(\boldsymbol{\beta})) + \mathrm{E}_q[\log p(\mathbf{u}|\tau_u)] + \mathrm{E}_q[\log p(\tau_u)] + H[q(\mathbf{u})] + H[q(\tau_u)]$$
where $\bar\psi_{ij} = \mathbf{x}_{ij}^T\boldsymbol{\mu}_\beta + m_j$ and $(\xi_{ij}^*)^2 = \bar\psi_{ij}^2 + \mathbf{x}_{ij}^T\boldsymbol{\Sigma}_\beta\mathbf{x}_{ij} + v_j$."""))

cells.append(code(r"""# Prior hyperparameters
ALPHA_U = 1.0;  GAMMA_U = 0.1
LAM     = 0.1   # precision of beta prior

def unpack_hlg(theta, pp, JJ):
    # Unpack unconstrained vector into variational parameters.
    idx = 0
    mu_beta = theta[idx:idx+pp];  idx += pp
    L = np.zeros((pp, pp))
    for i in range(pp):
        L[i, i] = np.exp(theta[idx]);  idx += 1
        for jj in range(i+1, pp):
            L[jj, i] = theta[idx];  idx += 1
    Sigma_beta = L @ L.T
    m   = theta[idx:idx+JJ].copy();        idx += JJ
    v   = np.exp(theta[idx:idx+JJ]);       idx += JJ
    a_u = np.exp(theta[idx]);  idx += 1
    b_u = np.exp(theta[idx]);  idx += 1
    return mu_beta, Sigma_beta, L, m, v, a_u, b_u

def pack_hlg(mu_beta, L, m, v, a_u, b_u):
    # Pack variational parameters into unconstrained vector.
    pp = len(mu_beta);  JJ = len(m)
    t  = list(mu_beta)
    for i in range(pp):
        t.append(np.log(L[i, i]))
        for jj in range(i+1, pp):
            t.append(L[jj, i])
    t.extend(m)
    t.extend(np.log(np.maximum(v, 1e-30)))
    t.extend([np.log(a_u), np.log(b_u)])
    return np.array(t)

D = p + p*(p+1)//2 + J + J + 2
print(f'Unconstrained parameter dimension D={D}')"""))

cells.append(code(r"""def elbo_hlg(theta, X, y, groups, J, n_groups,
             alpha_u=ALPHA_U, gamma_u=GAMMA_U, lam=LAM):
    # ELBO for hierarchical logistic model (Jaakkola-Jordan bound).
    if not np.all(np.isfinite(theta)):
        return -np.inf
    N, pp = X.shape
    mu_beta, Sigma_beta, L, m, v, a_u, b_u = unpack_hlg(theta, pp, J)

    E_tau_u     = a_u / b_u
    E_log_tau_u = digamma(a_u) - np.log(b_u)

    # JJ likelihood at optimal xi_ij
    psi_mean = X @ mu_beta + m[groups]
    XSX      = np.einsum('ij,jk,ik->i', X, Sigma_beta, X)
    s2       = XSX + v[groups]
    xi       = np.maximum(np.sqrt(psi_mean**2 + s2), 1e-10)
    lik      = np.sum((y - 0.5) * psi_mean - np.log(2.) - np.log(np.cosh(xi / 2.)))

    # -KL(q(beta) || p(beta))  split as H[q(beta)] + E[log p(beta)]
    _, logdet = np.linalg.slogdet(Sigma_beta)
    h_beta  = 0.5 * logdet + 0.5 * pp * (1 + np.log(2 * np.pi))
    lp_beta = (-0.5 * pp * np.log(2 * np.pi) + 0.5 * pp * np.log(lam)
               - 0.5 * lam * (np.dot(mu_beta, mu_beta) + np.trace(Sigma_beta)))

    # E[log p(u | tau_u)] — random effects
    lu = (0.5 * J * E_log_tau_u - 0.5 * J * np.log(2 * np.pi)
          - 0.5 * E_tau_u * np.sum(m**2 + v))

    # E[log p(tau_u)]
    lp_tau_u = (alpha_u - 1) * E_log_tau_u - gamma_u * E_tau_u

    # H[q(u)]
    h_u = 0.5 * np.sum(np.log(v)) + 0.5 * J * (1 + np.log(2 * np.pi))

    # H[q(tau_u)]
    h_tau_u = a_u - np.log(b_u) + gammaln(a_u) + (1 - a_u) * digamma(a_u)

    return lik + h_beta + lp_beta + lu + lp_tau_u + h_u + h_tau_u

def _safe_elbo(theta, X, y, groups, J, n_groups):
    # ELBO returning -inf for any invalid (NaN/Inf) result.
    try:
        val = elbo_hlg(theta, X, y, groups, J, n_groups)
        return val if np.isfinite(val) else -np.inf
    except Exception:
        return -np.inf

def elbo_neg(theta, *args):
    return -elbo_hlg(theta, *args)

def elbo_grad_fd(theta, X, y, groups, J, n_groups, h=1e-5):
    g = np.zeros_like(theta)
    for i in range(len(theta)):
        tp, tm = theta.copy(), theta.copy()
        tp[i] += h;  tm[i] -= h
        g[i] = (elbo_hlg(tp, X, y, groups, J, n_groups)
                - elbo_hlg(tm, X, y, groups, J, n_groups)) / (2 * h)
    return g

print('ELBO functions defined.')"""))

cells.append(code(r"""def _warm_cavi(X, y, groups, J, n_groups, n_iter=80):
    # Brief CAVI run to obtain a good linearisation point for gradient verification.
    N, pp = X.shape
    mu_beta    = np.zeros(pp)
    Sigma_beta = np.eye(pp)
    m  = np.zeros(J);  v = np.ones(J) * 0.5
    a_u = 2.0;  b_u = 1.0

    for _ in range(n_iter):
        E_tau_u = a_u / b_u

        # xi update (optimal JJ parameters)
        psi_mean = X @ mu_beta + m[groups]
        XSX      = np.einsum('ij,jk,ik->i', X, Sigma_beta, X)
        s2       = XSX + v[groups]
        xi       = np.maximum(np.sqrt(psi_mean**2 + s2), 1e-10)
        lam_ij   = np.tanh(xi / 2.) / (4. * xi)

        # q(beta)
        Sigma_beta = np.linalg.inv(LAM * np.eye(pp) + 2. * (X.T * lam_ij) @ X)
        rhs        = np.sum((y - 0.5 - 2. * lam_ij * m[groups])[:, None] * X, axis=0)
        mu_beta    = Sigma_beta @ rhs

        # q(u_j)
        psi_beta = X @ mu_beta
        for j in range(J):
            idx_j = groups == j
            v[j]  = 1. / (2. * np.sum(lam_ij[idx_j]) + E_tau_u)
            m[j]  = v[j] * np.sum(y[idx_j] - 0.5 - 2. * lam_ij[idx_j] * psi_beta[idx_j])

        # q(tau_u)
        a_u = ALPHA_U + J / 2.
        b_u = GAMMA_U + 0.5 * np.sum(m**2 + v)

    return mu_beta, Sigma_beta, m, v, a_u, b_u

mu_ws, Sig_ws, m_ws, v_ws, au_ws, bu_ws = _warm_cavi(X, y, groups, J, n_groups)
L_ws     = np.linalg.cholesky(Sig_ws)
theta_ws = pack_hlg(mu_ws, L_ws, m_ws, v_ws, au_ws, bu_ws)
print(f'ELBO at warm start: {elbo_hlg(theta_ws, X, y, groups, J, n_groups):.4f}')
print(f'mu_beta={mu_ws.round(4)},  E[tau_u]={au_ws/bu_ws:.4f}')"""))

cells.append(code(r"""# Gradient verification: FD h=1e-5 vs h=1e-7
grad_fd  = elbo_grad_fd(theta_ws, X, y, groups, J, n_groups, h=1e-5)
grad_ref = elbo_grad_fd(theta_ws, X, y, groups, J, n_groups, h=1e-7)
rel_err  = np.abs(grad_fd - grad_ref) / (np.abs(grad_ref) + 1e-12)

chol_labels = ['$u_{11}$', '$u_{21}$', '$u_{22}$']
m_labels    = [f'$m_{j+1}$'        for j in range(J)]
lv_labels   = [f'$\\log v_{j+1}$'  for j in range(J)]
labels = (['$\\mu_{\\beta_0}$', '$\\mu_{\\beta_1}$']
          + chol_labels + m_labels + lv_labels
          + ['$\\log a_u$', '$\\log b_u$'])

print('Gradient verification (FD h=1e-5 vs h=1e-7):')
for lbl, g1, g2, re in zip(labels, grad_fd, grad_ref, rel_err):
    status = 'OK' if re < 1e-3 else 'WARN'
    print(f'  {lbl:18s}  g1={g1:10.4f}  g2={g2:10.4f}  rel={re:.2e}  {status}')

df_grad = pl.DataFrame({
    'parameter': labels,
    'grad_h1e5': grad_fd.tolist(),
    'grad_h1e7': grad_ref.tolist(),
    'rel_err':   rel_err.tolist(),
})
df_grad.write_parquet(DATA / f'{CASE}_gradient_check.parquet')
print(f'Saved: {CASE}_gradient_check.parquet')"""))

cells.append(code(r"""# Gradient verification bar chart
fig, ax = plt.subplots(figsize=(14, 4))
x_pos = np.arange(D);  w = 0.4
ax.bar(x_pos - w/2, grad_fd,  w, label='FD h=1e-5', color='steelblue', alpha=0.8)
ax.bar(x_pos + w/2, grad_ref, w, label='FD h=1e-7', color='tomato',    alpha=0.8)
ax.set_xticks(x_pos)
ax.set_xticklabels(labels, fontsize=7, rotation=45, ha='right')
ax.set_ylabel('Gradient value')
ax.set_title('ELBO gradient verification at CAVI warm start — hierarchical logistic')
ax.legend()
plt.tight_layout()
save_fig(fig, f'{CASE}_elbo_gradient_check.png')
plt.show()

# Save gradient check table
with open(TABLES / f'{CASE}_gradient_check.tex', 'w') as f:
    f.write('\\begin{tblr}{colspec={lrrr}, hline{1,2,Z}={solid}}\n')
    f.write('  Parameter & Gradient $h=10^{-5}$ & Gradient $h=10^{-7}$ & Rel.\\,error \\\\\n')
    for lbl, g1, g2, re in zip(labels, grad_fd, grad_ref, rel_err):
        f.write(f'  {lbl} & {g1:.4f} & {g2:.4f} & {re:.2e} \\\\\n')
    f.write('\\end{tblr}\n')
print(f'Saved: {CASE}_gradient_check.tex')"""))

cells.append(code(r"""# ELBO landscape: vary mu_beta0 x mu_beta1
mu0_grid = np.linspace(mu_ws[0] - 1.5, mu_ws[0] + 1.5, 50)
mu1_grid = np.linspace(mu_ws[1] - 1.5, mu_ws[1] + 1.5, 50)
Z = np.zeros((len(mu1_grid), len(mu0_grid)))
for ii, mb1 in enumerate(mu1_grid):
    for jj, mb0 in enumerate(mu0_grid):
        t = theta_ws.copy();  t[0] = mb0;  t[1] = mb1
        Z[ii, jj] = elbo_hlg(t, X, y, groups, J, n_groups)

fig, ax = plt.subplots(figsize=(6, 5))
cs = ax.contourf(mu0_grid, mu1_grid, Z, levels=20, cmap='viridis')
plt.colorbar(cs, ax=ax, label='ELBO')
ax.plot(mu_ws[0], mu_ws[1], 'r*', ms=12, label='CAVI warm start')
ax.plot(beta_true[0], beta_true[1], 'w+', ms=12, mew=2, label='True $\\beta$')
ax.set_xlabel('$\\mu_{\\beta_0}$');  ax.set_ylabel('$\\mu_{\\beta_1}$')
ax.set_title('ELBO landscape — hierarchical logistic')
ax.legend(loc='lower right', fontsize=9)
plt.tight_layout()
save_fig(fig, f'{CASE}_elbo_landscape.png')
plt.show()"""))

# ── Stage 3 ───────────────────────────────────────────────────────────────────
cells.append(md(r"""---
## Stage 3 — Optimisation Methods

All four methods share the same starting point $\theta_0$.
CAVI uses closed-form coordinate updates (JJ bound with $\xi_{ij}$ fixed-point iteration).
Gradient-based methods use finite-difference gradients of the ELBO."""))

cells.append(code(r"""# Shared starting point: small Sigma, zero means
L_init    = np.eye(p) * 0.1
m_init    = np.zeros(J)
v_init    = np.ones(J) * 0.5
a_u_init  = 2.0;  b_u_init = 1.0
theta0 = pack_hlg(np.zeros(p), L_init, m_init, v_init, a_u_init, b_u_init)

print(f'theta0 dimension: {theta0.shape[0]}')
print(f'ELBO at theta0: {elbo_hlg(theta0, X, y, groups, J, n_groups):.4f}')"""))

cells.append(code(r"""# --- CAVI ---
def cavi_hlg(X, y, groups, J, n_groups, max_iter=500, tol=1e-8):
    # Coordinate ascent variational inference for hierarchical logistic model.
    N, pp      = X.shape
    mu_beta    = np.zeros(pp)
    Sigma_beta = np.eye(pp)
    m  = np.zeros(J);  v = np.ones(J) * 0.5
    a_u = 2.0;  b_u = 1.0
    elbo_hist  = []
    t0         = time.perf_counter()

    for it in range(max_iter):
        E_tau_u = a_u / b_u

        # xi update
        psi_mean = X @ mu_beta + m[groups]
        XSX      = np.einsum('ij,jk,ik->i', X, Sigma_beta, X)
        s2       = XSX + v[groups]
        xi       = np.maximum(np.sqrt(psi_mean**2 + s2), 1e-10)
        lam_ij   = np.tanh(xi / 2.) / (4. * xi)

        # q(beta)
        Sigma_beta = np.linalg.inv(LAM * np.eye(pp) + 2. * (X.T * lam_ij) @ X)
        rhs        = np.sum((y - 0.5 - 2. * lam_ij * m[groups])[:, None] * X, axis=0)
        mu_beta    = Sigma_beta @ rhs

        # q(u_j)
        psi_beta = X @ mu_beta
        for j in range(J):
            idx_j = groups == j
            v[j]  = 1. / (2. * np.sum(lam_ij[idx_j]) + E_tau_u)
            m[j]  = v[j] * np.sum(y[idx_j] - 0.5 - 2. * lam_ij[idx_j] * psi_beta[idx_j])

        # q(tau_u)
        a_u = ALPHA_U + J / 2.
        b_u = GAMMA_U + 0.5 * np.sum(m**2 + v)

        # ELBO
        L_ch = np.linalg.cholesky(Sigma_beta + 1e-12 * np.eye(pp))
        th   = pack_hlg(mu_beta, L_ch, m.copy(), v.copy(), a_u, b_u)
        elbo_hist.append(elbo_hlg(th, X, y, groups, J, n_groups))
        if it > 0 and abs(elbo_hist[-1] - elbo_hist[-2]) < tol:
            break

    t_end = time.perf_counter() - t0
    return {'mu_beta': mu_beta, 'Sigma_beta': Sigma_beta, 'm': m.copy(), 'v': v.copy(),
            'a_u': a_u, 'b_u': b_u, 'E_tau_u': a_u / b_u,
            'elbo_history': np.array(elbo_hist), 'iterations': it + 1, 'runtime': t_end}

print('Running CAVI...')
res_cavi = cavi_hlg(X, y, groups, J, n_groups)
t_cavi   = res_cavi['runtime']
print(f'CAVI: {res_cavi["iterations"]} iters,  {t_cavi*1000:.1f} ms')
print(f'  mu_beta={res_cavi["mu_beta"].round(4)},  E[tau_u]={res_cavi["E_tau_u"]:.4f}')
print(f'  m={res_cavi["m"].round(3)}')"""))

cells.append(code(r"""# --- Gradient Ascent with Armijo backtracking ---
def gradient_ascent(theta0, X, y, groups, J, n_groups,
                    max_iter=2000, tol=1e-7, alpha0=0.5, c=0.1, rho=0.5):
    theta = theta0.copy()
    elbo_hist, step_hist = [], []
    t0 = time.perf_counter()
    for k in range(max_iter):
        f0 = elbo_hlg(theta, X, y, groups, J, n_groups)
        g  = elbo_grad_fd(theta, X, y, groups, J, n_groups, h=1e-5)
        alpha = alpha0
        for _ in range(30):
            if elbo_hlg(theta + alpha*g, X, y, groups, J, n_groups) >= f0 + c*alpha*np.dot(g, g):
                break
            alpha *= rho
        theta = theta + alpha * g
        elbo_hist.append(elbo_hlg(theta, X, y, groups, J, n_groups))
        step_hist.append(alpha)
        if k > 0 and abs(elbo_hist[-1] - elbo_hist[-2]) < tol:
            break
    return {'theta': theta, 'elbo_history': np.array(elbo_hist),
            'step_history': np.array(step_hist),
            'iterations': k + 1, 'runtime': time.perf_counter() - t0}

print('Running Gradient Ascent...')
res_ga = gradient_ascent(theta0, X, y, groups, J, n_groups)
mu_ga, Sig_ga, _, m_ga, v_ga, au_ga, bu_ga = unpack_hlg(res_ga['theta'], p, J)
print(f'GA: {res_ga["iterations"]} iters,  {res_ga["runtime"]*1000:.1f} ms')
print(f'  mu_beta={mu_ga.round(4)},  E[tau_u]={au_ga/bu_ga:.4f}')"""))

cells.append(code(r"""# --- Newton's Method (17x17 FD Hessian) ---
def hessian_fd(theta, X, y, groups, J, n_groups, h=1e-4):
    n  = len(theta)
    H  = np.zeros((n, n))
    f0 = elbo_hlg(theta, X, y, groups, J, n_groups)
    for i in range(n):
        for jj in range(i, n):
            tp = theta.copy();  tm = theta.copy()
            if i == jj:
                tp[i] += h;  tm[i] -= h
                H[i, i] = (elbo_hlg(tp, X, y, groups, J, n_groups)
                            - 2 * f0
                            + elbo_hlg(tm, X, y, groups, J, n_groups)) / (h * h)
            else:
                tp[i] += h;  tp[jj] += h
                tm[i] -= h;  tm[jj] -= h
                tpq = theta.copy();  tpq[i]  += h
                tmq = theta.copy();  tmq[jj] -= h
                H[i, jj] = H[jj, i] = (
                    elbo_hlg(tp,  X, y, groups, J, n_groups)
                    - elbo_hlg(tpq, X, y, groups, J, n_groups)
                    - elbo_hlg(tmq, X, y, groups, J, n_groups)
                    + elbo_hlg(tm,  X, y, groups, J, n_groups)) / (4 * h * h)
    return H

def newton_method(theta0, X, y, groups, J, n_groups,
                  max_iter=50, tol=1e-7, reg=1e-6):
    theta = theta0.copy()
    elbo_hist, cond_hist = [], []
    t0 = time.perf_counter()
    for k in range(max_iter):
        f0 = _safe_elbo(theta, X, y, groups, J, n_groups)
        if not np.isfinite(f0):
            break
        g = elbo_grad_fd(theta, X, y, groups, J, n_groups)
        if not np.all(np.isfinite(g)):
            break
        H = hessian_fd(theta, X, y, groups, J, n_groups)
        if not np.all(np.isfinite(H)):
            d = g;  cond = float('inf')
        else:
            try:
                eigs = np.linalg.eigvalsh(H)
                if eigs.max() >= 0:
                    H = H - (eigs.max() + reg) * np.eye(len(theta))
                cond = np.linalg.cond(H)
                d = np.linalg.solve(-H, g)
            except np.linalg.LinAlgError:
                d = g;  cond = float('inf')
        if np.dot(g, d) < 0:
            d = g
        alpha = 1.0
        for _ in range(30):
            f_new = _safe_elbo(theta + alpha * d, X, y, groups, J, n_groups)
            if f_new >= f0 + 0.1 * alpha * np.dot(g, d):
                break
            alpha *= 0.5
        theta = theta + alpha * d
        elbo_hist.append(_safe_elbo(theta, X, y, groups, J, n_groups))
        cond_hist.append(cond)
        if k > 0 and abs(elbo_hist[-1] - elbo_hist[-2]) < tol:
            break
    return {'theta': theta, 'elbo_history': np.array(elbo_hist),
            'cond_history': np.array(cond_hist),
            'iterations': k + 1, 'runtime': time.perf_counter() - t0}

print("Running Newton's method (17x17 FD Hessian)...")
res_newton = newton_method(theta0, X, y, groups, J, n_groups)
mu_n, Sig_n, _, m_n, v_n, au_n, bu_n = unpack_hlg(res_newton['theta'], p, J)
print(f"Newton: {res_newton['iterations']} iters,  {res_newton['runtime']:.1f} s")
print(f'  mu_beta={mu_n.round(4)},  E[tau_u]={au_n/bu_n:.4f}')"""))

cells.append(code(r"""# --- BFGS ---
elbo_hist_bfgs = []
def callback_bfgs(theta):
    elbo_hist_bfgs.append(elbo_hlg(theta, X, y, groups, J, n_groups))

print('Running BFGS...')
t0  = time.perf_counter()
opt = minimize(elbo_neg, theta0, args=(X, y, groups, J, n_groups),
               method='BFGS', options={'maxiter': 2000, 'gtol': 1e-7},
               callback=callback_bfgs)
t_bfgs = time.perf_counter() - t0
mu_b, Sig_b, _, m_b, v_b, au_b, bu_b = unpack_hlg(opt.x, p, J)
print(f'BFGS: {opt.nit} iters,  {t_bfgs*1000:.1f} ms,  success={opt.success}')
print(f'  mu_beta={mu_b.round(4)},  E[tau_u]={au_b/bu_b:.4f}')
res_bfgs = {'theta': opt.x, 'elbo_history': np.array(elbo_hist_bfgs),
            'iterations': opt.nit, 'runtime': t_bfgs}"""))

cells.append(code(r"""# ELBO convergence
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(res_cavi['elbo_history'], lw=1.5, color='steelblue', label='CAVI')
axes[0].set_xlabel('Iteration');  axes[0].set_ylabel('ELBO')
axes[0].set_title('CAVI ELBO history — hierarchical logistic');  axes[0].legend()

axes[1].plot(res_ga['elbo_history'],     lw=1.5, label='Gradient Ascent')
axes[1].plot(res_newton['elbo_history'], lw=1.5, label="Newton's Method")
axes[1].plot(res_bfgs['elbo_history'],   lw=1.5, label='BFGS')
axes[1].set_xlabel('Iteration');  axes[1].set_ylabel('ELBO')
axes[1].set_title('ELBO: GA / Newton / BFGS');  axes[1].legend()
plt.tight_layout()
save_fig(fig, f'{CASE}_elbo_convergence.png')
plt.show()

# Step size (gradient ascent)
fig, ax = plt.subplots(figsize=(7, 3))
ax.semilogy(res_ga['step_history'], color='darkorange', lw=1.2)
ax.set_xlabel('Iteration');  ax.set_ylabel('Step size (log)')
ax.set_title('Gradient Ascent: Armijo step size')
plt.tight_layout()
save_fig(fig, f'{CASE}_gradient_stepsize.png')
plt.show()

# Condition number (Newton)
fig, ax = plt.subplots(figsize=(7, 3))
ax.semilogy(res_newton['cond_history'], color='purple', lw=1.2)
ax.set_xlabel('Iteration');  ax.set_ylabel('Condition number (log)')
ax.set_title("Newton: Hessian condition number")
plt.tight_layout()
save_fig(fig, f'{CASE}_newton_condition.png')
plt.show()

# Save optimisation results
runtimes_ms = {
    'CAVI':             t_cavi * 1000,
    'Gradient Ascent':  res_ga['runtime'] * 1000,
    "Newton's Method":  res_newton['runtime'] * 1000,
    'BFGS':             t_bfgs * 1000,
}
df_opt = pl.DataFrame({
    'method':     list(runtimes_ms.keys()),
    'iterations': [res_cavi['iterations'], res_ga['iterations'],
                   res_newton['iterations'], res_bfgs['iterations']],
    'runtime_ms': list(runtimes_ms.values()),
    'final_elbo': [float(res_cavi['elbo_history'][-1]),
                   float(res_ga['elbo_history'][-1]),
                   float(res_newton['elbo_history'][-1]),
                   float(res_bfgs['elbo_history'][-1])],
    'mu_beta0':   [res_cavi['mu_beta'][0], mu_ga[0], mu_n[0], mu_b[0]],
    'mu_beta1':   [res_cavi['mu_beta'][1], mu_ga[1], mu_n[1], mu_b[1]],
    'E_tau_u':    [res_cavi['E_tau_u'], au_ga/bu_ga, au_n/bu_n, au_b/bu_b],
})
df_opt.write_parquet(DATA / f'{CASE}_opt.parquet')
print('Saved:', f'{CASE}_opt.parquet')
print(df_opt)"""))

# ── Stage 4 ───────────────────────────────────────────────────────────────────
cells.append(md(r"""---
## Stage 4 — Reference Sampler: Polya-Gamma Blocked Gibbs

Polson, Scott & Windle (2013) — blocked sampler for hierarchical logistic regression.

**Each sweep** (3 chains $\times$ 2000 iterations, 500 burn-in):
1. Draw $\omega_{ij} \mid \boldsymbol{\beta}, u_j \sim \mathrm{PG}(1,\, \mathbf{x}_{ij}^T\boldsymbol{\beta} + u_j)$
2. Draw $\boldsymbol{\beta} \mid \boldsymbol{\omega}, \mathbf{u}, \mathbf{y} \sim \mathcal{N}(\mathbf{m}_\beta, V_\beta)$
3. Draw $u_j \mid \boldsymbol{\beta}, \boldsymbol{\omega}_j, \mathbf{y}_j, \tau_u \sim \mathcal{N}(m_j^*, v_j^*)$
4. Draw $\tau_u \mid \mathbf{u} \sim \mathrm{Gamma}(\alpha_u + J/2,\; \gamma_u + \tfrac{1}{2}\sum_j u_j^2)$

PG sampler: T=50 truncated gamma approximation."""))

cells.append(code(r"""def sample_pg_one(c, T=50):
    # Sample PG(1, c) using the truncated sum approximation (Polson et al. 2013).
    c = abs(float(c))
    k = np.arange(1, T + 1, dtype=float)
    g = np.random.gamma(1., 1., T)
    return np.sum(g / ((k - 0.5)**2 + (c / (2. * np.pi))**2)) / (2. * np.pi**2)

# Verify: E[PG(1,0)] = 1/4
samp_pg = np.array([sample_pg_one(0.) for _ in range(500)])
print(f'E[PG(1,0)] mean={samp_pg.mean():.4f}  theory=0.2500  (T=50)')"""))

cells.append(code(r"""def gibbs_hl_logistic(X, y, groups, J, n_groups,
                      alpha_u=ALPHA_U, gamma_u=GAMMA_U, lam=LAM,
                      n_iter=2000, n_burnin=500, n_chains=3):
    # Polya-Gamma blocked Gibbs sampler for hierarchical logistic regression.
    N, pp = X.shape
    kappa = y - 0.5          # sufficient statistic
    all_samples = []

    for chain in range(n_chains):
        np.random.seed(SEED + chain)
        beta  = np.zeros(pp)
        u     = np.zeros(J)
        tau_u = 1.0
        chain_samps = []

        for it in range(n_iter):
            # 1. Draw omega_ij | beta, u ~ PG(1, psi_ij)
            psi   = X @ beta + u[groups]
            omega = np.array([sample_pg_one(psi[i]) for i in range(N)])

            # 2. Draw beta | omega, u, y
            V_beta_inv = lam * np.eye(pp) + (X.T * omega) @ X
            V_beta     = np.linalg.inv(V_beta_inv)
            m_beta     = V_beta @ (X.T @ (kappa - omega * u[groups]))
            beta       = np.random.multivariate_normal(m_beta, V_beta)

            # 3. Draw u_j | beta, omega, tau_u, y
            psi_beta = X @ beta
            for j in range(J):
                idx_j = groups == j
                v_j   = 1. / (np.sum(omega[idx_j]) + tau_u)
                m_j   = v_j * np.sum(kappa[idx_j] - omega[idx_j] * psi_beta[idx_j])
                u[j]  = np.random.normal(m_j, np.sqrt(v_j))

            # 4. Draw tau_u | u
            a_u_ = alpha_u + J / 2.
            b_u_ = gamma_u + 0.5 * np.sum(u**2)
            tau_u = np.random.gamma(a_u_, 1. / b_u_)

            if it >= n_burnin:
                chain_samps.append(np.concatenate([beta, u, [tau_u]]))

        all_samples.append(np.array(chain_samps))

    samples = np.vstack(all_samples)
    pnames  = ([f'beta{i}' for i in range(pp)]
               + [f'u{j}'  for j in range(J)]
               + ['tau_u'])
    return {'samples': samples, 'n_samples': len(samples),
            'param_names': pnames, 'n_per_chain': n_iter - n_burnin}

print('Running Polya-Gamma Gibbs (3 chains x 2000 iters, T=50)...')
t0 = time.perf_counter()
res_gibbs   = gibbs_hl_logistic(X, y, groups, J, n_groups)
t_gibbs     = time.perf_counter() - t0
samples     = res_gibbs['samples']
param_names = res_gibbs['param_names']
n_per_chain = res_gibbs['n_per_chain']
print(f'Done.  {res_gibbs["n_samples"]} post-burnin samples,  {t_gibbs:.1f} s')

df_gibbs = pl.DataFrame({nm: samples[:, i].tolist()
                          for i, nm in enumerate(param_names)})
df_gibbs.write_parquet(DATA / f'{CASE}_gibbs.parquet')
print(f'Saved: {CASE}_gibbs.parquet')"""))

cells.append(code(r"""# Trace plots for key scalar parameters
trace_params    = ['beta0', 'beta1', 'tau_u']
true_vals_trace = [beta_true[0], beta_true[1], tau_u_true]
chain_colors    = ['steelblue', 'darkorange', 'forestgreen']

for pname, tv in zip(trace_params, true_vals_trace):
    col_idx = param_names.index(pname)
    fig, ax = plt.subplots(figsize=(8, 3))
    for chain in range(3):
        start = chain * n_per_chain
        ax.plot(samples[start:start+500, col_idx],
                color=chain_colors[chain], lw=0.6, alpha=0.8, label=f'Chain {chain+1}')
    ax.axhline(tv, color='red', lw=1.2, ls='--', label='True')
    ax.set_xlabel('Post-burnin iter');  ax.set_ylabel(pname)
    ax.set_title(f'PG Gibbs trace: {pname}');  ax.legend(fontsize=8, ncol=4)
    plt.tight_layout()
    save_fig(fig, f'{CASE}_gibbs_trace_{pname}.png')
    plt.show()"""))

cells.append(code(r"""# ACF plots
def acf(x, max_lag=50):
    x  = x - x.mean()
    c0 = np.dot(x, x)
    return np.array([np.dot(x[:len(x)-k], x[k:]) / c0 for k in range(max_lag + 1)])

for pname in trace_params:
    col_idx = param_names.index(pname)
    chain1  = samples[:n_per_chain, col_idx]
    a_vals  = acf(chain1, 50)
    lags    = np.arange(len(a_vals))
    conf    = 1.96 / np.sqrt(len(chain1))
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.bar(lags, a_vals, color='steelblue', alpha=0.7, width=0.8)
    ax.axhline(0,     color='black', lw=0.8)
    ax.axhline(conf,  color='red', lw=1, ls='--')
    ax.axhline(-conf, color='red', lw=1, ls='--')
    ax.set_xlabel('Lag');  ax.set_ylabel('ACF')
    ax.set_title(f'PG Gibbs ACF (chain 1): {pname}')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.tight_layout()
    save_fig(fig, f'{CASE}_gibbs_acf_{pname}.png')
    plt.show()"""))

cells.append(code(r"""# Gelman-Rubin R-hat
def gelman_rubin(chains_list):
    m  = len(chains_list)
    n  = min(len(c) for c in chains_list)
    ch = np.array([c[:n] for c in chains_list])
    cm = ch.mean(axis=1);  gm = cm.mean()
    B  = n / (m - 1) * np.sum((cm - gm)**2)
    W  = np.mean([np.var(c, ddof=1) for c in chains_list])
    return np.sqrt(((n - 1) / n * W + B / n) / W)

rhat = {}
for pname in trace_params:
    col_idx = param_names.index(pname)
    chains  = [samples[ch * n_per_chain:(ch + 1) * n_per_chain, col_idx]
               for ch in range(3)]
    rhat[pname] = gelman_rubin(chains)

print('Gelman-Rubin R-hat:')
for k, v_rh in rhat.items():
    print(f'  {k}: {v_rh:.4f}  {"OK" if v_rh < 1.01 else "WARNING"}')

fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(list(rhat.keys()), list(rhat.values()), color='steelblue', alpha=0.8)
ax.axhline(1.01, color='red', lw=1.5, ls='--', label='R-hat = 1.01')
ax.set_ylabel('$\\hat{R}$');  ax.set_title('Gelman-Rubin convergence diagnostic')
ax.legend()
plt.tight_layout()
save_fig(fig, f'{CASE}_gibbs_rhat.png')
plt.show()

gibbs_means = {nm: samples[:, i].mean()      for i, nm in enumerate(param_names)}
gibbs_stds  = {nm: samples[:, i].std(ddof=1) for i, nm in enumerate(param_names)}
print('Gibbs reference posteriors:')
for k in trace_params:
    print(f'  {k}: mean={gibbs_means[k]:.4f},  sd={gibbs_stds[k]:.4f}')"""))

# ── Stage 5 ───────────────────────────────────────────────────────────────────
cells.append(md(r"""---
## Stage 5 — Diagnostics and Comparison

VB methods compared against the PG Gibbs reference:
- Posterior density overlays ($\beta_0$, $\beta_1$, $\tau_u$)
- SD ratios $\sigma_\text{VB}/\sigma_\text{Gibbs}$ (variance collapse)
- Mean errors $|\mu_\text{VB} - \mu_\text{Gibbs}|$
- Random effects recovery"""))

cells.append(code(r"""method_colors = {'CAVI': 'steelblue', 'Gradient Ascent': 'darkorange',
                 "Newton's Method": 'forestgreen', 'BFGS': 'purple'}

methods_vb = {
    'CAVI':            {'mu': res_cavi['mu_beta'], 'Sig': res_cavi['Sigma_beta'],
                        'a_u': res_cavi['a_u'],    'b_u': res_cavi['b_u'],
                        'm':   res_cavi['m'],       'v':   res_cavi['v']},
    'Gradient Ascent': {'mu': mu_ga, 'Sig': Sig_ga, 'a_u': au_ga, 'b_u': bu_ga,
                        'm': m_ga, 'v': v_ga},
    "Newton's Method": {'mu': mu_n,  'Sig': Sig_n,  'a_u': au_n,  'b_u': bu_n,
                        'm': m_n, 'v': v_n},
    'BFGS':            {'mu': mu_b,  'Sig': Sig_b,  'a_u': au_b,  'b_u': bu_b,
                        'm': m_b, 'v': v_b},
}
scalar_params    = ['beta0', 'beta1', 'tau_u']
true_vals_scalar = [beta_true[0], beta_true[1], tau_u_true]

print('VB vs Gibbs posterior means:')
for pname in scalar_params:
    gm = gibbs_means[pname]
    for mname, mp in methods_vb.items():
        if pname == 'beta0':
            vm = mp['mu'][0]
        elif pname == 'beta1':
            vm = mp['mu'][1]
        else:
            vm = mp['a_u'] / mp['b_u']
        print(f'  {pname} {mname}: VB={vm:.4f},  Gibbs={gm:.4f}')"""))

cells.append(code(r"""# VB vs Gibbs posterior overlays
for col_idx, pname in enumerate(scalar_params):
    samps_col = samples[:, param_names.index(pname)]
    fig, ax   = plt.subplots(figsize=(6, 4))
    ax.hist(samps_col, bins=50, density=True,
            color='#E7298A', alpha=0.35, label='PG Gibbs', edgecolor='none')
    xlo = samps_col.min();  xhi = samps_col.max()
    xv  = np.linspace(xlo, xhi, 300)
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
    plt.show()"""))

cells.append(code(r"""# SD ratios (VB / Gibbs)
sd_ratios = {}
for mname, mp in methods_vb.items():
    row = {}
    for col_idx, pname in enumerate(scalar_params):
        if col_idx < p:
            vb_sd = np.sqrt(mp['Sig'][col_idx, col_idx])
        else:
            vb_sd = np.sqrt(mp['a_u']) / mp['b_u']
        row[pname] = vb_sd / gibbs_stds[pname]
    sd_ratios[mname] = row

print('SD ratios (VB / Gibbs):')
for mname, row in sd_ratios.items():
    print(f'  {mname}: ' + '  '.join(f'{k}={v:.3f}' for k, v in row.items()))

x_pos = np.arange(len(scalar_params));  width = 0.2
fig, ax = plt.subplots(figsize=(9, 4))
for i, (mname, row) in enumerate(sd_ratios.items()):
    vals = [row[pn] for pn in scalar_params]
    ax.bar(x_pos + i * width, vals, width, label=mname,
           color=list(method_colors.values())[i], alpha=0.85)
ax.axhline(1.0, color='black', lw=1.2, ls='--', label='No collapse')
ax.set_xticks(x_pos + 1.5 * width)
ax.set_xticklabels(scalar_params)
ax.set_ylabel('$\\sigma_\\mathrm{VB}/\\sigma_\\mathrm{Gibbs}$')
ax.set_title('Posterior SD ratios: hierarchical logistic')
ax.legend(fontsize=9)
plt.tight_layout()
save_fig(fig, f'{CASE}_sd_ratios.png')
plt.show()"""))

cells.append(code(r"""# Mean errors
mean_errors = {}
for mname, mp in methods_vb.items():
    row = {}
    for col_idx, pname in enumerate(scalar_params):
        if col_idx < p:
            vb_mean = mp['mu'][col_idx]
        else:
            vb_mean = mp['a_u'] / mp['b_u']
        row[pname] = abs(vb_mean - gibbs_means[pname])
    mean_errors[mname] = row

fig, ax = plt.subplots(figsize=(9, 4))
for i, (mname, row) in enumerate(mean_errors.items()):
    vals = [row[pn] for pn in scalar_params]
    ax.bar(x_pos + i * width, vals, width, label=mname,
           color=list(method_colors.values())[i], alpha=0.85)
ax.set_xticks(x_pos + 1.5 * width)
ax.set_xticklabels(scalar_params)
ax.set_ylabel('$|\\mu_\\mathrm{VB} - \\mu_\\mathrm{Gibbs}|$')
ax.set_title('Posterior mean errors: hierarchical logistic')
ax.legend(fontsize=9)
plt.tight_layout()
save_fig(fig, f'{CASE}_mean_errors.png')
plt.show()"""))

cells.append(code(r"""# Random effects recovery
u_gibbs_means = np.array([gibbs_means[f'u{j}'] for j in range(J)])
u_gibbs_stds  = np.array([gibbs_stds[f'u{j}']  for j in range(J)])
j_labels = [f'Group {j+1}' for j in range(J)]
x_j = np.arange(J)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
mp_cavi = methods_vb['CAVI']
axes[0].bar(x_j, mp_cavi['m'], color='steelblue', alpha=0.7, label='CAVI mean')
axes[0].scatter(x_j, u_true, color='red', zorder=5, s=60, marker='*', label='True $u_j$')
axes[0].errorbar(x_j, mp_cavi['m'], yerr=2 * np.sqrt(mp_cavi['v']),
                 fmt='none', color='steelblue', capsize=4, lw=1.2, label='CAVI $\\pm 2$SD')
axes[0].set_xticks(x_j);  axes[0].set_xticklabels(j_labels, rotation=30, ha='right')
axes[0].set_ylabel('$u_j$');  axes[0].set_title('Random effects: CAVI')
axes[0].legend(fontsize=8)

axes[1].bar(x_j, u_gibbs_means, color='#E7298A', alpha=0.6, label='PG Gibbs mean')
axes[1].scatter(x_j, u_true, color='red', zorder=5, s=60, marker='*', label='True $u_j$')
axes[1].errorbar(x_j, u_gibbs_means, yerr=2 * u_gibbs_stds,
                 fmt='none', color='#E7298A', capsize=4, lw=1.2, label='Gibbs $\\pm 2$SD')
axes[1].set_xticks(x_j);  axes[1].set_xticklabels(j_labels, rotation=30, ha='right')
axes[1].set_ylabel('$u_j$');  axes[1].set_title('Random effects: PG Gibbs')
axes[1].legend(fontsize=8)
plt.tight_layout()
save_fig(fig, f'{CASE}_random_effects.png')
plt.show()"""))

cells.append(code(r"""# Timing comparison
runtimes_all = {
    'CAVI':             t_cavi * 1000,
    'Gradient Ascent':  res_ga['runtime'] * 1000,
    "Newton's Method":  res_newton['runtime'] * 1000,
    'BFGS':             t_bfgs * 1000,
    'Gibbs (PG)':       t_gibbs * 1000,
}
t_gibbs_ms    = runtimes_all['Gibbs (PG)']
method_keys_t = list(runtimes_all.keys())
tlabels       = ['CAVI', 'Gradient\nAscent', "Newton's\nMethod", 'BFGS', 'Gibbs\n(PG)']
tcolors       = ['steelblue', 'darkorange', 'forestgreen', 'purple', '#E7298A']

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(tlabels, [runtimes_all[k] for k in method_keys_t],
              color=tcolors, alpha=0.85, edgecolor='white')
for bar, key in zip(bars, method_keys_t):
    t = runtimes_all[key]
    if key != 'Gibbs (PG)':
        speedup = t_gibbs_ms / t
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.15,
                f'{speedup:.0f}x faster', ha='center', va='bottom',
                fontsize=9, fontweight='bold', color='black')
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2,
            f'{t:.0f} ms', ha='center', va='center',
            fontsize=8, color='white', fontweight='bold')
ax.set_yscale('log');  ax.set_ylabel('Runtime (ms, log scale)')
ax.set_title('Runtime comparison: hierarchical logistic')
ax.axhline(t_gibbs_ms, color='#E7298A', lw=1.2, ls='--', alpha=0.5, label='PG Gibbs runtime')
ax.legend(fontsize=9)
plt.tight_layout()
save_fig(fig, f'{CASE}_timing_comparison.png')
plt.show()"""))

cells.append(code(r"""# Write result tables
def write_tblr(rows, header, path):
    ncols   = len(header)
    colspec = 'l' + 'r' * (ncols - 1)
    lines   = [f'\\begin{{tblr}}{{colspec={{{colspec}}}, hline{{1,2,Z}}={{solid}}}}']
    lines.append('  ' + ' & '.join(header) + ' \\\\')
    for row in rows:
        lines.append('  ' + ' & '.join(str(v) for v in row) + ' \\\\')
    lines.append('\\end{tblr}')
    with open(path, 'w') as fh:
        fh.write('\n'.join(lines) + '\n')
    print(f'Saved: {path.name}')

ef_cavi   = float(res_cavi['elbo_history'][-1])
ef_ga     = float(res_ga['elbo_history'][-1])
ef_newton = float(res_newton['elbo_history'][-1])
ef_bfgs   = float(res_bfgs['elbo_history'][-1])
nm_key    = "Newton's Method"

# Performance table
perf_h = ['Method', 'Iterations', 'Runtime (ms)', 'Speedup vs Gibbs', 'Final ELBO']
perf_r = [
    ['CAVI',            str(res_cavi['iterations']),   f'{runtimes_all["CAVI"]:.1f}',
     f'{t_gibbs_ms/runtimes_all["CAVI"]:.0f}x',   f'{ef_cavi:.3f}'],
    ['Gradient Ascent', str(res_ga['iterations']),     f'{runtimes_all["Gradient Ascent"]:.1f}',
     f'{t_gibbs_ms/runtimes_all["Gradient Ascent"]:.0f}x', f'{ef_ga:.3f}'],
    [nm_key,            str(res_newton['iterations']), f'{runtimes_all[nm_key]:.1f}',
     f'{t_gibbs_ms/runtimes_all[nm_key]:.1f}x',    f'{ef_newton:.3f}'],
    ['BFGS',            str(res_bfgs['iterations']),   f'{runtimes_all["BFGS"]:.1f}',
     f'{t_gibbs_ms/runtimes_all["BFGS"]:.0f}x',    f'{ef_bfgs:.3f}'],
    ['PG Gibbs (3 chains)', '3x2000', f'{t_gibbs_ms:.1f}', '1x (reference)', 'N/A'],
]
write_tblr(perf_r, perf_h, TABLES / f'{CASE}_performance.tex')

# Posterior summary table
post_h = ['Method', '$\\mu_{\\beta_0}$', '$\\mu_{\\beta_1}$',
          '$\\mathrm{E}[\\tau_u]$',
          'SD ratio $\\beta_0$', 'SD ratio $\\beta_1$']
post_r = []
for mname, mp in methods_vb.items():
    post_r.append([mname,
                   f'{mp["mu"][0]:.4f}', f'{mp["mu"][1]:.4f}',
                   f'{mp["a_u"]/mp["b_u"]:.4f}',
                   f'{sd_ratios[mname]["beta0"]:.3f}',
                   f'{sd_ratios[mname]["beta1"]:.3f}'])
post_r.append(['PG Gibbs (ref)',
               f'{gibbs_means["beta0"]:.4f}', f'{gibbs_means["beta1"]:.4f}',
               f'{gibbs_means["tau_u"]:.4f}',
               '1.000', '1.000'])
write_tblr(post_r, post_h, TABLES / f'{CASE}_posterior_summary.tex')

print('\nAll outputs complete.')
print('\nFigures saved:')
for f in sorted(FIGS.glob(f'{CASE}_*.png')):
    print(f'  {f.name}')
print('\nTables saved:')
for f in sorted(TABLES.glob(f'{CASE}_*.tex')):
    print(f'  {f.name}')"""))

# ── Finalise notebook ─────────────────────────────────────────────────────────
nb = {
    'nbformat': 4,
    'nbformat_minor': 5,
    'metadata': {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'name': 'python',
            'version': '3.10.0'
        }
    },
    'cells': cells
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT, 'w', encoding='utf-8') as fh:
    json.dump(nb, fh, indent=1, ensure_ascii=False)

print(f'Created: {OUTPUT}')
print(f'Total cells: {len(cells)}')
