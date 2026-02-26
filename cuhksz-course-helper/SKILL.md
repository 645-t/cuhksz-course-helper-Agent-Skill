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

## Intake Questions (run FIRST, before any extraction)

After receiving the input file, **immediately ask the user** the following using
`AskUserQuestion` — but only for information not already present in the prompt.

### What to ask

**Q1 — Course info** (skip if course number AND instructor are already stated):
> 请确认课程信息：课程编号（如 STA2001）和授课老师姓名？

**Q2 — Slide style** (skip if user already specified a style/template):
Present **three options** by example course code — do NOT use the words
STATS / CS / MATH anywhere in the question or option labels:

| Option label shown to user | Internal template to use |
|---|---|
| STA2001 风格 | STATS |
| DDA3020 风格 | CS |
| MAT2040 风格 | MATH |

**Q3 — Operation level** (skip if already stated):
> 需要哪个级别？L1（仅重排格式）或 L2（重排 + 内容增强/补充参考答案）？

### Rules

- Ask all missing questions in **one single `AskUserQuestion` call** (up to 3 questions).
- If the user's prompt already answers a question (e.g., "换成 STA 风格"), skip that question.
- Answers from Q2 map to internal template names: STA2001-style → **STATS**, DDA3020-style → **CS**, MAT2040-style → **MATH**. Use the internal name everywhere in the workflow below; never expose it to the user.
- If user picks "Other" for style, ask a follow-up to clarify the course, then infer the closest template.

---

## Quick Reference

| Input | Required? | Notes |
|---|---|---|
| Course material file | Yes | PPTX / PDF / DOCX / images |
| Course number | Collected via intake | Ask if missing |
| Instructor name | Collected via intake | Ask if missing |
| Operation level | Collected via intake | Ask if missing |
| Slide style | Collected via intake | Presented as course code examples |
| Course syllabus | Optional | Improves L2 quality |
| Reference materials | Optional | User-supplied textbooks, notes |

## Template Mapping (internal — never show these names to the user)

| Internal name | Representative course shown to user |
|---|---|
| **STATS** | STA2001, STA2002, STA3010, … |
| **CS** | DDA3020, CSC3001, CSC4005, … |
| **MATH** | MAT2040, MAT3007, MAT4001, … |

Full visual specs: `references/template_specs.md`

## Operation Levels

### Level 1 — Structural Standardization Only

Goal: Apply target template formatting. Do NOT change content meaning.

1. **Extract content** from input:
   - PPTX: use `scripts/extract_content.py` — this also extracts all images to an `images/` subfolder and records their paths in the JSON under `image_paths`
   - PDF: use `python -m markitdown` or PyMuPDF
2. **Map each slide** to a slide type (see `references/slide_structure.md`)
3. **Build output** using the correct method for the template (see **Output Formats** below)
   - Write the `.tex` file to the **same directory** as the source PPTX so that `\includegraphics{images/...}` paths resolve correctly
   - For every slide that has `image_paths`, embed images using `\includegraphics` (see image patterns in the template references)
4. **List suspected typos** — ask user to confirm before fixing
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
- Answer files: title block must include disclaimer: *"AI-generated reference answers. NOT official. Verify with instructors."*

---

## Output Formats by Template

### MATH template → PDF via LaTeX Beamer (verified, pixel-perfect)

**Step 1 — Read the template reference:**
```
references/math_latex_template.md
```

**Step 2 — Write the `.tex` file** using the patterns in `math_latex_template.md`:
- Use `\usetheme{Boadilla}` + `\definecolor{cuhkblue}{RGB}{51, 51, 179}`
- Add `\usepackage{graphicx}` to the preamble
- Footer metadata: `\author[DEPT, CUHK(SZ)]{Name}`, `\institute[]{Full Name}`, `\title[SHORT]{Full}`
- Map each slide to its frame pattern (title / outline / section_divider / definition / content / example / remark / summary)
- For slides with images: use `\includegraphics` patterns from `math_latex_template.md`

**Step 3 — Compile:**
```bash
python scripts/compile_latex.py path/to/file.tex
```
Runs `pdflatex` twice; all intermediate files go into a temp folder that is automatically deleted.

**Step 4 — QA:** Convert to images with `pdftoppm -jpeg -r 150`, visually compare against reference.

### CS template → PDF via LaTeX Beamer (verified, pixel-perfect)

**Step 1 — Read the template reference:**
```
references/cs_latex_template.md
```

