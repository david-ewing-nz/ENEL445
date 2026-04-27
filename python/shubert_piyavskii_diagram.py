import numpy as np
import matplotlib.pyplot as plt

# ── true function ─────────────────────────────────────────────────────────────
def f(x):
    return np.sin(x) + 0.5*np.sin(2.5*x) + 0.3*np.cos(1.5*x)

L = 3.0   # Lipschitz constant — must satisfy L >= |f'(x)| for all x

x = np.linspace(0, 10, 2000)
fx = f(x)

# ── evaluated points (simulating 4 iterations) ───────────────────────────────
eval_x = np.array([0.5, 3.0, 5.5, 8.5])
eval_f = f(eval_x)

# ── build sawtooth envelope: max over all cones at each x ────────────────────
# each cone: g_i(x) = f(x_i) - L*|x - x_i|
cones    = np.array([fi - L * np.abs(x - xi) for xi, fi in zip(eval_x, eval_f)])
envelope = np.max(cones, axis=0)

# ── next sample = argmin of envelope ─────────────────────────────────────────
next_idx = np.argmin(envelope)
next_x   = x[next_idx]
next_env = envelope[next_idx]

# ── figure ────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
plt.subplots_adjust(wspace=0.08)

cone_colours = ['#a8d8ea', '#a8e6a8', '#f9d89c', '#f4a6a0']

for ax_idx, ax in enumerate(axes):
    # true function
    ax.plot(x, fx, 'k--', lw=1.5, label='$f(x)$ (true, unknown)', zorder=3)

    # individual cones (left panel only — for clarity)
    if ax_idx == 0:
        for i, (xi, fi, col) in enumerate(zip(eval_x, eval_f, cone_colours)):
            cone_i = fi - L * np.abs(x - xi)
            ax.fill_between(x, cone_i, -4, alpha=0.25, color=col)
            ax.plot(x, cone_i, lw=0.8, color=col, alpha=0.6)
        ax.set_title('Lipschitz Cones + Envelope', fontsize=12, fontweight='bold')
    else:
        ax.set_title('Next Sample Selection', fontsize=12, fontweight='bold')

    # envelope
    ax.plot(x, envelope, color='royalblue', lw=2.2, label='Envelope $\\max_i g_i(x)$', zorder=4)

    # evaluated points
    ax.scatter(eval_x, eval_f, color='black', s=60, zorder=6)
    for i, (xi, fi) in enumerate(zip(eval_x, eval_f)):
        ax.annotate(f'$x_{i+1}$', (xi, fi), xytext=(4, 6),
                    textcoords='offset points', fontsize=10, fontweight='bold')

    # next sample point
    ax.plot(next_x, next_env, '*', color='red', ms=16, zorder=7,
            label=f'Next sample $x^*={next_x:.2f}$')
    ax.annotate(f'$x^*$\n(next sample)', (next_x, next_env),
                xytext=(12, -30), textcoords='offset points',
                fontsize=9, color='red', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

    ax.set_xlim(0, 10)
    ax.set_ylim(-3.5, 2.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=8.5, loc='upper right')

# ── annotation boxes ─────────────────────────────────────────────────────────
# left panel: cone formula
axes[0].text(0.02, 0.03,
    r"Cone at $x_i$: $g_i(x) = f(x_i) - L\,|x - x_i|$" + "\n"
    r"Envelope: $\hat{g}(x) = \max_i\, g_i(x)$" + "\n"
    r"Lipschitz: $|f(x)-f(y)| \leq L|x-y|$",
    transform=axes[0].transAxes, fontsize=8.5, va='bottom', ha='left',
    bbox=dict(facecolor='lightyellow', edgecolor='grey', alpha=0.9, pad=4),
    linespacing=1.6, zorder=8)

# right panel: algorithm + stop — left side
axes[1].text(0.02, 0.98,
    "Algorithm:\n"
    r"1. Evaluate $f$ at initial points" + "\n"
    r"2. Build $\hat{g}(x) = \max_i\{f(x_i) - L|x-x_i|\}$" + "\n"
    r"3. Sample $x^* = \arg\min_x\,\hat{g}(x)$" + "\n"
    r"4. Add $(x^*, f(x^*))$ and repeat" + "\n"
    r"Stop: $f_{\rm best} - \min\hat{g} < \varepsilon$",
    transform=axes[1].transAxes, fontsize=8.5, va='top', ha='left',
    bbox=dict(facecolor='lightcyan', edgecolor='grey', alpha=0.9, pad=4),
    linespacing=1.6, zorder=8)

# right panel: DIRECT note — left side below algorithm box
axes[1].text(0.02, 0.52,
    "DIRECT addresses both weaknesses:\n"
    r"$\bullet$ Estimates $L$ locally per hyper-rectangle" + "\n"
    r"  (no global $K$ needed)" + "\n"
    r"$\bullet$ Generalises to $n$-D by partitioning" + "\n"
    r"  $n$-dimensional hyper-rectangles",
    transform=axes[1].transAxes, fontsize=8.5, va='top', ha='left',
    bbox=dict(facecolor='#f0e6ff', edgecolor='grey', alpha=0.9, pad=4),
    linespacing=1.6, zorder=8)

plt.suptitle('Shubert–Piyavskii Algorithm (Lipschitz Global Optimisation)',
             fontsize=13, fontweight='bold')

out = r'D:\github\ENEL445\figs\shubert_piyavskii_diagram.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
print('saved to', out)
plt.show()
