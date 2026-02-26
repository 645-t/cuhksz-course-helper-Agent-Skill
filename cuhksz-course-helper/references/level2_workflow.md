# Level 2 Workflow: Content Enhancement

## Step 1: Course Information Lookup

1. Extract course number from prompt or file (e.g., MAT3007, DDA3020)
2. Fetch: `https://www.cuhk.edu.cn/zh-hans/course`
   - Search by course code to get: full name, credit hours, brief description
3. If syllabus URL is available, fetch it for: weekly topics, textbook list, grading breakdown

## Step 2: Textbook Search Strategy

Priority order:

1. **Syllabus-listed textbook** (highest priority)
   - If user provides the textbook file, use it directly
   - If not, search by exact title + author on: Google Books, OpenLibrary, MIT OCW, course websites
   - Look for: free legal PDFs, official course pages, university library links

2. **Standard textbooks for the topic** (if no syllabus)
   - Search: "[course topic] standard textbook site:mit.edu OR site:stanford.edu OR site:coursera.org"
   - Cross-reference with similar CUHK-SZ course syllabi if accessible

3. **General web search** (fallback)
   - "[course topic] lecture notes PDF"
   - "[specific concept from slide] explanation site:wikipedia.org OR site:mathworld.wolfram.com"
   - For CS/ML: arXiv, Papers with Code, official documentation

4. **Academic search** (for proofs, theorems, rigorous sources)
   - Google Scholar, Semantic Scholar
   - Use only when precise mathematical/scientific claims need verification

## Step 3: Content Gap Analysis

For each slide in the original deck, assess:

| Issue Type | Trigger | Action |
|---|---|---|
| Unanswered question | "?" in red/colored text, "Think:", "Exercise:" with no answer | Add answer slide |
| Thin explanation | Single-line definition with no intuition | Add "Intuition" or "Why?" follow-up slide |
| Missing example | Theorem/formula with no worked example | Add example slide |
| Incomplete proof | "Proof: [omitted]" or truncated proof | Reconstruct from textbook |
| Jargon without definition | Technical term used without definition slide | Add definition slide before first use |
| Broken reference | "See Chapter X" with no further info | Pull content from identified textbook |

## Step 4: Augmentation Rules

- **Match slide type**: New slides must use the same slide type as adjacent original slides
- **Match language**: Use same language as the slide being supplemented
- **AI marker required**: All added slides must have italic AI Accent Color text + `[Helper]` tag
- **Cite sources**: Include a small gray citation at slide bottom (e.g., "[Ref: Boyd & Vandenberghe, Ch.3]")
- **No content deletion**: Never remove or replace original content; only add
- **Conservative augmentation**: Prefer adding 1 clear slide over 3 rushed ones

## Step 5: Reference Answer Generation

Triggered when input material type is: exam paper, homework, problem set, tutorial worksheet.

### Answer File Structure
1. First slide: Disclaimer (required, see SKILL.md)
2. For each question: reproduce question in original format, then answer block below
3. Answer style by material type:
   - Math proofs: show key steps, not full verbosity
   - Multiple choice: letter + 1-sentence justification
   - Short answer: 2-5 sentences
   - Long essay/report: outline form with key points
4. Confidence indicator per answer:
   - High: textbook directly answers this
   - Medium: inferred from related content
   - Low: general reasoning, verify carefully

## Step 6: Output Report

After generating files, always provide a summary:

```
[CUHKsz Course Helper - Run Report]
Course: [code] [name]
Level: L2
Template: [CS/MATH/STATS]
Input: [filename]

Changes:
  - Slides reformatted: X
  - Typos flagged: X (list them, awaiting confirmation)
  - AI slides added: X
  - Sources used: [list]

Output files:
  - [filename]_L2_helper.pptx
  - [filename]_L2_helper.pdf
  - [filename]_L2_answers_helper.pptx (if applicable)
```