**Step 2 — Write the `.tex` file** using the patterns in `cs_latex_template.md`:
- Use `\usetheme{Boadilla}` + `\definecolor{cuhkblue}{RGB}{51, 51, 178}` + `\usepackage{tikz}`
- Add `\usepackage{graphicx}` to the preamble
- Custom full-width frametitle bar: `\setbeamertemplate{frametitle}` with `wd=\paperwidth`
- Title page: tikz overlay node with `anchor=north west` for edge-to-edge rounded blue box
- Palette mixes with **black** (CS style): `cuhkblue`, `cuhkblue!75!black`, `cuhkblue!50!black`
- Navigation symbols: **suppressed** — `\setbeamertemplate{navigation symbols}{}`
- Bullets: round dots — `\setbeamertemplate{itemize item}{\scriptsize$\bullet$}`
- Section divider: `\tableofcontents[currentsection, sectionstyle=show/shaded]`
- Each `\section{}` needs ≥1 frame; use `[noframenumbering]` for placeholder frames
- For slides with images: use `\includegraphics` patterns from `cs_latex_template.md`

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
- Add `\usepackage{graphicx}` to the preamble
- White palette backgrounds: `{bg=white, fg=cuhkblue}` — makes footer bars invisible
- Navigation symbols: **keep visible** — do NOT add `\setbeamertemplate{navigation symbols}{}`
- No custom frametitle template — Boadilla default is correct
- Section divider: `\vfill {\Large\textbf{Section X.Y Title}} \vfill` (no frame title arg)
- Definition boxes: tcolorbox with `colbacktitle=defgreen`, `colback=deflightgreen`
- Institution: "The Chinese University of Hong Kong, Shenzhen" (full name)
- For slides with images: use `\includegraphics` patterns from `stats_latex_template.md`

**Step 3 — Compile:**
```bash
python scripts/compile_latex.py path/to/file.tex
```

**Step 4 — QA:** Convert to images with `pdftoppm -jpeg -r 150`, visually compare against reference.

### Answer Documents (exam / homework) → PDF via LaTeX article

Use `\documentclass[11pt,a4paper]{article}` — **not** Beamer. Solutions flow
naturally across pages, unlike fixed-height slides.

**Styling rules (black/white — no color added unless source has color):**
- Title block: thin black border, white background, black text
- Question headers: horizontal rules + bold "Question N", no color
- Solution boxes: `tcolorbox` with `colback=RGB(246,246,246)` (very light gray),
  `colframe=black!45`, dark gray title tag — use `breakable` for long solutions
- Header/footer: plain black text, `\fancyhdr`
- Place disclaimer in the title block (not a separate slide)

**Structure:** For each question, show the problem statement then the solution immediately after (same page flow). Use `\allowframebreaks` equivalent via `breakable` tcolorbox.

**Compile with the same script:**
```bash
python scripts/compile_latex.py path/to/file.tex
```

**Naming:** `[original_name]_answers.pdf` / `[original_name]_answers.tex`

### PDF from PPTX

Use `scripts/convert_to_pdf.py` (tries PowerPoint COM first, then LibreOffice).

### DOCX

Use `scripts/build_docx.py`.

---

## Image Handling

When extracting from PPTX with `scripts/extract_content.py`:
- All images are saved to an `images/` subfolder next to the JSON/PPTX
- Each slide's `image_paths` lists relative paths like `"images/slide_04_img_01.png"`
- These paths are ready for use directly in `\includegraphics{images/slide_04_img_01.png}`

**Critical**: Write the `.tex` file to the **same directory** as the `images/` folder (i.e., the same directory as the source PPTX). If the .tex is elsewhere, copy the `images/` folder next to it.

---

## Language Handling

- Detect input language (Chinese / English / mixed); preserve in L1
- L2 additions: match language of surrounding slide
- Math: always use LaTeX notation in `.tex` files; Unicode approximations in PPTX/DOCX

---

## Workflow

```
[Input file received]
      |
[Quick scan: detect course code / instructor / style / file type]
      |
[Intake: AskUserQuestion for any missing: course info, style (by course code), level]
      |
      +--[exam/homework answer request]
      |    --> article-class .tex (Q+solution layout, light-gray solbox, no color)
      |    --> compile_latex.py --> [original_name]_answers.pdf
      |
[Extract content: extract_content.py → JSON + images/ folder]
      |
      +--[MATH]-->[Read math_latex_template.md]-->[Write .tex with \includegraphics]-->[compile_latex.py]-->[PDF]
      |
      +--[CS]---->[Read cs_latex_template.md]--->[Write .tex with \includegraphics]-->[compile_latex.py]-->[PDF]
      |
      +--[STATS]-->[Read stats_latex_template.md]->[Write .tex with \includegraphics]-->[compile_latex.py]-->[PDF]
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
- `scripts/compile_latex.py` — Compile `.tex` → PDF (pdflatex ×2, temp folder auto-cleaned)
- `scripts/extract_content.py` — Extract content + images from PPTX to JSON
- `scripts/convert_to_pdf.py` — Convert PPTX → PDF
