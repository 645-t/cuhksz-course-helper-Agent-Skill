[README_中文.md](https://github.com/user-attachments/files/25586578/README_.md)
# CUHK-SZ Course Helper Agent Skill

A [Claude Code](https://claude.ai/claude-code) skill that standardizes, reformats, and enriches academic course materials for **The Chinese University of Hong Kong, Shenzhen (CUHK-SZ)**.

---

## Who Is This For

- **Students** who want CUHK-SZ-styled, consistently formatted, and content-enhanced course materials for self-study or to prepare their own presentations, academic reports, and meeting slides. Printable answer versions of exam past papers are also just one request away.
- **Professors and TAs** who need slides or exam papers automatically reformatted to approximate official CUHK-SZ department templates.
- Anyone working with CUHK-SZ course files (PPTX, PDF, DOCX) who needs quick
  conversion to pixel-perfect LaTeX Beamer PDFs.

---

## Features

### Three Official Templates

| Template | Source courses |  |
|---|---|---|
| **MATH** |  MAT2040| 
| **CS** | DDA3020 | 
| **STATS** | STA2001 |

All three are generated from **LaTeX Beamer** (`\usetheme{Boadilla}`) for pixel-perfect
fidelity — colors are extracted directly from real department PDFs. You can also supply your own template to the Agent.

### Slides Structural Standardization

Reformats an existing file to match the chosen template. Content is preserved exactly.

- Extracts text, layout, and embedded images from PPTX
- Maps each slide to a type (title, outline, section divider, definition, content, example, …)
- Writes a `.tex` file and compiles it to PDF via `pdflatex`
- Images are extracted and embedded with `\includegraphics` (no placeholders)
- Build artifacts (`.aux`, `.log`, `.nav`, etc.) are isolated in a temp folder and auto-deleted
- Output: `[original_name]_updated.pdf`

### Slides Content Enhancement

All Level 1 steps, plus:

- Searches for linked textbooks and reference materials
- Identifies thin sections or unanswered questions and adds supplementary slides
- All AI-added content is visually marked (italic text in AI accent color + `[Helper]` tag)
- Output: `[original_name]_enhanced.pdf`

### Exam / Homework Answer Generation

Produces a reference answer document from an exam or homework PDF.

- Uses `\documentclass{article}` (not Beamer) for natural page flow
- Solutions are placed immediately after each question
- Clean black-and-white layout: thin border title block, light-gray solution boxes
- Includes a disclaimer: *"AI-generated reference answers. NOT official. Verify with instructors."*
- Output: `[original_name]_answers.pdf`

---


## Prerequisites

**Python 3.8+** is the only manual requirement. **Everything else is handled automatically by your AI Agent.**

---
## Getting Claude Code

This skill requires [Claude Code](https://claude.ai/claude-code), Anthropic's CLI tool.

**1. Install Node.js 18+** from [nodejs.org](https://nodejs.org) if not already installed.

**2. Install Claude Code:**

```bash
npm install -g @anthropic-ai/claude-code
```

**3. Sign in:**

```bash
claude
```

Follow the prompts to authenticate with your Anthropic account. Claude Code is free to try;
sustained use requires an [Anthropic API key](https://console.anthropic.com/).


## Installation

### 1. Install the skill file

Copy `cuhksz-course-helper` into your Claude Code skills directory:

| Platform | Default skills directory |
|---|---|
| Windows | `%USERPROFILE%\.claude\skills\` |
| macOS / Linux | `~/.claude/skills/` |

### 2. Verify Claude Code recognizes the skill

```bash
claude /skills
```

The skill `cuhksz-course-helper` should appear in the list.

---

## Usage

Simply describe your task to Claude Code in natural language. The skill triggers on:

- Any CUHK-SZ course code (e.g. `MAT1001`, `DDA3020`, `STA2001`)
- Keywords: `"standardize slides"`, `"reformat course material"`, `"CUHK course material"`,
  `"update lecture PPT"`, `"生成答案版"`, etc.

**Examples:**

```
把桌面上的 Ch5.pptx 换成 STA2001 风格的课件
```
```
Generate a reference answer version of the MAT1001 final exam on my desktop.
```
```
Reformat this lecture slides to match DDA3020 style, Level 1 only.
```

### Intake questions

After receiving the file, the skill asks for any missing information in a single prompt:

1. **Course number + instructor name** — used for footer and title metadata
2. **Slide style** — presented as course code examples (STA2001 / DDA3020 / MAT2040)
3. **Operation level** — L1 (format only) or L2 (format + content enhancement / answer generation)

If any of these are already stated in your request, those questions are skipped.

---

## File Structure

```
cuhksz-course-helper/
├── SKILL.md                          # Skill definition and workflow guide
├── scripts/
│   ├── extract_content.py            # Extract text + images from PPTX → JSON
│   ├── compile_latex.py              # pdflatex wrapper (2-pass, auto temp-folder cleanup)
│   └── convert_to_pdf.py             # PPTX → PDF (PowerPoint COM or LibreOffice)
└── references/
    ├── template_specs.md             # Visual specs and verified colors for all 3 templates
    ├── math_latex_template.md        # Complete Beamer preamble + frame patterns (MATH)
    ├── cs_latex_template.md          # Complete Beamer preamble + frame patterns (CS)
    ├── stats_latex_template.md       # Complete Beamer preamble + frame patterns (STATS)
    ├── slide_structure.md            # Slide type classification guide
    ├── level2_workflow.md            # L2 search and augmentation workflow
    └── academic_standards.md        # Academic formatting rules
```

---

## Output Naming

| Task | Output file |
|---|---|
| standardization | `[original_name]_updated.tex` + `[original_name]_updated.pdf` |
| enhancement | `[original_name]_enhanced.pdf` |
| Answer generation | `[original_name]_answers.tex` + `[original_name]_answers.pdf` |

**Original files are never overwritten.**

---

## Notes


- AI-added content is always visually distinguished from original material.
- The `.tex` source is kept alongside the PDF so that you can make manual edits.
- Image extraction from PPTX requires slides to contain actual embedded Picture shapes
  (not linked or OLE objects).



