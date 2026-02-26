# CUHK-SZ Course Helper — Template Visual Specifications

All templates share: white background (#FFFFFF), 16:9 widescreen, CUHK-SZ footer branding.

---

## MATH Template

**Use for**: Pure math, applied math, optimization, linear algebra, analysis, etc.

### Colors
| Element | Color | Hex |
|---|---|---|
| Background | White | #FFFFFF |
| Primary text | Black | #000000 |
| Heading accent / underline | Navy blue | #003366 |
| Definition box background | Light blue | #EBF3FB |
| Definition box border | Navy blue | #003366 |
| Theorem box background | Light lavender | #F0EEF8 |
| Theorem box border | Dark purple | #4B0082 |
| Footer bar | Navy blue | #003366 |
| Footer text | White | #FFFFFF |
| **AI Accent Color** | Teal | #007A7A |

> **Build note**: Use **LaTeX Beamer** to generate PDF — this is the only method that replicates the template faithfully.
> - Theme: `\usetheme{Boadilla}`
> - **Verified colors (extracted from MATH template PDF vector data):**
>   - Structure/title color: `\definecolor{cuhkblue}{RGB}{51, 51, 179}` = `#3333B3` (blue-violet/indigo)
>   - Footer left   (palette primary):   `cuhkblue!90!white` → `#4747BA`
>   - Footer center (palette secondary): `cuhkblue!60!white` → `#8484D1`
>   - Footer right  (palette tertiary):  `cuhkblue!40!white` → `#ADADE0`
>   - Navigation symbol bg: `#D6D6EF` (auto-derived)
> - Palette settings (mix with white, NOT black):
>   ```latex
>   \setbeamercolor{palette primary}  {bg=cuhkblue!90!white, fg=white}
>   \setbeamercolor{palette secondary}{bg=cuhkblue!60!white, fg=white}
>   \setbeamercolor{palette tertiary} {bg=cuhkblue!40!white, fg=white}
>   \setbeamercolor{palette quaternary}{bg=cuhkblue!40!white, fg=white}
>   ```
> - Author short: `\author[SDS, CUHK(SZ)]{Professor Name}` → appears in footer left
> - Institute: `\institute[]{School of Data Science, CUHK(SZ)}` — empty short form suppresses parenthetical in footer
> - Title short: `\title[MAT3007 $|$ Lecture 1]{MAT3007: Optimization}` → appears in footer center
> - Date: `\date[]{}` — suppresses date, keeps page counter
> - **Definition slides**: `\begin{frame}` (no title arg) + plain `\textbf{Definition X.X}` inline (no Beamer block box)
> - **Content slides**: `\begin{frame}{Title}` with colored frame title
> - **Section dividers**: `\begin{frame}` + `\vfill\begin{center}{\large Section N}\\{\Large\textbf{\textcolor{cuhkblue}{...}}}\end{center}\vfill`
> - Run `pdflatex` **twice** to get correct total frame count in footer right
> - MiKTeX path (Windows): `C:/Users/10119/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdflatex`

### Typography
| Element | Font | Size | Style |
|---|---|---|---|
| Slide title | Times New Roman | 28pt | Bold |
| Section heading | Times New Roman | 22pt | Bold |
| Body text | Times New Roman | 14pt | Regular |
| Math inline | Cambria Math / LaTeX | 13pt | Regular |
| Definition label | Times New Roman | 13pt | Bold, navy |
| Footer text | Arial | 9pt | Regular |

### Layout
- Title: left-aligned, navy underline rule below
- Content area: 1in top margin from title, 0.75in side margins
- Footer: full-width navy bar, height 0.35in; left: "SSE, CUHK(SZ)"; center: course name; right: slide number
- Logo: CUHK-SZ logo in footer left area (title slide: centered top)

### Slide Types (MATH)
- `title`: large centered title, subtitle, instructor, institution, logo
- `outline`: bulleted agenda with checkboxes
- `definition`: blue box with "Definition X.X" label, formal statement
- `theorem`: lavender box with "Theorem X.X" + optional proof block
- `lemma`: similar to theorem, labeled "Lemma"
- `example`: "Example:" bold label, indented worked solution
- `remark`: italic text block with "Remark:" label
- `section_divider`: navy background, white title text
- `exercise`: "Exercise:" label, blank or partial solution space

---

## CS Template

**Use for**: CS, data science, AI/ML, programming, systems, networks, etc.

### Colors
| Element | Color | Hex |
|---|---|---|
| Background | White | #FFFFFF |
| Primary text | Dark charcoal | #2C3E50 |
| Header banner | Royal blue | #3B4FA3 |
| Header text | White | #FFFFFF |
| Heading accent | Dark navy | #1A2B5F |
| Code block background | Light gray | #F4F4F4 |
| Code block border | Medium gray | #CCCCCC |
| Bullet marker | Royal blue | #3B4FA3 |
| Footer bar | Dark navy | #1A2B5F |
| Footer text | White | #FFFFFF |
| **AI Accent Color** | Amber | #B8860B |

### Typography
| Element | Font | Size | Style |
|---|---|---|---|
| Slide title | Georgia (or serif) | 26pt | Bold |
| Section heading | Georgia | 20pt | Bold |
| Body text | Arial / Helvetica | 13pt | Regular |
| Code / monospace | Courier New | 11pt | Regular |
| Caption | Arial | 10pt | Italic |
| Footer text | Arial | 9pt | Regular |

### Layout
- Header: full-width royal blue banner, slide title in white
- Content area below banner, generous margins
- Footer: dark navy bar; course code left, lecture topic center, slide number right

> **Build note**: Use **LaTeX Beamer** to generate PDF — produces pixel-perfect results.
> - Theme: `\usetheme{Boadilla}` + custom frametitle template + `\usepackage{tikz}`
> - **Verified colors (extracted from CS template PDF vector data):**
>   - Structure/frametitle color: `\definecolor{cuhkblue}{RGB}{51, 51, 178}` = `#3333B2`
>   - Footer left   (palette primary):   `cuhkblue`           → `#3333B2`
>   - Footer center (palette secondary): `cuhkblue!75!black`  → `#262685`
>   - Footer right  (palette tertiary):  `cuhkblue!50!black`  → `#191959`
> - Palette settings (mix with **black**, unlike MATH which mixes with white):
>   ```latex
>   \setbeamercolor{palette primary}  {bg=cuhkblue,           fg=white}
>   \setbeamercolor{palette secondary}{bg=cuhkblue!75!black,  fg=white}
>   \setbeamercolor{palette tertiary} {bg=cuhkblue!50!black,  fg=white}
>   \setbeamercolor{palette quaternary}{bg=cuhkblue!50!black, fg=white}
>   ```
> - Full-width frametitle bar: `\setbeamertemplate{frametitle}` with `\begin{beamercolorbox}[wd=\paperwidth, ...]`
> - Navigation symbols: **suppressed** — `\setbeamertemplate{navigation symbols}{}`
> - Bullet style: round dots — `\setbeamertemplate{itemize item}{\scriptsize$\bullet$}`
> - Title page: tikz overlay node (`anchor=north west`) for full-width rounded blue box
> - Section divider: `\tableofcontents[currentsection, sectionstyle=show/shaded]`
> - Each `\section{}` needs ≥1 frame to appear in TOC; use `[noframenumbering]` for placeholders
> - See `references/cs_latex_template.md` for complete preamble and frame patterns

### Slide Types (CS)
- `title`: full-width rounded blue tcolorbox, course name + subtitle in white bold
- `outline`: numbered enumerate with nested itemize (round bullet dots)
- `section_divider`: shaded TOC via `\tableofcontents[currentsection]`
- `content`: frametitle blue bar + itemize with round dots + `\textcolor{cuhkblue}{...}` highlights
- `algorithm`: pseudocode or code block in gray box
- `example`: "Example:" with diagram or code
- `comparison`: two-column layout

---

## STATS Template (Default)

**Use for**: Statistics, probability, econometrics, or any unclassified course.

### Colors
| Element | Color | Hex |
|---|---|---|
| Background | White | #FFFFFF |
| Primary text | Black | #000000 |
| Heading accent | Navy blue | #003366 |
| Definition box background | Forest green | #2D8659 |
| Definition box text | White | #FFFFFF |
| Key formula box background | Light yellow | #FFFBE6 |
| Key formula box border | Gold | #D4A017 |
| Footer bar | Navy blue | #003366 |
| Footer text | White | #FFFFFF |
| **AI Accent Color** | Deep orange | #CC4400 |

### Typography
| Element | Font | Size | Style |
|---|---|---|---|
| Slide title | Times New Roman | 26pt | Bold |
| Section heading | Times New Roman | 20pt | Bold |
| Body text | Times New Roman | 13pt | Regular |
| Definition text | Arial | 13pt | White, regular |
| Formula | Cambria Math | 13pt | Regular |
| Footer text | Arial | 9pt | Regular |

### Layout
- Title: left-aligned with navy underline
- Footer: footer section backgrounds are white (invisible); only nav symbols + page counter visible
- Definition boxes: tcolorbox with dark green header and light green body

> **Build note**: Use **LaTeX Beamer** to generate PDF — produces pixel-perfect results.
> - Theme: `\usetheme{Boadilla}` — minimal customization, NO custom frametitle template
> - **Verified colors (extracted from STATS template PDF vector data):**
>   - Structure/frametitle: `\definecolor{cuhkblue}{RGB}{51, 51, 179}` = `#3333B3`
>   - Nav symbol bg: `#D6D6EF` = `cuhkblue!20!white` (auto-derived)
>   - Page counter text: `#ADADE0` = `cuhkblue!40!white` (auto-derived)
>   - Definition header: `#006600` = `RGB(0,102,0)` (`defgreen`)
>   - Definition body: `#F2FFF2` = `RGB(242,255,242)` (`deflightgreen`)
> - Palette settings (all white backgrounds → invisible footer bars):
>   ```latex
>   \setbeamercolor{palette primary}  {bg=white, fg=cuhkblue}
>   \setbeamercolor{palette secondary}{bg=white, fg=cuhkblue!60!white}
>   \setbeamercolor{palette tertiary} {bg=white, fg=cuhkblue!40!white}
>   \setbeamercolor{palette quaternary}{bg=white, fg=cuhkblue!40!white}
>   ```
> - Navigation symbols: **visible** — do NOT suppress (opposite of CS/MATH)
> - No custom frametitle — Boadilla default shows blue title on white background
> - No `\usepackage{tikz}` needed
> - Section divider: `\vfill {\Large\textbf{Section X.Y Title}} \vfill` (no frame title arg)
> - Definition boxes: `\usepackage{tcolorbox}` with `colbacktitle=defgreen, colback=deflightgreen`
> - See `references/stats_latex_template.md` for complete preamble and frame patterns

### Slide Types (STATS)
- `title`: course number, lecture title, date, instructor
- `review`: "Review of Last Lecture" section with bullets
- `section_divider`: heading-only slide with navy underline
- `definition`: green box with white text, "Definition:" label
- `formula`: yellow box with gold border, key equation
- `example`: "Example X.X" with problem statement and solution
- `table`: data or probability table with alternating row shading
- `exercise`: practice problem block
