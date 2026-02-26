# MATH Template — LaTeX Beamer Reference

Use this file to write `.tex` files that match the CUHK-SZ MATH template exactly.
After writing the `.tex`, compile with `scripts/compile_latex.py`.

---

## Preamble (copy verbatim for every MATH slide deck)

```latex
\documentclass{beamer}   % default 4:3 aspect ratio matches MATH template
\usetheme{Boadilla}

% ── Verified colors (extracted from MATH template PDF vector data) ─────────────
% Structure/title: #3333B3 = RGB(51,51,179)
% Footer primary:  #4747BA  Footer secondary: #8484D1  Footer tertiary: #ADADE0
\definecolor{cuhkblue}{RGB}{51, 51, 179}
\setbeamercolor{structure}{fg=cuhkblue}
\setbeamercolor{palette primary}  {bg=cuhkblue!90!white, fg=white}
\setbeamercolor{palette secondary}{bg=cuhkblue!60!white, fg=white}
\setbeamercolor{palette tertiary} {bg=cuhkblue!40!white, fg=white}
\setbeamercolor{palette quaternary}{bg=cuhkblue!40!white, fg=white}

% ── Math + image packages ──────────────────────────────────────────────────────
\usepackage{amsmath, amssymb, bm}
\usepackage{graphicx}            % for \includegraphics

% ── Metadata → footer: left=short author | center=short title | right=page ────
\title[COURSE $|$ Lecture N]{COURSE: Full Title}
\subtitle{Lecture N: Lecture Title}
\author[DEPT, CUHK(SZ)]{Professor Name}
\institute[]{School Name, CUHK(SZ)}   % MUST use [] empty short form
\date[]{}                               % suppress date; keeps page counter

\begin{document}
% ... frames here ...
\end{document}
```

**Critical rules for metadata:**
- `\author[SHORT]{}` — SHORT appears in footer left (e.g. `SDS, CUHK(SZ)`)
- `\institute[]{}` — empty `[]` prevents "(full name)" appending in footer
- `\title[SHORT]{}` — SHORT appears in footer center
- `\date[]{}` — empty, suppresses date field

---

## Frame Patterns by Slide Type

### title — Title page

```latex
\begin{frame}
  \titlepage
\end{frame}
```

---

### outline — Agenda / Table of contents

```latex
\begin{frame}{Outline}
  \begin{enumerate}
    \item Topic One
    \item Topic Two
    \item Topic Three
  \end{enumerate}
\end{frame}
```

---

### section_divider — Section break slide

```latex
\begin{frame}
  \vfill
  \begin{center}
    {\large Section N}\\[0.8em]
    {\Large\textbf{\textcolor{cuhkblue}{Section Title Here}}}
  \end{center}
  \vfill
\end{frame}
```

Note: no `{Title}` argument → no frame title bar at top.

---

### definition — Definition slide (NO frame title)

```latex
\begin{frame}
  \textbf{Definition X.Y}\quad\textbf{(Name)}
  \medskip

  Formal statement here, with math $f(\mathbf{x}) \le 0$.

  \bigskip

  \textbf{Definition X.Z}\quad\textbf{(Another Name)}
  \medskip

  Another definition here.
\end{frame}
```

**Critical**: Do NOT use `\begin{definition}` Beamer block. Do NOT add a frame title.
Use `\textbf{Definition X.Y}` inline, separated by `\bigskip`.

---

### content — Regular content slide

```latex
\begin{frame}{Frame Title}
  Introductory sentence.

  \medskip

  \textbf{Category One:} description text
  \begin{itemize}
    \item First point.
    \item Second point.
  \end{itemize}

  \medskip

  \textbf{Category Two:} description
  \begin{itemize}
    \item Point A.
    \item Point B.
  \end{itemize}
\end{frame}
```

---

### example — Worked example

```latex
\begin{frame}{Example X.Y\quad(Short Description)}
  Setup sentence.
  \[
    \begin{aligned}
      \text{maximize}   & \quad \text{expression} \\
      \text{subject to} & \quad \text{constraint}, \quad \text{label} \\
                        & \quad x_1, x_2 \ge 0
    \end{aligned}
  \]
  \medskip
  \textbf{Key term:} explanation.\quad
  \textbf{Another term:} explanation.
\end{frame}
```

---

### theorem — Theorem / Proposition

