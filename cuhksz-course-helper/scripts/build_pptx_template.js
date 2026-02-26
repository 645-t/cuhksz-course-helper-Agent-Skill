"use strict";
const pptxgen = require("pptxgenjs");

// ── Design Tokens (CUHK-SZ MATH / Beamer style) ──────────────────────────────
const C = {
  cyan:     "4070B8",   // Slide titles — steel blue matching CUHK-SZ MATH template
  black:    "000000",   // Body text
  footerBg: "2D2D2D",   // Footer bar background
  white:    "FFFFFF",   // Footer text
  divBg:    "4070B8",   // Section-divider background (full slide)
};

// LAYOUT_WIDE = 13.33" × 7.5"
const W = 13.33, H = 7.5;
const FOOT_H = 0.27, FOOT_Y = H - FOOT_H;
const ML = 0.55, MR = 0.55, CW = W - ML - MR;
const FONT = "Cambria";         // Closest to Computer Modern on Windows
const COURSE = "MAT3007 | Lecture 1";
const N = 18;

// ── Helpers ───────────────────────────────────────────────────────────────────
function foot(slide, n) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: FOOT_Y, w: W, h: FOOT_H,
    fill: { color: C.footerBg }, line: { color: C.footerBg },
  });
  slide.addText("SSE, CUHK(SZ)", {
    x: 0.14, y: FOOT_Y, w: 3.5, h: FOOT_H,
    fontFace: FONT, fontSize: 9, color: C.white, valign: "middle", margin: 0,
  });
  slide.addText(COURSE, {
    x: (W - 5.5) / 2, y: FOOT_Y, w: 5.5, h: FOOT_H,
    fontFace: FONT, fontSize: 9, color: C.white,
    align: "center", valign: "middle", margin: 0,
  });
  slide.addText(`${n} / ${N}`, {
    x: W - 2.2, y: FOOT_Y, w: 2.1, h: FOOT_H,
    fontFace: FONT, fontSize: 9, color: C.white,
    align: "right", valign: "middle", margin: 0,
  });
}

// Cyan title, left-aligned, tight to top (matching Beamer style)
function cyanTitle(slide, text) {
  slide.addText(text, {
    x: ML, y: 0.12, w: CW, h: 0.62,
    fontFace: FONT, fontSize: 24, color: C.cyan,
    valign: "middle", margin: 0,
  });
}

// Body text block — array of run objects: {text, bold, italic, indent, space}
function bodyBlock(slide, runs, topY = 0.88) {
  const h = FOOT_Y - topY - 0.08;
  const arr = runs.map((r, i) => ({
    text: r.text,
    options: {
      bold:       !!r.bold,
      italic:     !!r.italic,
      breakLine:  i < runs.length - 1,
      indentLevel: r.indent || 0,
      paraSpaceAfter: r.space !== undefined ? r.space : 0,
    },
  }));
  slide.addText(arr, {
    x: ML, y: topY, w: CW, h,
    fontFace: FONT, fontSize: 16, color: C.black,
    valign: "top", margin: 0, lineSpacingMultiple: 1.4,
  });
}

// Section-divider: white text on cyan background
function sectionDivider(slide, num, title) {
  slide.background = { color: C.cyan };
  slide.addText(`Section ${num}`, {
    x: 0, y: 2.5, w: W, h: 0.65,
    fontFace: FONT, fontSize: 22, color: C.white,
    align: "center", valign: "middle",
  });
  slide.addText(title, {
    x: 0, y: 3.25, w: W, h: 1.0,
    fontFace: FONT, fontSize: 32, color: C.white,
    align: "center", valign: "middle", bold: true,
  });
}

// ── Presentation ──────────────────────────────────────────────────────────────
const pres = new pptxgen();
pres.layout  = "LAYOUT_WIDE";
pres.author  = "CUHKsz Course Helper";
pres.title   = "MAT3007 Optimization — Lecture 1";

