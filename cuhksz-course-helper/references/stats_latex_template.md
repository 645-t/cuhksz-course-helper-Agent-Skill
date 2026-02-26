# STATS Template — LaTeX Beamer Reference

Use this file to write `.tex` files that match the CUHK-SZ STATS template exactly.
After writing the `.tex`, compile with `scripts/compile_latex.py`.

---

## Preamble (copy verbatim for every STATS slide deck)

```latex
\documentclass{beamer}   % default 4:3 aspect ratio matches STATS template
\usetheme{Boadilla}

% ── Verified colors (extracted from STATS template PDF vector data) ──────────
% Structure/frametitle: #3333B3 = RGB(51,51,179)  [same base as MATH template]
% Nav symbol bg:   #D6D6EF = cuhkblue!20!white (auto-derived)
% Page counter:    #ADADE0 = cuhkblue!40!white (auto-derived)
% White palette backgrounds → footer section bars are invisible
\definecolor{cuhkblue}{RGB}{51, 51, 179}
\setbeamercolor{structure}{fg=cuhkblue}
\setbeamercolor{palette primary}  {bg=white, fg=cuhkblue}
\setbeamercolor{palette secondary}{bg=white, fg=cuhkblue!60!white}
\setbeamercolor{palette tertiary} {bg=white, fg=cuhkblue!40!white}
\setbeamercolor{palette quaternary}{bg=white, fg=cuhkblue!40!white}

% ── Definition box colors ────────────────────────────────────────────────────
\definecolor{defgreen}{RGB}{0, 102, 0}       % #006600 — header bg
\definecolor{deflightgreen}{RGB}{242, 255, 242} % #F2FFF2 — body bg

% ── STATS style: navigation symbols remain VISIBLE (do NOT suppress) ─────────
% (CS and MATH templates suppress navigation symbols; STATS keeps them)

% ── Packages ─────────────────────────────────────────────────────────────────
\usepackage{amsmath, amssymb, bm}
\usepackage{graphicx}            % for \includegraphics
\usepackage{tcolorbox}
\tcbuselibrary{skins}

% ── Metadata ─────────────────────────────────────────────────────────────────
\title[COURSE]{COURSE Full Title}
\subtitle{Lecture N}
\author[Short Name]{Full Name}
\institute[]{The Chinese University of Hong Kong, Shenzhen}
\date[]{}    % empty — no date in footer for STATS

\begin{document}
% ... frames here ...
\end{document}
```

**Critical differences from CS/MATH templates:**
- Palette backgrounds are **white** (no colored footer bars)
- Navigation symbols **visible** — do NOT add `\setbeamertemplate{navigation symbols}{}`
- No `\usepackage{tikz}` or custom frametitle template — Boadilla default is correct
- No date in footer: `\date[]{}`
- Institution: "The Chinese University of Hong Kong, Shenzhen" (full name, not abbreviated)

---

## Frame Patterns by Slide Type

### title — Title page

```latex
\begin{frame}
  \titlepage
\end{frame}
```

The default Boadilla title page produces the correct centered layout:
- Course name in blue (large)
- Lecture number in blue (medium)
- Author in black
- Institution in smaller black

---

### section_divider — Bold black section heading

```latex
\begin{frame}
  \vfill
  {\Large\textbf{Section X.Y Section Title Here}}
  \vfill
\end{frame}
```

**No frame title argument** → no colored title bar. Text is left-aligned, vertically centered, in black bold.

---

### review — Review of last lecture (with definition box)

```latex
\begin{frame}{Review of the Last Lecture}
  Key concepts and/or techniques:
  \begin{itemize}
    \item Topic Name:\\[0.3em]
          One-sentence description.
  \end{itemize}

  \medskip

  \begin{tcolorbox}[
    enhanced,
    colback=deflightgreen,
    colframe=defgreen,
    colbacktitle=defgreen,
    coltitle=white,
    fonttitle=\bfseries,
    title={Definition[Name of Concept]},
    arc=2pt,
    boxrule=0.5pt,
  ]
    Formal definition text with math $f(x) = \ldots$
  \end{tcolorbox}
\end{frame}
```

---

### definition — Definition slide (standalone tcolorbox)

```latex
\begin{frame}{Frame Title}
  Introductory text.

  \begin{tcolorbox}[
    enhanced,
    colback=deflightgreen,
    colframe=defgreen,
    colbacktitle=defgreen,
    coltitle=white,
    fonttitle=\bfseries,
    title={Definition[Concept Name]},
    arc=2pt,
    boxrule=0.5pt,
  ]
    A random variable $X$ is said to have a \textbf{distribution name}
    with parameter $\theta$ if its pmf/pdf satisfies
    \[
      f(x) = \ldots, \quad x \in \mathcal{X}.
    \]
  \end{tcolorbox}
\end{frame}
```

---

### content — Regular content slide

