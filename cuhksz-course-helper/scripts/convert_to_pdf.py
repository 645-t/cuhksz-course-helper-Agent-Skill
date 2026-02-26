"""
CUHKsz Course Helper - PDF Converter
Converts PPTX to PDF using available system tools.

Usage:
    python convert_to_pdf.py <input.pptx> [output.pdf]

Methods tried in order:
    1. Microsoft PowerPoint COM (Windows only, best quality)
    2. LibreOffice (cross-platform)
    3. Falls back with instructions if neither available
"""

import sys
import subprocess
from pathlib import Path


def convert_via_powerpoint_com(pptx_path: str, pdf_path: str) -> bool:
    """Convert using PowerPoint COM automation (Windows, best quality)."""
    try:
        import comtypes.client
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        powerpoint.Visible = 1
        deck = powerpoint.Presentations.Open(str(Path(pptx_path).resolve()))
        deck.SaveAs(str(Path(pdf_path).resolve()), 32)  # 32 = ppSaveAsPDF
        deck.Close()
        powerpoint.Quit()
        return True
    except Exception as e:
        print(f"  PowerPoint COM failed: {e}")
        return False


def convert_via_libreoffice(pptx_path: str, output_dir: str) -> bool:
    """Convert using LibreOffice headless mode."""
    commands = [
        ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", output_dir, pptx_path],
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", output_dir, pptx_path],
    ]
    for cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    return False


def convert_pptx_to_pdf(pptx_path: str, pdf_path: str = None) -> str:
    pptx_path = str(Path(pptx_path).resolve())
    if not pdf_path:
        pdf_path = str(Path(pptx_path).with_suffix(".pdf"))

    print(f"Converting: {pptx_path}")
    print(f"Output:     {pdf_path}")

    # Try PowerPoint COM first (Windows)
    print("Trying PowerPoint COM...")
    if convert_via_powerpoint_com(pptx_path, pdf_path):
        print(f"Done (PowerPoint COM): {pdf_path}")
        return pdf_path

    # Try LibreOffice
    print("Trying LibreOffice...")
    output_dir = str(Path(pdf_path).parent)
    if convert_via_libreoffice(pptx_path, output_dir):
        # LibreOffice names the file based on input filename
        expected = Path(output_dir) / (Path(pptx_path).stem + ".pdf")
        if expected.exists() and str(expected) != pdf_path:
            expected.rename(pdf_path)
        print(f"Done (LibreOffice): {pdf_path}")
        return pdf_path

    # Neither method worked
    print("\nERROR: Could not convert to PDF automatically.")
    print("Manual options:")
    print("  1. Open the PPTX in Microsoft PowerPoint > File > Export > PDF")
    print("  2. Install LibreOffice from https://www.libreoffice.org/")
    print("  3. Install comtypes: pip install comtypes")
    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_pdf.py <input.pptx> [output.pdf]")
        sys.exit(1)

    pptx = sys.argv[1]
    pdf = sys.argv[2] if len(sys.argv) > 2 else None
    result = convert_pptx_to_pdf(pptx, pdf)
    sys.exit(0 if result else 1)