```latex
\begin{frame}{Theorem X.Y\quad(Name)}
  \textbf{Theorem X.Y}\quad\textbf{(Name)}
  \medskip

  Statement: if condition, then $f(\mathbf{x}^*) \le f(\mathbf{x})$.

  \medskip
  \textit{Proof sketch.} Argument here. \qed
\end{frame}
```

---

### remark — Remark / Note

```latex
\begin{frame}{Remark: Short Label}
  Remark body. The infimum $\inf_{\mathbf{x}\in\mathcal{D}} f(\mathbf{x})$
  always exists but may not be attained.

  \medskip

  \textbf{Example.} Minimise $x$ subject to $x > 0$.
  \[
    \inf = 0 \quad(\text{not attained}); \quad \min \text{ does not exist.}
  \]

  \bigskip
  \textit{Consequence.} Key takeaway here.
\end{frame}
```

---

### summary — Summary / review slide

```latex
\begin{frame}{Summary of Lecture N}
  \begin{enumerate}
    \item \textbf{Key concept:}\quad brief recap.
    \item Feasible region $\mathcal{D}$, optimal solution $\mathbf{x}^*$.
    \item Problem classes: LP / NLP / MIP.
  \end{enumerate}

  \bigskip
  \textit{Next lecture: Topic of next lecture.}
\end{frame}
```

---

## Math Formatting Quick Reference

| Construct | LaTeX |
|---|---|
| Bold vector | `\mathbf{x}` |
| Real numbers | `\mathbb{R}^n` |
| Calligraphic set | `\mathcal{D}` |
| Optimal solution | `\mathbf{x}^*` |
| Optimal value | `p^*` |
| Inequality | `g_i(\mathbf{x}) \le 0` |
| Norm | `\|\mathbf{x}\|` |
| Infinity norm | `\|\mathbf{x}\|_\infty` |
| For all | `\forall\,\mathbf{x}\in\mathcal{D}` |
| Exists | `\exists\,\varepsilon > 0` |
| Infimum | `\inf_{\mathbf{x}\in\mathcal{D}}` |
| Open ball | `B(\mathbf{x}^*,\varepsilon)` |
| Aligned equations | `\begin{aligned}...\end{aligned}` inside `\[...\]` |
| Inline math | `$f(\mathbf{x})$` |

---

## LaTeX Special Character Escaping

When content comes from plain-text sources, escape these characters:

| Plain text | LaTeX |
|---|---|
| `&` | `\&` |
| `%` | `\%` |
| `$` (literal) | `\$` |
| `#` | `\#` |
| `_` outside math | `\_` |
| `^` outside math | `\^{}` |
| `~` | `\textasciitilde{}` |
| `\` | `\textbackslash{}` |
| `{` `}` | `\{` `\}` |
| `≤` | `\le` (in math mode) |
| `≥` | `\ge` |
| `→` | `\to` or `\rightarrow` |
| `∈` | `\in` |
| `∅` | `\varnothing` |
| `∞` | `\infty` |
| `‖` | `\|` (in math) |

---

## Compilation

```bash
python scripts/compile_latex.py path/to/file.tex [output_dir]
```

The script runs `pdflatex` **twice** automatically (required for correct page totals in footer).
Output: `file.pdf` in the same directory, or `output_dir` if specified.

---

## Complete Minimal Example

```latex
\documentclass{beamer}
\usetheme{Boadilla}
\definecolor{cuhkblue}{RGB}{51, 51, 179}
\setbeamercolor{structure}{fg=cuhkblue}
\setbeamercolor{palette primary}  {bg=cuhkblue!90!white, fg=white}
\setbeamercolor{palette secondary}{bg=cuhkblue!60!white, fg=white}
\setbeamercolor{palette tertiary} {bg=cuhkblue!40!white, fg=white}
\setbeamercolor{palette quaternary}{bg=cuhkblue!40!white, fg=white}
\usepackage{amsmath, amssymb, bm}
\title[MAT3007 $|$ Lecture 1]{MAT3007: Optimization}
\subtitle{Lecture 1: Introduction to Optimization}
\author[SDS, CUHK(SZ)]{Minghua Chen}
\institute[]{School of Data Science, CUHK(SZ)}
\date[]{}
\begin{document}
\begin{frame}\titlepage\end{frame}
\begin{frame}{Main Result}
  The optimal solution $\mathbf{x}^*$ satisfies $f(\mathbf{x}^*) \le f(\mathbf{x})$
  for all $\mathbf{x}\in\mathcal{D}$.
\end{frame}
\end{document}
```
