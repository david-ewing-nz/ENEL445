# ENEL445 Workspace Review & Session Log

**Review Started:** February 25, 2026  
**Last Updated:** February 25, 2026 - 22:00 UTC

---

## Current Session Context

**Session Date:** February 25, 2026  
**Last Activity:** 22:00 UTC  
**Current Focus:** PDF to LaTeX conversion in progress (AUTOMATED)
**Current Task:** Batch converting 44 PDFs → Markdown + LaTeX files

### What's Running Now (BACKGROUND PROCESSES)
- Batch PDF Conversion (PID 28248) - Converting 44 PDFs using Marker
- Auto-Replacement Monitor (PID 28864) - Replacing notes/*.md as conversions complete
- Estimated completion: 2-3 hours (overnight)

**TO CHECK STATUS WHEN YOU RETURN:**
```powershell
& "d:\github\ENEL445\scripts\check_status.ps1"
```

**CONVERSION LOG:**
```
d:\github\ENEL445\conversion_log.txt
```


### Completed Today
1. VS Code moved to D: drive (freed 1.22 GB from C:)
2. Installed Marker PDF converter (AI-powered OCR with LaTeX support)
3. Installed MiKTeX (XeLaTeX compiler) to D:\MiKTeX (961 MB)
4. Created automated conversion pipeline: PDF → Markdown → .tex
5. Started batch conversion of all 44 course PDFs

### Next Steps (When Conversion Completes)
1. Verify LaTeX rendering in markdown preview
2. Check .tex files compile with XeLaTeX
3. Begin course review with proper math notation

---

## Workspace Overview

### Folder Structure
- **context/** - Extracted text files from course materials (lectures, notes, projects)
- **contents/** - MATLAB and Python implementation files
- **Week 1/** - Week 1 PDF lecture materials
- **scripts/** - Utility scripts for PDF/PPTX extraction
- **reference/** - Reference materials and tests
- **_unzipped/** - Unzipped course content archive

### Key Files
- `ENEL445-26S1_1771808777.zip` - Main course archive
- `capture-course-files-from-zip-ALL-FROM-CONTENT.ps1` - Content extraction script
- `capturepdfs.ps1` - PDF capture script
- Various `.m` (MATLAB) and `.py` (Python) files in contents/

---

## Session History

### Session 1 - February 25, 2026

#### Actions Taken
**18:00** - Created `.vscode/ENEL445-workspace-review.md` as session tracking file
**18:05** - Established structure for session logging and continuity
**18:15** - Fixed PDF extraction script path (`reference/contents/`)
**18:20** - Ran image extraction (1,205 images from 44 PDFs)
**18:30** - Generated 44 markdown files with embedded images
**18:35** - Implemented Option C structure (moved .md to `reference/notes/`)
**18:40** - Installed Markdown extensions (All in One + Preview Enhanced)
**18:42** - Fixed PowerShell execution policy (no more prompts)
**18:45** - Added timestamp tracking to session log
**18:47** - Documented initial VS Code extensions
**18:50** - Installed LaTeX Workshop extension and updated complete extension list

#### Extensions Installed This Session
- Markdown All in One (yzhang.markdown-all-in-one)
- Markdown Preview Enhanced (shd101wyy.markdown-preview-enhanced)
- LaTeX Workshop (james-yu.latex-workshop)

#### Pre-existing Extensions Discovered
- PowerShell (ms-vscode.powershell)
- Python + Pylance (ms-python.python, ms-python.vscode-pylance)
- R (reditorsupport.r)
- GitHub Copilot Chat (github.copilot-chat)

#### Decisions Made
- Using markdown file in .vscode folder for session persistence
- Structured with: Current Context, Session History, Progress Tracking, Notes

#### Current State
- Workspace contains extracted course materials in context/
- Implementation files available in contents/
- Week 1 PDFs in dedicated folder
- Review/analysis work not yet started

#### Questions/Blockers
- Waiting for user direction on what to review/analyze next

---

## Overall Progress Tracking

### Completed Tasks
- [x] Workspace initial setup
- [x] Course content extraction to text files
- [x] Session tracking system created

### In Progress
- [ ] *(no active tasks)*

### Planned/Backlog
- [ ] *(awaiting user direction)*

---

## Key Findings & Insights

### Course Content Identified
- Multiple lecture series (T2-1 through T2-8)
- Topics: Nelder-Mead, GPS, DIRECT, Nature-Inspired Algorithms, Linear Programming, Discrete Optimisation, Simulated Annealing, Game Theory, Multi-objectives
- Projects: Geolocation (FDOA), Power Systems Optimisation
- Sample questions and practice materials available

### Technical Files
- MATLAB implementations for: BFGS, Bisection, FDOA, Hammersley sequences, ML cost functions
- Python implementations for: plant building/operation, simulation
- Coordinate transformation utilities (ECEF, LLA, ENU)

---

## Notes & Observations

### Important Context
- Course: ENEL445 - Applied Engineering Optimisation
- Semester: 2026 S1
- Contains both Term 1 and Term 2 materials
- Mix of constrained/unconstrained optimisation topics

### Questions to Clarify
- What is the specific review objective?
- Are we studying for exam, working on project, or organizing materials?
- Which topics/weeks to prioritize?

---
---

## Installed Tools & Environment

**All tools installed on D: drive to preserve C: drive space**

### LaTeX & PDF Processing

| Tool | Location | Size | Purpose |
|------|----------|------|---------|
| **MiKTeX 25.12** | D:\MiKTeX | 961 MB | XeLaTeX compiler for .tex → PDF |
| **XeLaTeX** | D:\MiKTeX\miktex\bin\x64\xelatex.exe | - | LaTeX engine with Unicode support |
| **Pandoc 3.6.4** | C:\Program Files\Pandoc | - | Markdown → LaTeX conversion |

### Python & AI Tools

| Tool | Location | Purpose |
|------|----------|---------|
| **Python 3.12.3** | D:\Python | Python interpreter |
| **Marker PDF 1.10.2** | D:\Python\Lib\site-packages\marker | AI-powered PDF → Markdown with LaTeX OCR |
| **PyTorch 2.10.0** | D:\Python\Lib\site-packages\torch | Deep learning backend for Marker |
| **Transformers 4.57.6** | D:\Python\Lib\site-packages\transformers | NLP models for text recognition |
| **Surya OCR 0.17.1** | D:\Python\Lib\site-packages\surya_ocr | Advanced OCR for equations |

**AI Model Cache:** C:\Users\david\AppData\Local\datalab (~1.5 GB, one-time download)

### Conversion Pipeline

```
PDF → [Marker] → Markdown + LaTeX → [Pandoc] → .tex → [XeLaTeX] → PDF
```

**Scripts:**
- `d:\github\ENEL445\scripts\batch_convert.ps1` - Batch PDF conversion
- `d:\github\ENEL445\scripts\auto_replace_notes.ps1` - Auto-replace monitor
- `d:\github\ENEL445\scripts\check_status.ps1` - Status checker

---

## Action Items for Next Session

1. Determine review focus/objective
2. TBD based on user needs

---

## Quick Reference Timeline

| Date | Time (UTC) | Session | Key Activity |
|------|------------|---------|--------------|
| 2026-02-25 | 18:00-18:45 | 1 | Workspace setup, image extraction, markdown generation |

---

**Instructions for Next Agent:**
1. Read "Current Session Context" section first
2. Review latest entry in "Session History"
3. Check "In Progress" tasks
4. Update "Last Updated" date when making changes
5. Add new session entry when starting new work
6. Keep "Current Session Context" updated with latest status

### Language Convention: British English

**All work must use British English spelling and conventions:**

- **Agent Responses:** Use British English in all communications (optimisation, behaviour, colour, analyse, parametrise, etc.)
- **Code Comments:** All comments in code must use British English spelling
- **Variable Names:** Where naming is at your discretion, use British English (e.g., `colour_map`, `optimisation_result`, `behaviour_flag`)
- **Documentation:** All markdown files, reports, and written documents must use British English
- **Exception:** Do NOT change fixed command names, library functions, or API arguments that are defined in US English (e.g., `color` parameter in matplotlib, `minimize` function in scipy). These are non-optional system-defined names.

**Rationale:** University of Canterbury (NZ) follows British English conventions. Course title is "Applied Engineering Optimisation" (British spelling).

### Character Set Convention: No Unicode or Emoji

**All code and documentation must use ASCII characters only:**

- **Code Files:** No emoji or unicode symbols in Python, MATLAB, or any source code files
- **Code Comments:** Use plain ASCII text only (no ✓, ✗, →, etc.)
- **Documentation:** No emoji in markdown files, reports, or LaTeX documents
- **Exception:** Mathematical notation in LaTeX equations is permitted (e.g., `$\mu$`, `$\tau$`, `$\lambda$`)

**Rationale:** Ensures maximum compatibility, readability in all editors, and professional academic standards.

---

## VS Code Extensions

**Installed as of:** February 25, 2026 - 18:50 UTC

### Essential for ENEL445

| Extension | ID | Purpose |
|-----------|-----|---------|
| **Markdown All in One** | yzhang.markdown-all-in-one | Math/LaTeX support, auto-completion, shortcuts |
| **Markdown Preview Enhanced** | shd101wyy.markdown-preview-enhanced | Superior math rendering (KaTeX/MathJax), export to PDF |
| **LaTeX Workshop** | james-yu.latex-workshop | LaTeX compilation, preview for reports |

### Programming Language Support

| Extension | ID | Purpose |
|-----------|-----|---------|
| **Python** | ms-python.python | Python IntelliSense, debugging, linting |
| **Pylance** | ms-python.vscode-pylance | Fast Python language server, type checking |
| **PowerShell** | ms-vscode.powershell | PowerShell scripting, IntelliSense, debugging |
| **R** | reditorsupport.r | R language support for statistical optimization |

### AI Assistant

| Extension | ID | Purpose |
|-----------|-----|---------|
| **GitHub Copilot Chat** | github.copilot-chat | AI coding assistance (currently in use!) |

**Note:** All extensions are essential for working with ENEL445 optimization code (Python, MATLAB via text), writing reports (LaTeX), and taking notes with proper mathematical notation (Markdown + LaTeX).