// ── Slide 1: Title ─────────────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  s.addText("MAT3007: Optimization", {
    x: 0, y: 2.0, w: W, h: 0.85,
    fontFace: FONT, fontSize: 32, color: C.cyan,
    align: "center", bold: false,
  });
  s.addText("Lecture 1: Introduction to Optimization", {
    x: 0, y: 2.9, w: W, h: 0.55,
    fontFace: FONT, fontSize: 22, color: C.cyan,
    align: "center",
  });
  s.addText("Minghua Chen", {
    x: 0, y: 3.7, w: W, h: 0.4,
    fontFace: FONT, fontSize: 18, color: C.black, align: "center",
  });
  s.addText("School of Data Science, CUHK(SZ)   ·   Spring 2025", {
    x: 0, y: 4.15, w: W, h: 0.36,
    fontFace: FONT, fontSize: 14, color: C.black, align: "center",
  });
  foot(s, 1);
}

// ── Slide 2: Outline ──────────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Outline");
  bodyBlock(s, [
    { text: "1.  Optimization Mathematical Formulation",          space: 10 },
    { text: "2.  Classification of Optimization Problems",        space: 10 },
    { text: "3.  Solution Status",                                space: 10 },
    { text: "4.  The 3 Elements of an Optimization Problem",      space: 10 },
    { text: "5.  Global and Local Optimal Solutions",             space: 10 },
  ]);
  foot(s, 2);
}

// ── Slide 3: Section Divider 1 ────────────────────────────────────────────────
{
  const s = pres.addSlide();
  sectionDivider(s, "1", "Optimization Mathematical Formulation");
  foot(s, 3);
}

// ── Slide 4: Standard Form ────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Optimization Mathematical Formulation");
  bodyBlock(s, [
    { text: "The general optimization problem is written in standard form:", space: 12 },
    { text: "    minimize    f(x)",                                            space: 4  },
    { text: "    subject to  g_i(x) ≤ 0,   i = 1, …, m",                    space: 4  },
    { text: "                h_j(x) = 0,   j = 1, …, p",                    space: 16 },
    { text: "where:", space: 6 },
    { text: "   x ∈ R^n  is the decision variable vector  (n variables)",    space: 4  },
    { text: "   f : R^n → R  is the objective function",                      space: 4  },
    { text: "   g_i  are inequality constraints,   h_j  are equality constraints", space: 0 },
  ]);
  foot(s, 4);
}

// ── Slide 5: Key Definitions ──────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Feasibility and Optimality");
  bodyBlock(s, [
    { text: "Definition 1.1  (Feasible Point)", bold: true, space: 4 },
    { text: "A point x ∈ R^n is feasible if  g_i(x) ≤ 0  for all i  and  h_j(x) = 0  for all j.", space: 14 },
    { text: "Definition 1.2  (Feasible Region)", bold: true, space: 4 },
    { text: "D = { x ∈ R^n  :  g_i(x) ≤ 0,  h_j(x) = 0 }.", space: 14 },
    { text: "Definition 1.3  (Optimal Solution and Optimal Value)", bold: true, space: 4 },
    { text: "x* is an optimal solution if  x* ∈ D  and  f(x*) ≤ f(x)  for all x ∈ D.", space: 4 },
    { text: "The optimal value is  p* = f(x*).", space: 0 },
  ]);
  foot(s, 5);
}

// ── Slide 6: Example — Window and Door ───────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Example 1.1  (Window and Door Manufacturing)");
  bodyBlock(s, [
    { text: "A factory produces windows (x₁) and doors (x₂).  Formulate as an LP:", space: 12 },
    { text: "    maximize     6x₁ + 5x₂",           space: 4  },
    { text: "    subject to   x₁  +  x₂  ≤ 48    (wood, board-feet)",   space: 4  },
    { text: "                 10x₁ + 6x₂  ≤ 480   (labor, minutes)",    space: 4  },
    { text: "                 x₁          ≤ 40    (machine hours)",      space: 4  },
    { text: "                 x₁, x₂      ≥ 0",   space: 16 },
    { text: "Decision variables:   x₁ = no. of windows,   x₂ = no. of doors.", space: 4 },
    { text: "Objective:   maximize profit.    Constraints: resource limits.", space: 0 },
  ]);
  foot(s, 6);
}

