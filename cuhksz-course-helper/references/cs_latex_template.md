# CS Template — LaTeX Beamer Reference

Use this file to write `.tex` files that match the CUHK-SZ CS template exactly.
After writing the `.tex`, compile with `scripts/compile_latex.py`.

---

## Preamble (copy verbatim for every CS slide deck)

```latex
\documentclass{beamer}   % default 4:3 aspect ratio matches CS template
\usetheme{Boadilla}

% ── Verified colors (extracted from CS template PDF vector data) ─────────────
% Structure/frametitle: #3333B2 = RGB(51,51,178)
% Footer primary   (left):   cuhkblue           = #3333B2
% Footer secondary (center): cuhkblue!75!black  = #262685
% Footer tertiary  (right):  cuhkblue!50!black  = #191959
\definecolor{cuhkblue}{RGB}{51, 51, 178}
\setbeamercolor{structure}{fg=cuhkblue}
\setbeamercolor{palette primary}  {bg=cuhkblue,           fg=white}
\setbeamercolor{palette secondary}{bg=cuhkblue!75!black,  fg=white}
\setbeamercolor{palette tertiary} {bg=cuhkblue!50!black,  fg=white}
\setbeamercolor{palette quaternary}{bg=cuhkblue!50!black, fg=white}

% ── Full-width colored frametitle bar ────────────────────────────────────────
\setbeamercolor{frametitle}{bg=cuhkblue, fg=white}
\setbeamertemplate{frametitle}{
  \nointerlineskip
  \begin{beamercolorbox}[wd=\paperwidth, ht=0.55cm, dp=0.2cm, leftskip=0.5cm]{frametitle}
    \usebeamerfont{frametitle}\insertframetitle
  \end{beamercolorbox}
}

% ── Suppress navigation symbols ──────────────────────────────────────────────
\setbeamertemplate{navigation symbols}{}

% ── Round bullet dots for all itemize levels ─────────────────────────────────
\setbeamertemplate{itemize item}{\scriptsize$\bullet$}
\setbeamertemplate{itemize subitem}{\scriptsize$\bullet$}
\setbeamertemplate{itemize subsubitem}{\scriptsize$\bullet$}

% ── Math + tikz packages ─────────────────────────────────────────────────────
\usepackage{amsmath, amssymb, bm}
\usepackage{tikz}

% ── Full-width rounded title box via tikz overlay ────────────────────────────
% anchor=north west at current page.north west guarantees left-to-right coverage.
% minimum width=\paperwidth ensures edge-to-edge width.
\setbeamertemplate{title page}{
  \begin{tikzpicture}[remember picture, overlay]
    \node[
      rounded corners=8pt,
      fill=cuhkblue,
      inner xsep=1.2cm,
      inner ysep=0.7em,
      minimum width=\paperwidth,
      text width=\dimexpr\paperwidth-2.4cm\relax,
      align=center,
      anchor=north west,
    ] at ([yshift=-1.8cm]current page.north west) {
      {\large\bfseries\color{white}\inserttitle}\\[0.35em]
      {\large\bfseries\color{white!85!black}\insertsubtitle}
    };
  \end{tikzpicture}
  \vspace{4.2cm}
  \begin{center}
    {\usebeamerfont{author}\insertauthor}\\[0.25em]
    {\small\insertinstitute}\\[0.7em]
    {\usebeamerfont{date}\insertdate}
  \end{center}
}

% ── Metadata → footer: left=short author | center=short title | right=page ──
\title[COURSE $|$ Lecture N]{COURSE: Full Title}
\subtitle{Lecture N: Lecture Title}
\author[Name, SDS, CUHK-SZ]{Professor Name}
\institute[]{School of Data Science, CUHK-SZ}   % MUST use [] empty short form
\date{Date}

\begin{document}
% ... frames here ...
\end{document}
```

**Critical rules:**
- `\author[SHORT]{}` — SHORT appears in footer left
- `\institute[]{}` — empty `[]` prevents "(full name)" appending in footer
- `\title[SHORT]{}` — SHORT appears in footer center
- `\date{Date}` — date shown in footer right (unlike MATH which suppresses it)
- Palette mixes with **black** (NOT white) for the darker footer gradient

---

## Frame Patterns by Slide Type

### title — Title page

```latex
\begin{frame}
  \titlepage
\end{frame}
```

---

### outline — Agenda slide

```latex
\begin{frame}{Outlines}
  \begin{enumerate}
    \item Topic One
    \item Topic Two
      \begin{itemize}
        \item Sub-topic A
        \item Sub-topic B
      \end{itemize}
    \item Topic Three
  \end{enumerate}
\end{frame}
```

---

### section_divider — Shaded TOC at section start

This is the CS section break style: all sections shown, current one highlighted, others faded.

**IMPORTANT**: Every `\section{}` must be followed by at least one `\begin{frame}` for it to appear in the TOC.

```latex
% Place \section{} before the divider frame:
\section{Section Title}

\begin{frame}
  \tableofcontents[currentsection,
    sectionstyle=show/shaded,
    subsectionstyle=show/shaded/shaded]
\end{frame}
```

For sections without content in a test file, add a placeholder frame:
```latex
\section{Another Topic}
\begin{frame}[noframenumbering]{Another Topic}
  \textit{(Content not shown in this excerpt.)}
\end{frame}
```

