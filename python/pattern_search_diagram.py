import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
plt.subplots_adjust(wspace=0.05)

# ── left panel: minimal positive spanning set in R2 ──────────────────────────
ax = axes[0]

# minimal positive spanning set: n+1 = 3 vectors in R2
# every vector in R2 can be written as non-negative combination of these
dirs = np.array([
    [ 1.0,  0.0],   # d1
    [-0.5,  np.sqrt(3)/2],  # d2 — 120 deg
    [-0.5, -np.sqrt(3)/2],  # d3 — 240 deg
])
colours = ['royalblue', 'green', 'darkorange']
labels  = ['$d_1$', '$d_2$', '$d_3$']

for d, col, lbl in zip(dirs, colours, labels):
    ax.annotate('', xy=d, xytext=[0, 0],
                arrowprops=dict(arrowstyle='->', color=col, lw=2.5))
    ax.text(d[0]*1.15, d[1]*1.15, lbl, color=col, fontsize=13, fontweight='bold',
            ha='center', va='center')

ax.plot(0, 0, 'ko', ms=8, zorder=5)
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect('equal')
ax.axhline(0, color='grey', lw=0.5, ls='--', alpha=0.5)
ax.axvline(0, color='grey', lw=0.5, ls='--', alpha=0.5)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)

ax.text(0.5, 0.01,
        r"Minimal: $n+1 = 3$ vectors in $\mathbb{R}^2$" + "\n"
        r"Any $v \in \mathbb{R}^2$: $v = \sum_i \lambda_i d_i,\ \lambda_i \geq 0$",
        transform=ax.transAxes, fontsize=9, ha='center', va='bottom',
        bbox=dict(facecolor='lightyellow', edgecolor='grey', alpha=0.9, pad=4))

ax.set_title('Minimal Positive Spanning Set in $\\mathbb{R}^2$',
             fontsize=12, fontweight='bold')

# ── right panel: opportunistic polling ───────────────────────────────────────
ax = axes[1]

Xk = np.array([0.0, 0.0])
delta = 1.0  # mesh size

# poll directions (2n compass — typical GPS uses 2n or n+1)
poll_dirs = np.array([[1,0],[-1,0],[0,1],[0,-1]], dtype=float)
poll_pts  = Xk + delta * poll_dirs

# pretend f(Xk) = 5; poll points get f values assigned
f_vals = [3.2, 6.1, 5.8, 7.0]   # first point improves: f=3.2 < 5

ax.plot(*Xk, 'ko', ms=10, zorder=6)
ax.annotate('$X_k$\n$f=5$', Xk, xytext=(-0.25, -0.25),
            fontsize=10, ha='center', fontweight='bold')

# draw mesh faintly
for x in np.arange(-2, 2.5, 0.5):
    ax.axvline(x, color='lightgrey', lw=0.5)
for y in np.arange(-2, 2.5, 0.5):
    ax.axhline(y, color='lightgrey', lw=0.5)

eval_order = [0, 1, 2, 3]   # order of evaluation
for rank, i in enumerate(eval_order):
    pt  = poll_pts[i]
    fv  = f_vals[i]
    improving = fv < 5.0
    if improving:
        col  = 'green'
        ms   = 12
        mark = '*'
        note = f'$f={fv}$ ✓ accept\n(stop polling)'
    else:
        col  = 'lightgrey'
        ms   = 9
        mark = 'x'
        note = None

    # arrow from Xk
    ax.annotate('', xy=pt, xytext=Xk,
                arrowprops=dict(arrowstyle='->', color=col, lw=1.8,
                                linestyle='--' if not improving else '-'))
    ax.plot(*pt, marker=mark, color=col, ms=ms, zorder=5,
            markeredgecolor=col if improving else 'grey')
    ax.text(pt[0]+0.07, pt[1]+0.07, f'$f={fv}$', fontsize=8.5,
            color=col if improving else 'grey')

    if rank == 0:
        ax.annotate('1st eval', pt, xytext=(pt[0]+0.4, pt[1]-0.3),
                    fontsize=8, color='green',
                    arrowprops=dict(arrowstyle='->', color='green', lw=1))
    if improving:
        break   # opportunistic: stop at first improvement

# unevaluated directions — shown faded
for i in eval_order[rank+1:]:
    pt = poll_pts[i]
    ax.annotate('', xy=pt, xytext=Xk,
                arrowprops=dict(arrowstyle='->', color='lightgrey', lw=1.2, linestyle=':'))
    ax.plot(*pt, 'o', color='lightgrey', ms=8, zorder=4)
    ax.text(pt[0]+0.07, pt[1]+0.07, 'not\neval.', fontsize=7, color='lightgrey')

ax.text(0.02, 0.98,
        "Opportunistic polling:\nEvaluate poll points one at a time.\n"
        "Accept first $X$ with $f(X) < f(X_k)$\nand skip remaining directions.",
        transform=ax.transAxes, fontsize=8.5, va='top', ha='left',
        bbox=dict(facecolor='lightcyan', edgecolor='grey', alpha=0.9, pad=4),
        linespacing=1.6)

ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Opportunistic Polling (GPS)', fontsize=12, fontweight='bold')

plt.suptitle('Generalised Pattern Search', fontsize=13, fontweight='bold')
plt.subplots_adjust(wspace=0.05, bottom=0.22)

caption = (
    r"A minimal positive spanning set in $\mathbb{R}^2$ requires $n+1=3$ vectors. "
    r"Example: $\{e_1, e_2, -e_1-e_2\}$ where $e_1=(1,0)^\top$, $e_2=(0,1)^\top$. "
    "These span all of $\\mathbb{R}^2$ in the positive sense.\n"
    r"$\bf{Opportunistic\ polling:}$"
    " poll directions are evaluated one at a time in a preferred order. "
    r"As soon as one direction yields $f < f_{\rm current}$, the algorithm immediately "
    "accepts that point and starts a new iteration — it does "
    r"$\it{not}$"
    " evaluate all remaining directions in the pattern."
)
fig.text(0.5, 0.01, caption, ha='center', va='bottom', fontsize=8.5,
         wrap=True, linespacing=1.5,
         bbox=dict(facecolor='white', edgecolor='none', alpha=0.0))

out = r'D:\github\ENEL445\figs\pattern_search_diagram.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
print('saved to', out)
plt.show()
