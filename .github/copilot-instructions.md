# Copilot Instructions

## Machine Information

The user's primary machine is an **Alienware 17 R5** running Windows 11 Home.

| Property     | Value                              |
|--------------|------------------------------------|
| Manufacturer | Alienware                          |
| Model        | Alienware 17 R5                    |
| OS           | Windows 11 Home (Build 26200)      |
| Architecture | 64-bit                             |
| CPU          | Intel Core i7-8750H @ 2.20 GHz (6 cores, 12 logical) |
| RAM          | ~31.9 GB                           |
| GPU          | NVIDIA GeForce GTX 1060 (~4 GB VRAM) |
| GPU (iGPU)   | Intel UHD Graphics 630 (1 GB)      |
| Storage      | 256 GB NVMe SSD + 1 TB HDD         |

An **ASUS GX10** mini-PC has also been added to the user's setup as a separate machine.

## Student Information

| Property | Value |
|----------|-------|
| Name     | David Ewing |
| UC ID    | 82171165 |
| Course   | ENEL445 — Applied Engineering Optimisation |

## Python Environment

System Python at `D:\Python`. Packages in use: `numpy`, `scipy` (`stats`, `special.digamma`), `polars` (parquet I/O), `matplotlib`, `pathlib` (stdlib). No virtual environment.

## Language and Style

- All responses, reports, comments, and user-defined identifiers must use **British English** spelling.
  - Examples: optimisation, colour, behaviour, modelled, licence, analyse, centre, fibre
- **Exception**: external library API arguments and parameter names (numpy, scipy, matplotlib, polars, etc.) must keep their original American English spelling — do NOT change `color=`, `normalize=`, `gray`, `optimize`, etc.
- Preferred report format: IEEE two-column. LaTeX compiler: `xelatex`. MiKTeX at `D:\MiKTeX`.

## Live Project State

See [README-WHEN-YOU-RETURN.md](../README-WHEN-YOU-RETURN.md) for current git status, file counts, and recently modified files.

## VS Code Keybindings

The following user keybinding is stored at `D:\VSCode\data\user-data\User\keybindings.json` (user-scoped, not workspace). It is **not** reset by VS Code updates but may be lost on a new machine or a clean install.

```json
{
    "key": "ctrl+alt+b",
    "command": "latex-workshop.build",
    "when": "editorTextFocus && resourceExtname == '.tex'"
}
```

**To restore after a VS Code update or on a new machine:**
1. Open `D:\VSCode\data\user-data\User\keybindings.json` (or File → Preferences → Keyboard Shortcuts → open JSON)
2. Add the entry above if it is missing

The workspace also has `.vscode/tasks.json` defining a build task that calls `scripts/archive_tex.py` directly, as a fallback.

## File Execution Rules

### Python files in `python/`
- Always invoke via `python scripts/archive_py.py python/<script>.py` — never run directly.
- This applies only to files in `python/`. Scripts in `scripts/` are utility/logistics files and are exempt — run them directly.

### LaTeX files
- When a `.tex`, `.pdf`, or `.html` file is in context, compile the associated `.tex` source using `python scripts/archive_tex.py <path/to/file.tex>`.
- For `.pdf` or `.html` in context, identify the source `.tex` by reading its PDF metadata field `Subject` (set at compile time to the source filename). Look for the `.tex` in `report/`.
- The archive copy at `archive/<ts>/tex/` does NOT count as a duplicate — only source-folder copies are checked.

### Pre-compile check (LaTeX)
Before compiling any `.tex` file, verify it contains:

1. A correctly formatted `\mymarginlabel` command:
```latex
\newcommand{\mymarginlabel}{David Ewing dew59@uclive.ac.nz | \DTMnow\ | \jobname.tex}
```
2. A `\hypersetup` block with `pdfsubject` and `pdfkeywords` referencing `\jobname`:
```latex
\hypersetup{
  pdfauthor   = {David Ewing},
  pdfsubject  = {\jobname.tex},
  pdfkeywords = {source: \jobname.tex}
}
```
If either is missing or malformed, add/correct it before compiling.
