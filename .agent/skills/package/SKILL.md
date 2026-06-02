---
name: package
description: Packages project illustration images into a single PDF document. Trigger this skill whenever the user wants to compile a PDF, package illustrations, export scene images to a PDF book, or generate a PDF file from a folder of images (e.g., painterly style, colorbook style).
---

# Package Skill

Use this skill to bundle a sequence of scene images into a single PDF document.

## Workflow

1. **Verify Dependencies**:
   * Execute the bundled setup script `scripts/setup.sh` to ensure `img2pdf` is installed.

2. **Locate Target Files**:
   * Determine the target folder of images. If the folder path is not specified or multiple styling folders exist (e.g., `illustration/painterly/`, `illustration/colorbook/`), prompt the user to confirm which folder to compile.
   * Verify the folder contains image files (PNG, JPG, JPEG).

3. **Compile PDF**:
   * Run the bundled Python script `scripts/package.py` passing:
     1. The path to the input directory.
     2. The path to the desired output PDF file (e.g., `projects/pilot/output/<book_name>.pdf`).

4. **Verify Output**:
   * Print a list of files packaged in order and provide the final path to the generated PDF.
