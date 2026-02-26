---
name: cuhksz-course-helper
description: >
  CUHKsz Course Helper - Standardizes, reformats, and enriches academic course materials
  for The Chinese University of Hong Kong, Shenzhen (CUHK-SZ). Use when the user wants to:
  (1) reformat/standardize lecture slides, TA tutorials, student presentations, exam papers,
  or homework into CUHK-SZ official templates; (2) apply Level 1 structural formatting only;
  (3) apply Level 2 content enhancement by searching textbooks and online resources for the
  course; (4) generate reference answer versions of exams or homework; (5) convert course
  materials between formats (PPTX, PDF, DOCX). Triggers on: "course helper", "standardize
  slides", "update lecture PPT", "reformat course material", "CUHK course material", any
  mention of a CUHKsz course code (e.g. MAT3007, CSC3001, STA2001, DDA3020).
---

# CUHKsz Course Helper

## Quick Reference

| Input | Required? | Notes |
|---|---|---|
| Course material file | Yes | PPTX / PDF / DOCX / images |
| Course number | Yes | From prompt or extracted from file |
| Operation level | Yes | L1 or L2 (ask if not specified) |
| Course syllabus | Optional | Improves L2 quality |
| Target template | Optional | CS / MATH / STATS; default: STATS |
| Reference materials | Optional | User-supplied textbooks, notes |

## Template Selection

| Template | Use for |
|---|---|
| **CS** | CS, data science, AI/ML, programming, engineering courses |
| **MATH** | Pure math, applied math, analysis, algebra, optimization |
| **STATS** | Statistics, probability, econometrics, biostatistics |
| **STATS (default)** | Any course not clearly in CS or MATH category |

Full visual specs: `references/template_specs.md`

## Operation Levels

### Level 1 — Structural Standardization Only

Goal: Apply target template formatting. Do NOT change content meaning.

1. Extract content from input (use `scripts/extract_content.py` for PPTX; use `python -m markitdown` or PyMuPDF for PDF)
2. Map each slide to a slide type (see `references/slide_structure.md`)
3. Build output using the correct method for the template (see **Output Formats** below)
4. List suspected typos — ask user to confirm before fixing
5. Output to same directory as input; never overwrite originals

Naming: `[original_name]_updated.pdf` / `[original_name]_updated.tex`

### Level 2 — Content Enhancement

All Level 1 steps, plus:

1. **Course lookup**: fetch from `https://www.cuhk.edu.cn/zh-hans/course` using course code
2. **Textbook search**: find syllabus-linked textbooks; see `references/level2_workflow.md`
3. **Content review**: identify incomplete explanations, unanswered questions, thin sections
4. **Augmentation**: add slides matching original slide types, marked with AI visual markers
5. **Reference answers**: if input is exam/homework, generate a separate answer file

Naming:
- Enhanced: `[original_name]_enhanced.[ext]`
- Answers: `[original_name]_answers.[ext]`

**AI content markers** (never skip):
- Slides: italic text in AI Accent Color (see `references/template_specs.md`)
- Every AI-added slide: small `[Helper]` tag bottom-right
- Answer files: first slide must include disclaimer: *"AI-generated reference answers. NOT official. Verify with instructors."*

---

## Output Formats by Template

### MATH template → PDF via LaTeX Beamer (verified, pixel-perfect)

This is the only method that replicates the MATH template exactly.

**Step 1 — Read the template reference:**
```
references/math_latex_template.md
```
This contains the exact preamble (verified colors), and frame patterns for every slide type.

**Step 2 — Write the `.tex` file** using the patterns in `math_latex_template.md`:
- Use `\usetheme{Boadilla}` + `\definecolor{cuhkblue}{RGB}{51, 51, 179}`
- Footer metadata: `\author[DEPT, CUHK(SZ)]{Name}`, `\institute[]{Full Name}`, `\title[SHORT]{Full}`
- Map each slide to its frame pattern (title / outline / section_divider / definition / content / example / remark / summary)
- Definition slides: `\begin{frame}` with NO title argument, use `\textbf{Definition X.Y}` inline
- Content slides: `\begin{frame}{Title}` with colored title bar

**Step 3 — Compile:**
```bash
python scripts/compile_latex.py path/to/file.tex
```
The script runs `pdflatex` twice automatically (required for correct page totals).

**Step 4 — QA:** Convert to images with `pdftoppm -jpeg -r 150`, visually compare against reference.