// ── Slide 7: Section Divider 2 ────────────────────────────────────────────────
{
  const s = pres.addSlide();
  sectionDivider(s, "2", "Classification of Optimization Problems");
  foot(s, 7);
}

// ── Slide 8: Classification by Constraints ────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Constrained vs. Unconstrained");
  bodyBlock(s, [
    { text: "Unconstrained Problem:", bold: true, space: 4 },
    { text: "    minimize  f(x),   x ∈ R^n   — no feasibility restrictions.", space: 4 },
    { text: "    Examples: curve fitting, neural network training.", space: 16 },
    { text: "Constrained Problem:", bold: true, space: 4 },
    { text: "    minimize  f(x)   subject to constraints  g_i(x) ≤ 0,  h_j(x) = 0.", space: 4 },
    { text: "    Feasible region is a proper subset of R^n.", space: 4 },
    { text: "    Examples: resource allocation, portfolio optimization.", space: 0 },
  ]);
  foot(s, 8);
}

// ── Slide 9: Classification by Linearity ─────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Linear, Nonlinear, and Integer Programs");
  bodyBlock(s, [
    { text: "Linear Program (LP):", bold: true, space: 4 },
    { text: "    f, g_i, h_j  all linear.   Solvable in polynomial time (Simplex, Interior Point).", space: 14 },
    { text: "Nonlinear Program (NLP):", bold: true, space: 4 },
    { text: "    At least one of f, g_i, h_j  is nonlinear.", space: 4 },
    { text: "    Generally harder; may have multiple local optima.", space: 14 },
    { text: "Mixed-Integer Program (MIP):", bold: true, space: 4 },
    { text: "    Some or all variables restricted to integer values.", space: 4 },
    { text: "    NP-hard in general.", space: 0 },
  ]);
  foot(s, 9);
}

// ── Slide 10: Section Divider 3 ───────────────────────────────────────────────
{
  const s = pres.addSlide();
  sectionDivider(s, "3", "Solution Status");
  foot(s, 10);
}

// ── Slide 11: Solution Status ─────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Solution Status of an Optimization Problem");
  bodyBlock(s, [
    { text: "Every optimization problem falls into one of four categories:", space: 14 },
    { text: "(1)  Infeasible:     D = ∅   (no feasible point exists).", space: 8 },
    { text: "(2)  Unbounded:     inf f(x) = −∞   (objective has no finite lower bound).", space: 8 },
    { text: "(3)  Optimal value attained:     ∃ x* ∈ D  with  f(x*) = p*.", space: 8 },
    { text: "(4)  Optimal value not attained:     p* > −∞,  but no x* achieves f(x*) = p*.", space: 14 },
    { text: "Case (4) arises when the infimum is approached but never reached,", space: 4 },
    { text: "e.g., minimizing e^x over R — the infimum is 0 but is never attained.", space: 0 },
  ]);
  foot(s, 11);
}

// ── Slide 12: Section Divider 4 ───────────────────────────────────────────────
{
  const s = pres.addSlide();
  sectionDivider(s, "4", "The 3 Elements of an Optimization Problem");
  foot(s, 12);
}

// ── Slide 13: Three Elements ──────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "The 3 Elements Framework");
  bodyBlock(s, [
    { text: "Every optimization problem must specify three things:", space: 14 },
    { text: "(1)  Decision Variables", bold: true, space: 4 },
    { text: "       What quantities can we choose?   x = (x₁, …, xₙ) ∈ R^n.", space: 14 },
    { text: "(2)  Objective Function", bold: true, space: 4 },
    { text: "       What quantity do we minimize (or maximize)?   f : R^n → R.", space: 14 },
    { text: "(3)  Constraints", bold: true, space: 4 },
    { text: "       What restrictions must the decision satisfy?", space: 4 },
    { text: "       Inequalities  g_i(x) ≤ 0   and equalities  h_j(x) = 0.", space: 0 },
  ]);
  foot(s, 13);
}

