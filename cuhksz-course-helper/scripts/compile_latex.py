"""
CUHKsz Course Helper - LaTeX Compiler
Compiles a .tex file to PDF using pdflatex (run twice for correct page totals).

All intermediate build files (.aux, .log, .nav, .snm, .toc, .out) are isolated
in a temp subdirectory and cleaned up automatically after compilation.

Usage:
    python compile_latex.py <input.tex> [output_dir]
"""

import sys
import subprocess
import shutil
import tempfile
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

    # Create an isolated temp directory inside the tex file's folder.
    # Keeping it next to the .tex file ensures \includegraphics{images/...}
    # paths (relative to the tex directory) resolve correctly during compilation.
    tex_dir = tex_path.parent
    tmp_dir = Path(tempfile.mkdtemp(prefix="_cuhksz_build_", dir=tex_dir))

    try:
        args = [
            pdflatex,
            "-interaction=nonstopmode",
            f"-output-directory={tmp_dir}",
            tex_path.name,
        ]

        for pass_num in (1, 2):
            print(f"Compiling (pass {pass_num}): {tex_path.name}")
            r = subprocess.run(args, cwd=tex_dir, capture_output=True, text=True)
            if r.returncode != 0 and "Fatal error" in (r.stdout + r.stderr):
                log = tmp_dir / tex_path.with_suffix(".log").name
                if log.exists():
                    lines = log.read_text(encoding="utf-8", errors="ignore").splitlines()
                    for line in lines[-30:]:
                        if line.strip():
                            print(" ", line)
                print("ERROR: LaTeX compilation failed.")
                return None

        pdf_in_tmp = tmp_dir / tex_path.with_suffix(".pdf").name
        if not pdf_in_tmp.exists():
            print("ERROR: PDF not produced. Check pdflatex output above.")
            return None

        dest_dir = Path(output_dir) if output_dir else tex_dir
        dest = dest_dir / tex_path.with_suffix(".pdf").name
        shutil.copy2(pdf_in_tmp, dest)
        print(f"Done: {dest}")
        return str(dest)

    finally:
        # Always remove the temp build directory, even on failure
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compile_latex.py <input.tex> [output_dir]")
        sys.exit(1)

    result = compile_tex(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    sys.exit(0 if result else 1)
