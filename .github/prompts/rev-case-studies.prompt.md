---
name: rev-case-studies
mode: agent
description: "Revision bump: copy the latest version of each case study and the combined report to a new YYYYMMDD<ALPHA> filename, then treat the new files as the active working copies for all subsequent edits and queries."
---

From the project root (`d:\github\ENEL445`), perform the following steps:

## Step 1 — Identify the six case names

The six case names are:
- `LINEAR-CASE-STUDY`
- `QUADRATIC-CASE-STUDY`
- `LOGISTIC-CASE-STUDY`
- `HIERARCHICAL-LINEAR-CASE-STUDY`
- `HIERARCHICAL-LOGISTIC-CASE-STUDY`
- `COMBINED-REPORT`

## Step 2 — Find the latest source file for each case name

For each case name, list all files in `report/` matching the pattern `????????<ALPHA>-<CASENAME>.tex` (where `????????` is an 8-digit date and `<ALPHA>` is one uppercase letter A–Z). Sort them and take the last one (highest date + alpha). That is the source file.

## Step 3 — Determine the new filename

1. Get today's date as `YYYYMMDD` (use the system date — do NOT hardcode it).
2. Try alpha = `A`. If `report/YYYYMMDD-A-<CASENAME>.tex` does not exist, use `A`.
3. Otherwise try `B`, `C`, … in order until a free slot is found.
4. The new filename is `YYYYMMDD<ALPHA>-<CASENAME>.tex`, e.g. `20260515A-LINEAR-CASE-STUDY.tex`.

Note: the format is `YYYYMMDD` immediately followed by the alpha letter with no separator, then a hyphen, then the case name — e.g. `20260515A-LINEAR-CASE-STUDY.tex`.

## Step 4 — Copy each file

Copy (do not rename or delete) the source file to the new filename in `report/`. Do this for all six case names.

## Step 5 — Report the mapping

Print a table of old filename → new filename for all six files so the user can confirm what was created.

## Step 6 — Update session context

After the copies are made, treat the **new** filenames as the active working copies for the remainder of this conversation. All subsequent edits, content queries, and compile requests refer to the new files unless the user explicitly names a different file.