// ── Slide 14: Example 1.2 — LP Formulation ───────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Example 1.2  (Data Summarization as LP)");
  bodyBlock(s, [
    { text: "Problem:  Given n data points {a₁, …, aₙ} ⊂ R^m,  find a representative x ∈ R^m.", space: 12 },
    { text: "Formulation (Chebyshev / L∞ center):", space: 6 },
    { text: "    minimize    max_{i}  ‖ x − aᵢ ‖_∞", space: 4 },
    { text: "    over        x ∈ R^m", space: 14 },
    { text: "Equivalent LP  (introduce slack t):", space: 6 },
    { text: "    minimize    t", space: 4 },
    { text: "    subject to  ‖ x − aᵢ ‖_∞  ≤  t,   i = 1, …, n;    t ≥ 0.", space: 0 },
  ]);
  foot(s, 14);
}

// ── Slide 15: Section Divider 5 ───────────────────────────────────────────────
{
  const s = pres.addSlide();
  sectionDivider(s, "5", "Global and Local Optimal Solutions");
  foot(s, 15);
}

// ── Slide 16: Global vs Local ─────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Global and Local Optimal Solutions");
  bodyBlock(s, [
    { text: "Definition 1.4  (Global Optimal Solution)", bold: true, space: 4 },
    { text: "x* ∈ D is a global optimal solution  if  f(x*) ≤ f(x)  for all x ∈ D.", space: 16 },
    { text: "Definition 1.5  (Local Optimal Solution)", bold: true, space: 4 },
    { text: "x* ∈ D is a local optimal solution  if ∃ ε > 0  such that", space: 4 },
    { text: "    f(x*) ≤ f(x)   for all  x ∈ D ∩ B(x*, ε),", space: 4 },
    { text: "where  B(x*, ε) = { x : ‖x − x*‖ < ε }  is an open ball.", space: 14 },
    { text: "Every global optimum is local.  The converse is false in general.", italic: true, space: 0 },
  ]);
  foot(s, 16);
}

// ── Slide 17: Remark — Infimum vs Minimum ────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Remark: Infimum vs. Minimum");
  bodyBlock(s, [
    { text: "The infimum  inf_{x∈D} f(x)  always exists (possibly −∞),", space: 4 },
    { text: "but may not be attained by any feasible point.", space: 14 },
    { text: "The minimum  min_{x∈D} f(x)  exists only when the infimum is attained.", space: 14 },
    { text: "Example:", bold: true, space: 4 },
    { text: "    minimize  x   subject to  x > 0.", space: 4 },
    { text: "    ⟹  inf = 0  (not attained).  The minimum does not exist.", space: 14 },
    { text: "Consequence:   A problem is solvable iff its optimal value is finite and attained.", italic: true, space: 0 },
  ]);
  foot(s, 17);
}

// ── Slide 18: Summary ────────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  cyanTitle(s, "Summary of Lecture 1");
  bodyBlock(s, [
    { text: "Key concepts covered today:", space: 12 },
    { text: "1.  Standard form:   min f(x)  s.t.  g(x) ≤ 0,  h(x) = 0.", space: 6 },
    { text: "2.  Feasible region, optimal solution, optimal value  p*.", space: 6 },
    { text: "3.  Problem classes:  LP / NLP / MIP,  constrained / unconstrained.", space: 6 },
    { text: "4.  Solution status:  infeasible · unbounded · optimal (attained / not).", space: 6 },
    { text: "5.  The 3 Elements framework:  variables · objective · constraints.", space: 6 },
    { text: "6.  Global vs. local optimal solutions.", space: 16 },
    { text: "Next lecture:   Convex sets and convex functions.", italic: true, space: 0 },
  ]);
  foot(s, 18);
}

// ── Write ────────────────────────────────────────────────────────────────────
const OUT = "MAT3007_Lecture1_L1_helper.pptx";
pres.writeFile({ fileName: OUT }).then(() => {
  console.log("Saved: " + OUT);
});