### CS template → PDF via LaTeX Beamer (verified, pixel-perfect)

**Step 1 — Read the template reference:**
```
references/cs_latex_template.md
```

**Step 2 — Write the `.tex` file** using the patterns in `cs_latex_template.md`:
- Use `\usetheme{Boadilla}` + `\definecolor{cuhkblue}{RGB}{51, 51, 178}` + `\usepackage{tikz}`
- Custom full-width frametitle bar: `\setbeamertemplate{frametitle}` with `wd=\paperwidth`
- Title page: tikz overlay node with `anchor=north west` for edge-to-edge rounded blue box
- Palette mixes with **black** (CS style): `cuhkblue`, `cuhkblue!75!black`, `cuhkblue!50!black`
- Navigation symbols: **suppressed** — `\setbeamertemplate{navigation symbols}{}`
- Bullets: round dots — `\setbeamertemplate{itemize item}{\scriptsize$\bullet$}`
- Section divider: `\tableofcontents[currentsection, sectionstyle=show/shaded]`
- Each `\section{}` needs ≥1 frame; use `[noframenumbering]` for placeholder frames

**Step 3 — Compile:**
```bash
python scripts/compile_latex.py path/to/file.tex
```

**Step 4 — QA:** Convert to images with `pdftoppm -jpeg -r 150`, visually compare against reference.

### STATS template → PDF via LaTeX Beamer (verified, pixel-perfect)

**Step 1 — Read the template reference:**
```
references/stats_latex_template.md
```

**Step 2 — Write the `.tex` file** using the patterns in `stats_latex_template.md`:
- Use `\usetheme{Boadilla}` + `\definecolor{cuhkblue}{RGB}{51, 51, 179}` (no tikz needed)
- White palette backgrounds: `{bg=white, fg=cuhkblue}` — makes footer bars invisible
- Navigation symbols: **keep visible** — do NOT add `\setbeamertemplate{navigation symbols}{}`
- No custom frametitle template — Boadilla default is correct
- Section divider: `\vfill {\Large\textbf{Section X.Y Title}} \vfill` (no frame title arg)
- Definition boxes: tcolorbox with `colbacktitle=defgreen`, `colback=deflightgreen`
- Institution: "The Chinese University of Hong Kong, Shenzhen" (full name)

**Step 3 — Compile:**
```bash
python scripts/compile_latex.py path/to/file.tex
```

**Step 4 — QA:** Convert to images with `pdftoppm -jpeg -r 150`, visually compare against reference.

### PDF from PPTX

Use `scripts/convert_to_pdf.py` (tries PowerPoint COM first, then LibreOffice).

### DOCX

Use `scripts/build_docx.py`.

---

## Language Handling

- Detect input language (Chinese / English / mixed); preserve in L1
- L2 additions: match language of surrounding slide
- Math: always use LaTeX notation in `.tex` files; Unicode approximations in PPTX/DOCX

---

## Workflow

```
[Input received]
      |
[Identify: course code, level (L1/L2), template (MATH/CS/STATS)]
      |
      +--[MATH]-->[Read math_latex_template.md]-->[Write .tex]-->[compile_latex.py]-->[PDF]
      |
      +--[CS]---->[Read cs_latex_template.md]--->[Write .tex]-->[compile_latex.py]-->[PDF]
      |
      +--[STATS]-->[Read stats_latex_template.md]->[Write .tex]-->[compile_latex.py]-->[PDF]
      |
    [L2?]--yes-->[Web search + Textbook lookup]-->[Augment with AI markers]
      |
[Report: changes made, AI additions, typos flagged, output path]
```

---

## References

- `references/template_specs.md` — Visual specs + verified colors for all 3 templates
- `references/math_latex_template.md` — LaTeX Beamer preamble + frame patterns (MATH)
- `references/cs_latex_template.md` — LaTeX Beamer preamble + frame patterns (CS)
- `references/stats_latex_template.md` — LaTeX Beamer preamble + frame patterns (STATS)
- `references/slide_structure.md` — Slide type classification guide
- `references/level2_workflow.md` — L2 search and augmentation workflow
- `references/academic_standards.md` — Academic formatting rules
- `scripts/compile_latex.py` — Compile `.tex` → PDF (pdflatex ×2)
- `scripts/extract_content.py` — Extract content from PPTX to JSON
- `scripts/convert_to_pdf.py` — Convert PPTX → PDF
