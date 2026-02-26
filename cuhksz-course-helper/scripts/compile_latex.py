"""
CUHKsz Course Helper - LaTeX Compiler
Compiles a .tex file to PDF using pdflatex (run twice for correct page totals).

Usage:
    python compile_latex.py <input.tex> [output_dir]
"""

import sys
import subprocess
import shutil
from pathlib import Path

# Known pdflatex locations (Windows MiKTeX / TeX Live)
PDFLATEX_CANDIDATES = [
    # MiKTeX Windows (user install)
    r"C:\Users\10119\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex",
    # MiKTeX Windows (system install)
    r"C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex",
    r"C:\Program Files (x86)\MiKTeX\miktex\bin\pdflatex",
    # TeX Live (Linux/macOS)
    "/usr/bin/pdflatex",
    "/usr/local/bin/pdflatex",
    "/Library/TeX/texbin/pdflatex",
]


def find_pdflatex():
    if shutil.which("pdflatex"):
        return "pdflatex"
    for p in PDFLATEX_CANDIDATES:
        if Path(p).exists():
            return p
    return None


def compile_tex(tex_path: str, output_dir: str = None) -> str | None:
    tex_path = Path(tex_path).resolve()
    if not tex_path.exists():
        print(f"ERROR: File not found: {tex_path}")
        return None

    pdflatex = find_pdflatex()
    if not pdflatex:
        print("ERROR: pdflatex not found. Install MiKTeX (Windows) or TeX Live (Linux/macOS).")
        return None

    cwd = tex_path.parent
    args = [pdflatex, "-interaction=nonstopmode", tex_path.name]

    for pass_num in (1, 2):
        print(f"Compiling (pass {pass_num}): {tex_path.name}")
        r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
        if r.returncode != 0 and "Fatal error" in (r.stdout + r.stderr):
            # Show last few lines of log for diagnosis
            log = tex_path.with_suffix(".log")
            if log.exists():
                lines = log.read_text(encoding="utf-8", errors="ignore").splitlines()
                for line in lines[-30:]:
                    if line.strip():
                        print(" ", line)
            print("ERROR: LaTeX compilation failed.")
            return None

    pdf = tex_path.with_suffix(".pdf")
    if not pdf.exists():
        print("ERROR: PDF not produced. See .log file for details.")
        return None

    if output_dir:
        dest = Path(output_dir) / pdf.name
        pdf.rename(dest)
        print(f"Done: {dest}")
        return str(dest)

    print(f"Done: {pdf}")
    return str(pdf)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compile_latex.py <input.tex> [output_dir]")
        sys.exit(1)

    result = compile_tex(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    sys.exit(0 if result else 1)
