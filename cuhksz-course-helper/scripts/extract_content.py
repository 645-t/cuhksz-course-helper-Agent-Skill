"""
CUHKsz Course Helper - Content Extraction Script
Extracts structured content from PPTX files for processing.

Usage:
    python extract_content.py <input.pptx> [output.json]

Output JSON structure:
{
  "source_file": "filename.pptx",
  "slide_count": N,
  "slides": [
    {
      "index": 1,
      "type": "title",          // detected slide type
      "title": "...",
      "body_text": ["..."],
      "notes": "...",           // speaker notes
      "has_images": true/false,
      "layout_name": "...",
      "shapes": [...]           // raw shape info
    }
  ]
}
"""

import json
import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Pt
except ImportError:
    print("ERROR: python-pptx not installed. Run: pip install python-pptx")
    sys.exit(1)


SLIDE_TYPE_SIGNALS = {
    "title": ["course", "lecture", "instructor", "cuhk", "university"],
    "outline": ["outline", "agenda", "contents", "today", "topics"],
    "definition": ["definition", "def.", "let ", "denote", "we say"],
    "theorem": ["theorem", "lemma", "corollary", "proposition"],
    "proof": ["proof:", "proof of", "pf."],
    "example": ["example", "ex.", "illustration"],
    "exercise": ["exercise", "problem", "homework", "hw"],
    "remark": ["remark", "note:", "observation"],
    "algorithm": ["algorithm", "pseudocode", "procedure"],
    "section_divider": [],  # detected by layout/minimal content
    "summary": ["summary", "takeaway", "conclusion", "recap"],
    "reference": ["references", "bibliography", "citation"],
}


def detect_slide_type(slide, index):
    """Heuristically detect the slide type."""
    title_text = ""
    body_text = ""

    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        text = shape.text_frame.text.lower().strip()
        if shape.shape_type == 13:  # Picture
            continue
        if hasattr(shape, "placeholder_format") and shape.placeholder_format:
            ph_idx = shape.placeholder_format.idx
            if ph_idx == 0:  # Title placeholder
                title_text = text
            else:
                body_text += " " + text
        else:
            body_text += " " + text

    combined = title_text + " " + body_text

    # First slide heuristic
    if index == 0:
        return "title"

    # Check body content length - section divider = minimal content
    total_text = combined.strip()
    if len(total_text) < 30 and title_text:
        return "section_divider"

    # Signal-based detection
    for slide_type, signals in SLIDE_TYPE_SIGNALS.items():
        for signal in signals:
            if signal in combined:
                return slide_type

    return "content"  # generic fallback


def extract_text_from_shape(shape):
    """Extract text preserving basic structure."""
    if not shape.has_text_frame:
        return []
    lines = []
    for para in shape.text_frame.paragraphs:
        text = para.text.strip()
        if text:
            lines.append(text)
    return lines


def extract_pptx(input_path: str, output_path: str = None):
    prs = Presentation(input_path)
    slides_data = []

    for i, slide in enumerate(prs.slides):
        slide_info = {
            "index": i + 1,
            "type": detect_slide_type(slide, i),
            "title": "",
            "body_text": [],
            "notes": "",
            "has_images": False,
            "layout_name": slide.slide_layout.name if slide.slide_layout else "",
        }

        for shape in slide.shapes:
            # Check for images
            if shape.shape_type == 13:
                slide_info["has_images"] = True
                continue

            if shape.has_text_frame:
                if (hasattr(shape, "placeholder_format")
                        and shape.placeholder_format
                        and shape.placeholder_format.idx == 0):
                    slide_info["title"] = shape.text_frame.text.strip()
                else:
                    slide_info["body_text"].extend(extract_text_from_shape(shape))

        # Extract speaker notes
        if slide.has_notes_slide:
            notes_tf = slide.notes_slide.notes_text_frame
            if notes_tf:
                slide_info["notes"] = notes_tf.text.strip()

        slides_data.append(slide_info)

    result = {
        "source_file": str(Path(input_path).name),
        "slide_count": len(slides_data),
        "slides": slides_data,
    }

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Extracted {len(slides_data)} slides -> {output_path}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_content.py <input.pptx> [output.json]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    extract_pptx(input_file, output_file)
