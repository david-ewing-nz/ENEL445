import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

rng = np.random.default_rng(42)

fig, axes = plt.subplots(1, 3, figsize=(13, 5))
plt.subplots_adjust(wspace=0.1, top=0.97)

# colour map for individuals
ind_colours = ['#4e79a7','#f28e2b','#e15759','#76b7b2','#59a14f','#edc948']

# ── helper: draw a chromosome bar ─────────────────────────────────────────────
def draw_chromosome(ax, y, genes, colours, label=None, alpha=1.0):
    n = len(genes)
    for j, (g, c) in enumerate(zip(genes, colours)):
        ax.barh(y, 1, left=j, height=0.6, color=c, alpha=alpha,
                edgecolor='white', linewidth=1.5)
        ax.text(j + 0.5, y, str(g), ha='center', va='center',
                fontsize=8, fontweight='bold', color='white')
    if label:
        ax.text(-0.3, y, label, ha='right', va='center', fontsize=9)

# gene pool colours (fixed per locus)
locus_col = ['#4e79a7','#f28e2b','#e15759','#76b7b2','#59a14f','#edc948']

# ── left panel: Selection ─────────────────────────────────────────────────────
ax = axes[0]
pop = [[3,7,1,4,6,2],
       [5,2,8,3,1,7],
       [1,9,4,6,2,5],
       [7,3,6,1,8,4],
       [2,6,3,8,5,1]]
fitness = [0.9, 0.3, 0.7, 0.5, 0.2]   # higher = better

for i, (ind, fit) in enumerate(zip(pop, fitness)):
    y = 4 - i
    alpha = 0.4 + 0.6*fit
    draw_chromosome(ax, y, ind, locus_col, label=f'$x_{i+1}$', alpha=alpha)
    # fitness bar on right
    ax.barh(y, fit*1.5, left=6.3, height=0.5, color='steelblue', alpha=0.7)
    ax.text(6.3 + fit*1.5 + 0.05, y, f'{fit:.1f}', va='center', fontsize=8)

# circle selected (top 2)
for y in [4, 2]:
    circ = mpatches.FancyBboxPatch((-0.05, y-0.35), 6.1, 0.7,
                                    boxstyle='round,pad=0.05',
                                    linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(circ)

ax.text(6.5, 4.7, 'fitness', fontsize=8, color='steelblue', ha='center')
ax.set_xlim(-1.5, 8.5); ax.set_ylim(0.2, 5.3)
ax.axis('off')
ax.set_title('1. Selection\n(fitness-proportionate)', fontsize=11, fontweight='bold')
ax.text(0.5, 0.02, 'Higher fitness → more likely selected\n(roulette wheel / tournament)',
        transform=ax.transAxes, fontsize=8.5, ha='center', va='bottom',
        bbox=dict(facecolor='lightyellow', edgecolor='grey', pad=3, alpha=0.9))

# ── middle panel: Crossover ───────────────────────────────────────────────────
ax = axes[1]
parent1 = [3,7,1,4,6,2]
parent2 = [1,9,4,6,2,5]
xpt = 3   # crossover point

child1 = parent1[:xpt] + parent2[xpt:]
child2 = parent2[:xpt] + parent1[xpt:]

col1 = ['#4e79a7']*xpt + ['#e15759']*(6-xpt)
col2 = ['#e15759']*xpt + ['#4e79a7']*(6-xpt)

draw_chromosome(ax, 4.2, parent1, locus_col,          label='$p_1$')
draw_chromosome(ax, 3.2, parent2, locus_col,          label='$p_2$')
draw_chromosome(ax, 1.8, child1,  col1,               label='$c_1$')
draw_chromosome(ax, 0.8, child2,  col2,               label='$c_2$')

# crossover point line
ax.axvline(xpt, ymin=0.05, ymax=0.95, color='black', lw=2, ls='--', zorder=5)
ax.text(xpt, 2.5, ' cut', fontsize=9, color='black', va='center')

# arrows
ax.annotate('', xy=(3, 2.15), xytext=(3, 3.0),
            arrowprops=dict(arrowstyle='->', color='grey', lw=1.5))

ax.set_xlim(-1.5, 6.5); ax.set_ylim(0.1, 5.0)
ax.axis('off')
ax.set_title('2. Crossover\n(single-point)', fontsize=11, fontweight='bold')
ax.text(0.5, 0.02, 'Swap genetic material at cut point\n(also: uniform, two-point crossover)',
        transform=ax.transAxes, fontsize=8.5, ha='center', va='bottom',
        bbox=dict(facecolor='lightcyan', edgecolor='grey', pad=3, alpha=0.9))

# ── right panel: Mutation ─────────────────────────────────────────────────────
ax = axes[2]
before = [3,7,1,4,6,2]
after  = [3,7,1,9,6,2]   # locus 3 mutated

draw_chromosome(ax, 3.5, before, locus_col, label='before')
draw_chromosome(ax, 1.5, after,
                [locus_col[j] if j != 3 else '#ff0000' for j in range(6)],
                label='after')

ax.annotate('', xy=(3.5, 1.85), xytext=(3.5, 3.15),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax.text(3.7, 2.5, 'mutate\nlocus 3', fontsize=8.5, color='red', va='center')

ax.set_xlim(-1.5, 6.5); ax.set_ylim(0.3, 4.8)
ax.axis('off')
ax.set_title('3. Mutation\n(random gene flip)', fontsize=11, fontweight='bold')
ax.text(0.5, 0.02,
        'Random allele change with prob $p_m \ll 1$\nMaintains diversity, prevents premature convergence',
        transform=ax.transAxes, fontsize=8.5, ha='center', va='bottom',
        bbox=dict(facecolor='#f0e6ff', edgecolor='grey', pad=3, alpha=0.9))

# ── advantages / disadvantages ────────────────────────────────────────────────
fig.text(0.02, -0.01,
    r'$\bf{Advantages:}$' +
    '  global search (avoids local minima);  no gradient needed;  handles discrete/mixed variables',
    fontsize=8.5, ha='left')
fig.text(0.02, -0.07,
    r'$\bf{Disadvantages:}$' +
    '  many function evaluations;  no convergence guarantee;  tuning required ($p_c$, $p_m$, pop size)',
    fontsize=8.5, ha='left')

out = r'D:\github\ENEL445\figs\genetic_algorithm_diagram.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
print('saved to', out)
plt.show()
