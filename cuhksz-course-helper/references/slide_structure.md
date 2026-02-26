# Slide Structure Patterns

## Slide Type Detection Rules

Use these rules to classify each slide during extraction:

| Slide Type | Detection Signals |
|---|---|
| `title` | First slide, large centered text, instructor/date present |
| `outline` | "Outline", "Agenda", "Contents", "Today's Topics", checkbox bullets |
| `section_divider` | Single large text, minimal content, separates major sections |
| `definition` | "Definition", "Def.", boxed text, formal "Let X be..." phrasing |
| `theorem` | "Theorem", "Lemma", "Corollary", "Proposition" label |
| `proof` | "Proof:", "Proof of...", ends with QED or square |
| `example` | "Example", "Ex.", numbered example, worked solution |
| `exercise` | "Exercise", "Problem", "HW", blank answer space |
| `remark` | "Remark", "Note", "Observation", italic or indented block |
| `algorithm` | Pseudocode, code block, numbered steps with indentation |
| `diagram` | Image-heavy, figure caption present, minimal prose |
| `comparison` | Two-column layout, versus/comparison language |
| `formula` | Equation-dominant, derivation steps, numbered equations |
| `review` | "Review", "Recall", "Last time..." at beginning of deck |
| `summary` | "Summary", "Key Takeaways", at end of deck |
| `reference` | "References", citation list, bibliography |

## Slide Layout Templates

### title
```
[Full-width header or centered block]
  COURSE NUMBER - COURSE NAME
  LECTURE N: Topic Title

  Instructor Name
  School of [X], CUHK(SZ)
  Date
  [CUHK-SZ Logo]
```

### outline
```
[Slide title: "Outline" or "Today"]
  [ ] Section 1 - Topic A
  [ ] Section 2 - Topic B
  [ ] Section 3 - Topic C
```

### definition (MATH/STATS)
```
[Slide title]
+-----------------------------------------+
| Definition X.X (Name if applicable)     |
|                                         |
| Formal statement in mathematical        |
| notation. Let X in R^n such that...     |
+-----------------------------------------+
  Optional: intuitive explanation below box
```

### theorem (MATH)
```
[Slide title]
+==========================================+
| Theorem X.X                             |
| Statement of theorem                    |
+==========================================+
  Proof:
    Step 1: ...
    Step 2: ...
    QED []
```

### example
```
[Slide title: "Example X.X" or "Example: Topic"]
  Problem statement or setup.

  Solution:
    Step 1: ...
    Step 2: ...
    Result: [boxed or bold]
```

### section_divider
```
[Full-slide accent color background]
  SECTION N
  Section Title
```

### algorithm (CS)
```
[Slide title]
+-- Algorithm Name -------------------------+
| Input: ...                               |
| Output: ...                              |
|                                          |
|   1: Initialize ...                      |
|   2: for i = 1 to n do                  |
|   3:   ...                               |
|   4: return ...                          |
+------------------------------------------+
  Time complexity: O(...)
```

## Content Density Guidelines

- Max ~8 bullet points per slide
- Max ~6 lines of displayed math per slide
- Max ~20 lines of code per slide (split if longer)
- If a slide is empty or has only a title, flag for user review
- If text overflows, split into continuation slide with "(Cont.)" suffix
