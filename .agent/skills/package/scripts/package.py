#!/usr/bin/env python3
import os
import re
import sys
import img2pdf

def main():
    if len(sys.argv) < 3:
        print("Usage: package.py <input_dir> <output_pdf>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_pdf = sys.argv[2]

    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        sys.exit(1)

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_pdf)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Filter image assets
    valid_exts = ('.png', '.jpg', '.jpeg')
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(valid_exts)]
    if not files:
        print(f"Error: No image assets (.png, .jpg, .jpeg) found in: {input_dir}")
        sys.exit(1)

    # Sort numerically based on numeric indices in filenames (e.g., scene2 -> 2)
    def get_sort_key(filename):
        numbers = re.findall(r'\d+', filename)
        return int(numbers[0]) if numbers else filename

    files.sort(key=get_sort_key)
    img_paths = [os.path.join(input_dir, f) for f in files]

    print(f"Found {len(img_paths)} illustrations to compile in order:")
    for path in img_paths:
        print(f"  - {os.path.basename(path)}")

    print(f"\nPackaging to PDF: {output_pdf} ...")
    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(img_paths))
        print("🎉 PDF package created successfully!")
    except Exception as e:
        print(f"❌ Error during PDF creation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
