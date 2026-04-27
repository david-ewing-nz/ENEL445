import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── function ──────────────────────────────────────────────────────────────────
def f(x):
    return np.sin(7*x) + 0.5*np.cos(4*x) + 0.3*x

x_dense = np.linspace(0, 1, 1000)

# ── simulated DIRECT intervals after 3 trisection levels ─────────────────────
# level 0 → trisect [0,1]
# level 1 → trisect [0, 1/3]  (best)
# level 2 → trisect [0, 1/9]  (best)
intervals = [
    (1/3,  2/3  ),   # d = 1/6
    (2/3,  1.00 ),   # d = 1/6
    (1/9,  2/9  ),   # d = 1/18
    (2/9,  1/3  ),   # d = 1/18
    (1/27, 2/27 ),   # d = 1/54
    (2/27, 3/27 ),   # d = 1/54
    (0.00, 1/27 ),   # d = 1/54
    (1/81, 2/81 ),   # d = 1/162
    (2/81, 3/81 ),   # d = 1/162
    (0.00, 1/81 ),   # d = 1/162
]

centres = np.array([(l+r)/2 for l, r in intervals])
d_vals  = np.array([(r-l)/2 for l, r in intervals])
fvals   = f(centres)
f_min   = fvals.min()

eps       = 1.5
threshold = f_min + eps * abs(f_min)

# ── lower convex hull indices ─────────────────────────────────────────────────
def lower_hull_idx(xs, ys):
    order = sorted(range(len(xs)), key=lambda i: (xs[i], ys[i]))
    hull  = []
    for i in order:
        while len(hull) >= 2:
            a, b = hull[-2], hull[-1]
            cross = (xs[b]-xs[a])*(ys[i]-ys[a]) - (ys[b]-ys[a])*(xs[i]-xs[a])
            if cross >= 0:
                hull.pop()
            else:
                break
        hull.append(i)
    return hull

hull_set = set(lower_hull_idx(d_vals, fvals))
selected = [i for i in hull_set if fvals[i] <= threshold]

# ── figure ────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
plt.subplots_adjust(wspace=0.08)

def pt_colour(i):
    if i in selected:   return 'red'
    if i in hull_set:   return 'darkorange'
    return 'lightgrey'

# ── left: function + shaded rectangles ───────────────────────────────────────
ax = axes[0]
ax.plot(x_dense, f(x_dense), 'k-', lw=1.8, zorder=5, label='$f(x)$')

for i, (l, r) in enumerate(intervals):
    col = pt_colour(i)
    ax.axvspan(l, r, alpha=0.3, color=col, zorder=1)
    ax.plot(centres[i], fvals[i], 'o', color=col, ms=7,
            markeredgecolor='dimgrey', zorder=6)

legend_items = [
    mpatches.Patch(color='red',        alpha=0.5, label='Selected for subdivision'),
    mpatches.Patch(color='darkorange', alpha=0.5, label='On hull, filtered by $\\varepsilon$'),
    mpatches.Patch(color='lightgrey',  alpha=0.5, label='Not potentially optimal'),
]
ax.legend(handles=legend_items, fontsize=8.5, loc='upper right')
ax.set_xlim(0, 1); ax.set_xticks([]); ax.set_yticks([])
ax.grid(True, alpha=0.2)
ax.set_title('DIRECT: Rectangles on $f(x)$', fontsize=12, fontweight='bold')

# ── right: f–d scatter ────────────────────────────────────────────────────────
ax = axes[1]

# all points
for i in range(len(intervals)):
    col = pt_colour(i)
    ms  = 12 if i in hull_set else 8
    ax.plot(d_vals[i], fvals[i], 'o', color=col, ms=ms, zorder=5,
            markeredgecolor='dimgrey')

# circle selected points
for i in selected:
    ax.plot(d_vals[i], fvals[i], 'o', ms=20, mfc='none',
            mec='red', mew=2.5, zorder=7)

# convex hull line
hull_sorted = sorted(hull_set, key=lambda i: d_vals[i])
ax.plot([d_vals[i] for i in hull_sorted],
        [fvals[i]  for i in hull_sorted],
        'k--', lw=1.5, zorder=4, label='Lower-right convex hull')

# ε|f_min| threshold
ax.axhline(threshold, color='purple', lw=1.5, ls=':', zorder=3,
           label=r'$f_{\min}+\varepsilon|f_{\min}|$')
ax.axhline(f_min, color='green', lw=1.0, ls='--', alpha=0.6, zorder=3,
           label='$f_{\\min}$')

# bracket for ε|f_min|
x_brk = d_vals.max() * 1.12
ax.annotate('', xy=(x_brk, f_min), xytext=(x_brk, threshold),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=1.5))
ax.text(x_brk * 1.03, (f_min + threshold)/2,
        r'$\varepsilon|f_{\min}|$', color='purple', fontsize=9, va='center')

# annotation box
ax.text(0.98, 0.98,
    "Select $i$ if:\n"
    r"$(d_i, f(c_i))$ on lower-right convex hull" + "\n"
    r"and $f(c_i) \leq f_{\min} + \varepsilon|f_{\min}|$" + "\n\n"
    r"Formally $\exists\, K>0$:" + "\n"
    r"$f(c_i) - Kd_i \leq f_{\min} - \varepsilon|f_{\min}|$",
    transform=ax.transAxes, fontsize=9, va='top', ha='right',
    bbox=dict(facecolor='lightyellow', edgecolor='grey', alpha=0.9, pad=4),
    linespacing=1.6, zorder=8)

ax.set_xlabel('$d_i$  (rectangle half-size)', fontsize=10)
ax.set_ylabel('$f(c_i)$', fontsize=10)
ax.legend(fontsize=8.5, loc='lower left')
ax.grid(True, alpha=0.2)
ax.set_title('$f$-$d$ Scatter: Convex Hull Selection', fontsize=12, fontweight='bold')

plt.suptitle('DIRECT Algorithm: Potentially Optimal Rectangle Selection',
             fontsize=13, fontweight='bold')

out = r'D:\github\ENEL445\figs\direct_diagram.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
print('saved to', out)
plt.show()