---

### content — Regular content slide

```latex
\begin{frame}{Frame Title}
  Introductory sentence.
  \begin{itemize}
    \item First point with \textcolor{cuhkblue}{highlighted term}.
    \item Second point:
      \begin{itemize}
        \item Sub-point A.
        \item Sub-point B.
      \end{itemize}
    \item Third point.
  \end{itemize}
\end{frame}
```

---

### content with math — Slide with equations

```latex
\begin{frame}{Frame Title}
  A \textbf{key concept} is defined as:
  \begin{itemize}
    \item Each \textbf{node} represents a test on an attribute.
    \item Each \textbf{leaf} holds a class label.
  \end{itemize}

  \medskip

  \textbf{Formula Name} for parameter $X$:
  \[
    F(x) = \sum_{i} p_i \log_2 p_i
  \]
  where $p_i$ is the probability of class $i$.
\end{frame}
```

---

### algorithm — Code or pseudocode slide

```latex
\usepackage{listings}  % add to preamble
...
\begin{frame}{Algorithm: Name}
  \textbf{Input:} dataset $D$, attributes $A$\\
  \textbf{Output:} decision tree $T$
  \medskip
  \begin{enumerate}
    \item If $D$ is pure, return leaf node.
    \item Select best attribute $a^* \in A$.
    \item Split $D$ by $a^*$ into subsets $D_1, \ldots, D_k$.
    \item Recurse on each subset.
  \end{enumerate}
\end{frame}
```

---

### summary — Summary slide

```latex
\begin{frame}{Summary}
  \begin{enumerate}
    \item \textbf{Key concept:}\quad brief recap.
    \item Important formula: $F(x) = \ldots$
    \item Next lecture: Topic of next lecture.
  \end{enumerate}
\end{frame}
```

---

## Color Reference

| Element | Color | Value |
|---|---|---|
| Structure / frametitle bg | `#3333B2` | `RGB(51,51,178)` |
| Footer left | `cuhkblue` | `#3333B2` |
| Footer center | `cuhkblue!75!black` | `#262685` |
| Footer right | `cuhkblue!50!black` | `#191959` |
| AI Accent Color | Amber | `#B8860B` |

**Note**: Palette mixes with `black` (CS style), producing a darker gradient footer.
Compare to MATH template which mixes with `white`.

---

## Compilation

```bash
python scripts/compile_latex.py path/to/file.tex [output_dir]
```

Run `pdflatex` **twice** for correct total frame count in footer.

---

## Complete Minimal Example

```latex
\documentclass{beamer}
\usetheme{Boadilla}
\definecolor{cuhkblue}{RGB}{51, 51, 178}
\setbeamercolor{structure}{fg=cuhkblue}
\setbeamercolor{palette primary}  {bg=cuhkblue,           fg=white}
\setbeamercolor{palette secondary}{bg=cuhkblue!75!black,  fg=white}
\setbeamercolor{palette tertiary} {bg=cuhkblue!50!black,  fg=white}
\setbeamercolor{palette quaternary}{bg=cuhkblue!50!black, fg=white}
\setbeamercolor{frametitle}{bg=cuhkblue, fg=white}
\setbeamertemplate{frametitle}{
  \nointerlineskip
  \begin{beamercolorbox}[wd=\paperwidth, ht=0.55cm, dp=0.2cm, leftskip=0.5cm]{frametitle}
    \usebeamerfont{frametitle}\insertframetitle
  \end{beamercolorbox}
}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{itemize item}{\scriptsize$\bullet$}
\setbeamertemplate{itemize subitem}{\scriptsize$\bullet$}
\usepackage{amsmath, amssymb, bm}
\usepackage{tikz}
\setbeamertemplate{title page}{
  \begin{tikzpicture}[remember picture, overlay]
    \node[rounded corners=8pt, fill=cuhkblue, inner xsep=1.2cm, inner ysep=0.7em,
      minimum width=\paperwidth, text width=\dimexpr\paperwidth-2.4cm\relax,
      align=center, anchor=north west]
      at ([yshift=-1.8cm]current page.north west) {
        {\large\bfseries\color{white}\inserttitle}\\[0.35em]
        {\large\bfseries\color{white!85!black}\insertsubtitle}
      };
  \end{tikzpicture}
  \vspace{4.2cm}
  \begin{center}
    {\usebeamerfont{author}\insertauthor}\\[0.25em]
    {\small\insertinstitute}\\[0.7em]
    {\usebeamerfont{date}\insertdate}
  \end{center}
}
\title[DDA3020 $|$ Lecture 1]{DDA3020 Machine Learning}
\subtitle{Lecture 1: Introduction}
\author[Zhou, SDS, CUHK-SZ]{Juexiao Zhou}
\institute[]{School of Data Science, CUHK-SZ}
\date{Sept 2, 2025}
\begin{document}
\begin{frame}\titlepage\end{frame}
\section{Topic One}
\begin{frame}
  \tableofcontents[currentsection, sectionstyle=show/shaded]
\end{frame}
\begin{frame}{First Slide}
  Content here with \textcolor{cuhkblue}{highlighted terms}.
\end{frame}
\end{document}
```