```latex
\begin{frame}{Frame Title}
  Introductory sentence about the topic.

  \bigskip

  Define a random variable $X$ to denote the quantity of interest.
  Then $X$ has the range $\overline{S} = \{a, b, \cdots\}$.

  \medskip

  Key equation: $f(x) = P(X = x)$.
\end{frame}
```

---

### math — Aligned derivations

```latex
\begin{frame}{Frame Title}
  \begin{align*}
    f(x) &= P(\{\text{event description}\}) \\
         &= P(A \cap B) \\
         &= P(A)P(B) \quad\text{(because $A$ and $B$ are independent)}
  \end{align*}
\end{frame}
```

For labeled sets with underbrace:
```latex
    f(x) &= P\Bigl(
      \underbrace{\{\text{first condition}\}}_{A}
      \cap
      \underbrace{\{\text{second condition}\}}_{B}
    \Bigr) \\
```

---

### image — Slide with image only (no text body)

Images extracted by `extract_content.py` go to the `images/` subfolder.
Use paths exactly as returned in `image_paths`, e.g. `images/slide_04_img_01.png`.

```latex
\begin{frame}{Frame Title}
  \begin{center}
    \includegraphics[width=0.92\textwidth,
                     height=0.75\textheight,
                     keepaspectratio]{images/slide_04_img_01.png}
  \end{center}
\end{frame}
```

### image+text — Slide with text above and image below

```latex
\begin{frame}{Frame Title}
  Introductory sentence or brief explanation.

  \medskip

  \begin{center}
    \includegraphics[width=0.88\textwidth,
                     height=0.60\textheight,
                     keepaspectratio]{images/slide_08_img_01.png}
  \end{center}
\end{frame}
```

### image-multi — Two images side by side

```latex
\begin{frame}{Frame Title}
  \begin{columns}[c]
    \column{0.5\textwidth}
    \centering
    \includegraphics[width=\linewidth,
                     height=0.70\textheight,
                     keepaspectratio]{images/slide_19_img_01.jpg}

    \column{0.5\textwidth}
    \centering
    \includegraphics[width=\linewidth,
                     height=0.70\textheight,
                     keepaspectratio]{images/slide_19_img_02.jpg}
  \end{columns}
\end{frame}
```

**Rules for images:**
- Always use `keepaspectratio` — never stretch or crop
- `width=0.92\textwidth, height=0.75\textheight` for full-slide images
- `width=0.88\textwidth, height=0.60\textheight` when text is also present
- Require `\usepackage{graphicx}` in preamble

---

## Color Reference

| Element | Color | Value |
|---|---|---|
| Structure / frame titles | `#3333B3` | `RGB(51,51,179)` |
| Nav symbol bg (auto) | `#D6D6EF` | `cuhkblue!20!white` |
| Page counter (auto) | `#ADADE0` | `cuhkblue!40!white` |
| Definition header bg | `#006600` | `RGB(0,102,0)` |
| Definition body bg | `#F2FFF2` | `RGB(242,255,242)` |
| AI Accent Color | Deep orange | `#CC4400` |

**Note**: STATS uses `cuhkblue = RGB(51,51,179)` (same as MATH). Palette mixes with **white** but at zero bg-opacity (white palette → invisible footer bars).

---

## Compilation

```bash
python scripts/compile_latex.py path/to/file.tex [output_dir]
```

Run `pdflatex` **twice** for correct total frame count in footer page counter.

---

## Complete Minimal Example

```latex
\documentclass{beamer}
\usetheme{Boadilla}
\definecolor{cuhkblue}{RGB}{51, 51, 179}
\setbeamercolor{structure}{fg=cuhkblue}
\setbeamercolor{palette primary}  {bg=white, fg=cuhkblue}
\setbeamercolor{palette secondary}{bg=white, fg=cuhkblue!60!white}
\setbeamercolor{palette tertiary} {bg=white, fg=cuhkblue!40!white}
\setbeamercolor{palette quaternary}{bg=white, fg=cuhkblue!40!white}
\definecolor{defgreen}{RGB}{0, 102, 0}
\definecolor{deflightgreen}{RGB}{242, 255, 242}
\usepackage{amsmath, amssymb, bm}
\usepackage{tcolorbox}
\tcbuselibrary{skins}
\title[STA2001]{STA2001 Probability and Statistics (I)}
\subtitle{Lecture 1}
\author[T.\ Chen]{Tianshi Chen}
\institute[]{The Chinese University of Hong Kong, Shenzhen}
\date[]{}
\begin{document}
\begin{frame}\titlepage\end{frame}
\begin{frame}
  \vfill
  {\Large\textbf{Section 1.1 Introduction to Probability}}
  \vfill
\end{frame}
\begin{frame}{Key Concept}
  \begin{tcolorbox}[
    enhanced, colback=deflightgreen, colframe=defgreen,
    colbacktitle=defgreen, coltitle=white, fonttitle=\bfseries,
    title={Definition[Sample Space]}, arc=2pt, boxrule=0.5pt]
    The \textbf{sample space} $\Omega$ is the set of all possible outcomes.
  \end{tcolorbox}
\end{frame}
\end{document}
```
