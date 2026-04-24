import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 6))

xb   = np.array([2.0, 2.5])
xs   = np.array([3.2, 1.2])
xw   = np.array([0.8, 0.8])
xbar = (xb + xs) / 2

# base simplex — grey dashed
tri = plt.Polygon([xb, xs, xw], fill=False, edgecolor='grey', lw=1.5, ls='--')
ax.add_patch(tri)

# common vertices
for pt, lbl, off in [
    (xb,   '$x_b$',       ( 6,  4)),
    (xs,   '$x_s$',       ( 6,  4)),
    (xw,   '$x_w$',       (-18, 4)),
    (xbar, r'$\bar{x}$',  ( 6,  4)),
]:
    ax.plot(*pt, 'ko', ms=7, zorder=4)
    ax.annotate(lbl, pt, xytext=off, textcoords='offset points', fontsize=12)

# operations: (point, colour, point label, formula, formula xy)
bbox_style = dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2)
ops = [
    (xbar + 1.0*(xbar - xw), 'royalblue', '$x_r$',
     r'$x_r = \bar{x} + (\bar{x} - x_w)$',            (4.4, 3.55)),
    (xbar + 2.0*(xbar - xw), 'green',     '$x_e$',
     r'$x_e = \bar{x} + 2(\bar{x} - x_w)$',            (2.2, 4.8)),
    (xbar + 0.5*(xw - xbar), 'darkorange','$x_c$',
     r'$x_c = \bar{x} + \frac{1}{2}(x_w - \bar{x})$',  (1.6, 0.4)),
]

for pt, col, lbl, formula, fxy in ops:
    ax.plot(*pt, 'o', color=col, ms=10, zorder=5)
    ax.annotate(lbl, pt, xytext=(6, 4), textcoords='offset points',
                fontsize=12, color=col, fontweight='bold')
    ax.annotate('', xy=pt, xytext=xbar,
                arrowprops=dict(arrowstyle='->', color=col, lw=1.8))
    ax.text(*fxy, formula, fontsize=9, color=col, ha='center', va='center',
            bbox=bbox_style, zorder=6)

# shrink — arrows from xs/xw toward xb
for pt, lbl in [(xs, "$x_s'$"), (xw, "$x_w'$")]:
    shrunk = xb + 0.5 * (pt - xb)
    ax.plot(*shrunk, 's', color='red', ms=9, zorder=5)
    ax.annotate(lbl, shrunk, xytext=(6, 4), textcoords='offset points',
                fontsize=12, color='red', fontweight='bold')
    ax.annotate('', xy=shrunk, xytext=pt,
                arrowprops=dict(arrowstyle='->', color='red', lw=1.8))
ax.text(0.4, -0.2, r"$x_i' = x_b + \frac{1}{2}(x_i - x_b)$",
        fontsize=9, color='red', ha='center', va='center', bbox=bbox_style, zorder=6)

# legend
from matplotlib.lines import Line2D
legend_items = [
    Line2D([0],[0], marker='o', color='royalblue',  lw=1.8, label='Reflection $x_r$'),
    Line2D([0],[0], marker='o', color='green',      lw=1.8, label='Expansion $x_e$'),
    Line2D([0],[0], marker='o', color='darkorange',  lw=1.8, label='Contraction $x_c$'),
    Line2D([0],[0], marker='s', color='red',        lw=1.8, label="Shrink $x_s', x_w'$"),
]
ax.legend(handles=legend_items, loc='lower right', fontsize=10)

# gradient-free use cases — upper right
gf_text = (
    "Use gradient-free when:\n"
    "Non-differentiable: gradient does not exist\n"
    "Black-box $f$: no closed-form expression\n"
    "Noisy $f$: gradient estimate corrupted by noise"
)
ax.text(0.02, 0.98, gf_text, transform=ax.transAxes,
        fontsize=8.5, va='top', ha='left',
        bbox=dict(facecolor='lightcyan', edgecolor='grey', alpha=0.9, pad=4),
        zorder=7, linespacing=1.6)

# stopping criteria — mid right
stop_text = (
    "Stop when:\n"
    r"Simplex size: $\max_i \|x_i - x_1\|_2 < \varepsilon$" + "\n"
    r"Fn. value spread: $\max_i |f(x_i) - f(x_1)| < \varepsilon$" + "\n"
    r"Iteration limit: $k > k_{\max}$ or $N_{\rm eval} > N_{\max}$"
)
ax.text(0.98, 0.98, stop_text, transform=ax.transAxes,
        fontsize=8.5, va='top', ha='right',
        bbox=dict(facecolor='lightyellow', edgecolor='grey', alpha=0.9, pad=4),
        zorder=7, linespacing=1.6)

ax.set_title('Nelder-Mead Simplex Operations', fontsize=13, fontweight='bold')
ax.set_xlim(-1, 7)
ax.set_ylim(-0.5, 6)
ax.grid(True, alpha=0.3)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
out = r'D:\github\ENEL445\figs\nelder_mead_ops.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
print('saved to', out)
plt.show()
