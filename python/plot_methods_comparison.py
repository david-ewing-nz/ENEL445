import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 6))

# contours of f = x1^2 + 5*x2^2
x1 = np.linspace(-0.5, 3.5, 400)
x2 = np.linspace(-1.5, 1.5, 400)
X1g, X2g = np.meshgrid(x1, x2)
F = X1g**2 + 5*X2g**2
ax.contour(X1g, X2g, F, levels=[0.5, 1, 2, 4, 8, 12, 16, 20, 25],
           colors='lightgrey', linewidths=0.8)

# key points
X0      = np.array([3.0,   1.0   ])
X1_sd   = np.array([2.239, -0.269])   # SD = CG iter 1 = BFGS iter 1
X1_newt = np.array([0.0,   0.0   ])   # Newton (exact minimum, 1 step)

# arrows from X0 to X1
for pt, col in [(X1_sd, '#1f77b4'), (X1_newt, '#d62728')]:
    ax.annotate('', xy=pt, xytext=X0,
                arrowprops=dict(arrowstyle='->', color=col, lw=1.8))

# scatter points
ax.scatter(*X0,     s=80, color='black',    zorder=5)
ax.scatter(*X1_sd,  s=80, color='#1f77b4',  zorder=5)
ax.scatter(*X1_newt, s=120, color='#d62728', marker='*', zorder=6)

# labels
ax.annotate(r'$X_0 = (3, 1)$',              xy=X0,      xytext=(3.05, 1.10),  fontsize=9)
ax.annotate('$X_1$ SD / CG / BFGS\n(2.239, -0.269)', xy=X1_sd,
            xytext=(2.3, -0.55), fontsize=9, color='#1f77b4')
ax.annotate('$X_1$ Newton\n(0, 0) exact min', xy=X1_newt,
            xytext=(0.1, 0.15), fontsize=9, color='#d62728')

ax.axhline(0, color='k', lw=0.4)
ax.axvline(0, color='k', lw=0.4)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('$f(X) = x_1^2 + 5x_2^2$ — one iteration from $X_0 = (3, 1)^T$')

plt.tight_layout()
plt.savefig('d:/github/ENEL445/figs/gradient_methods_comparison.png', dpi=150)
print("saved to figs/gradient_methods_comparison.png")
