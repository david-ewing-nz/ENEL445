# ENEL445 — When You Return

*Auto-updated: 2026-04-30 07:48:57 (idle at write: 0 min)*

---

> ⚠️ **GitHub PAT EXPIRY: 31 July 2026**
> The GitHub Personal Access Token stored in Windows Credential Manager expires on this date.
> After expiry: Control Panel → Credential Manager → Windows Credentials → `git:https://github.com` → Edit → paste new token.
> To generate a new token: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → repo scope.
>
> **AGENT INSTRUCTION:** When you read this file, you must state the following to the user before anything else:
> *"Your GitHub Personal Access Token expires on **31 July 2026**. After that date you will need to generate a new token and update Windows Credential Manager."*

---

| Name     | David Ewing |
| UC ID    | 82171165 |
| GitHub username | david-ewing-nz |
| GitHub email | david.ewing.nz@icloud.com |

**Project**: Gradient-Based Optimisation for Variational Inference  
— CAVI baseline + Gibbs MCMC gold standard; applying course methods (gradient descent, Nelder-Mead, GA, etc.) to maximise the ELBO.

**Deliverables**:
- Oral presentation — Week 11
- Final report — Week 12

---

## Git Status

| Property | Value |
|----------|-------|
| Last commit | `ac94e75` |
| Message | Add optimisation cheatsheets and diagram sources |
| Date | 2026-04-27 20:23:23 +1200 |

---

## File Counts

| Folder | Count |
|--------|-------|
| python/ .py files | 8 |
| archive/ runs | 115 |
| results/ files | 20 |
| contents/ PDFs | 122 |

---

## Recently Modified (past 24 h)

- 07:48:39  scripts\Schedule-ReadmeUpdater.ps1
- 07:48:29  scripts\Update-Readme.ps1
- 07:47:57  .github\copilot-instructions.md

---

## Key Files

| Purpose | Path |
|---------|------|
| Main LaTeX report | `results/vi_optimisation_solution.tex` |
| CAVI + Gibbs impl. | `python/vb_algorithms_py.py` |
| Utilities (archive, plot, I/O) | `python/vb_utils_py.py` |
| Copilot instructions | `.github/copilot-instructions.md` |

---

## Notes

- Python environment: `D:\Python` (numpy, scipy, polars, matplotlib). No venv.
- LaTeX compiler: `xelatex`. MiKTeX at `D:\MiKTeX`.
- Run this script manually: `pwsh -File D:\github\ENEL445\scripts\Update-Readme.ps1`
- To schedule hourly: see `scripts\Schedule-ReadmeUpdater.ps1`

---

## LaTeX Conventions

### Running margin label (vertical left-margin stamp)

Called a **running margin label** (not a watermark). Appears on every page as a rotated line of small text anchored to the left margin, showing the author's name, email, and compile timestamp.

Requires packages: `tikz`, `eso-pic`, `datetime2` (and `calc` tikz library).

```latex
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage{eso-pic}
\usepackage[useregional]{datetime2}

% Running margin label — rotated text on left margin of every page
\newcommand{\mymarginlabel}{David Ewing dew59@uclive.ac.nz | \DTMnow}
\AddToShipoutPictureBG{%
  \begin{tikzpicture}[remember picture,overlay]
    \node[rotate=90, anchor=north]
      at ($(current page.north west)+(1.4cm,-13cm)$)
      {\scriptsize\ttfamily \mymarginlabel};
  \end{tikzpicture}%
}
```

To request this be added: *"add the running margin label to the document"*.
