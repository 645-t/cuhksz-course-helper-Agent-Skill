"""
CUHKsz Course Helper - Dependency Checker & Auto-Installer

Checks all required dependencies and installs any that are missing:
  - Python packages: python-pptx, pymupdf
  - LaTeX distribution: pdflatex (MiKTeX on Windows, MacTeX on macOS, TeX Live on Linux)

Usage:
    python ensure_deps.py

Returns exit code 0 if all dependencies are satisfied after the run, 1 otherwise.
"""

import sys
import subprocess
import shutil
import platform
from pathlib import Path


# ── Python packages ───────────────────────────────────────────────────────────
# (pip_name, import_name)
PYTHON_PACKAGES = [
    ("python-pptx", "pptx"),
    ("pymupdf",     "fitz"),
]

# ── pdflatex search paths (same as compile_latex.py) ─────────────────────────
PDFLATEX_CANDIDATES = [
    r"C:\Users\10119\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex",
    r"C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex",
    r"C:\Program Files (x86)\MiKTeX\miktex\bin\pdflatex",
    "/usr/bin/pdflatex",
    "/usr/local/bin/pdflatex",
    "/Library/TeX/texbin/pdflatex",
]


# ─────────────────────────────────────────────────────────────────────────────
def _pip_install(pip_name: str) -> bool:
    """Install a Python package via pip. Returns True on success."""
    print(f"  Installing {pip_name} ...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "--quiet", pip_name],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print(f"  OK: {pip_name} installed.")
        return True
    print(f"  FAILED: {result.stderr.strip()}")
    return False


def check_python_packages() -> bool:
    """Check and install required Python packages. Returns True if all OK."""
    import importlib
    all_ok = True
    for pip_name, import_name in PYTHON_PACKAGES:
        try:
            importlib.import_module(import_name)
            print(f"  OK: {pip_name}")
        except ImportError:
            print(f"  MISSING: {pip_name}")
            if not _pip_install(pip_name):
                all_ok = False
    return all_ok


# ─────────────────────────────────────────────────────────────────────────────
def find_pdflatex() -> str | None:
    """Return path to pdflatex executable, or None if not found."""
    if shutil.which("pdflatex"):
        return shutil.which("pdflatex")
    for p in PDFLATEX_CANDIDATES:
        if Path(p).exists():
            return p
    return None


def _install_latex_windows() -> bool:
    """Install MiKTeX on Windows via winget. Returns True on success."""
    if not shutil.which("winget"):
        print("  winget not available. Download MiKTeX manually from https://miktex.org/download")
        return False
    print("  Installing MiKTeX via winget (this may take several minutes) ...")
    result = subprocess.run(
        ["winget", "install", "--id", "MiKTeX.MiKTeX", "-e", "--silent", "--accept-package-agreements", "--accept-source-agreements"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print("  OK: MiKTeX installed. You may need to open a new terminal for pdflatex to be on PATH.")
        return True
    # winget sometimes returns non-zero even on success (e.g. already installed)
    if "successfully installed" in result.stdout.lower() or "no applicable upgrade" in result.stdout.lower():
        print("  OK: MiKTeX already installed or just installed.")
        return True
    print(f"  winget output: {result.stdout.strip()}")
    print("  If installation failed, download MiKTeX from https://miktex.org/download")
    return False


def _install_latex_macos() -> bool:
    """Install BasicTeX on macOS via Homebrew. Returns True on success."""
    if shutil.which("brew"):
        print("  Installing BasicTeX via Homebrew (this may take a few minutes) ...")
        result = subprocess.run(
            ["brew", "install", "--cask", "basictex"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print("  OK: BasicTeX installed. Run: sudo tlmgr update --self && sudo tlmgr install collection-latexextra")
            return True
        print(f"  Homebrew error: {result.stderr.strip()}")
    print("  Download MacTeX from https://www.tug.org/mactex/ or install Homebrew first: https://brew.sh")
    return False


def _install_latex_linux() -> bool:
    """Install TeX Live on Linux. Returns True on success."""
    # Try apt (Debian/Ubuntu)
    if shutil.which("apt-get"):
        print("  Installing texlive-full via apt-get (this may take several minutes) ...")
        result = subprocess.run(
            ["sudo", "apt-get", "install", "-y", "texlive-full"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print("  OK: texlive-full installed.")
            return True
        # Try smaller package as fallback
        print("  Trying texlive-latex-extra instead ...")
        result2 = subprocess.run(
            ["sudo", "apt-get", "install", "-y", "texlive-latex-extra"],
            capture_output=True, text=True,
        )
        if result2.returncode == 0:
            print("  OK: texlive-latex-extra installed.")
            return True
    # Try dnf (Fedora/RHEL)
    if shutil.which("dnf"):
        print("  Installing texlive via dnf ...")
        result = subprocess.run(
            ["sudo", "dnf", "install", "-y", "texlive-scheme-full"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print("  OK: texlive installed.")
            return True
    print("  Could not auto-install LaTeX. Install manually: https://www.tug.org/texlive/")
    return False


def check_pdflatex() -> bool:
    """Check and install pdflatex. Returns True if available after check."""
    path = find_pdflatex()
    if path:
        print(f"  OK: pdflatex found at {path}")
        return True

    print("  MISSING: pdflatex not found.")
    system = platform.system()
    if system == "Windows":
        return _install_latex_windows()
    elif system == "Darwin":
        return _install_latex_macos()
    else:
        return _install_latex_linux()


# ─────────────────────────────────────────────────────────────────────────────
def main():
    print("=== CUHKsz Course Helper — Dependency Check ===\n")

    print("[1/2] Python packages:")
    py_ok = check_python_packages()

    print("\n[2/2] LaTeX (pdflatex):")
    latex_ok = check_pdflatex()

    print()
    if py_ok and latex_ok:
        print("All dependencies satisfied. Ready to use.")
        sys.exit(0)
    else:
        if not py_ok:
            print("WARNING: Some Python packages could not be installed.")
        if not latex_ok:
            print("WARNING: pdflatex is not available. PDF compilation will fail.")
            print("         Install a LaTeX distribution and re-run this script.")
        sys.exit(1)


if __name__ == "__main__":
    main()
