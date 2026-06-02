import os
import re
import img2pdf

# Resolve paths dynamically relative to the script location
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)  # points to projects/pilot
img_dir = os.path.join(project_dir, "illustration", "painterly")
output_dir = os.path.join(project_dir, "output")
output_pdf = os.path.join(output_dir, "shhh_woof.pdf")

def generate_pdf():
    # Ensure illustration directory exists
    if not os.path.exists(img_dir):
        print(f"Error: Illustration directory not found at: {img_dir}")
        return

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Gather and sort all scene PNG files numerically (e.g., scene1_cat.png -> 1)
    img_files = [f for f in os.listdir(img_dir) if f.startswith("scene") and f.endswith(".png")]
    if not img_files:
        print(f"Error: No matching scene PNG files found in {img_dir}")
        return

    img_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    img_paths = [os.path.join(img_dir, f) for f in img_files]

    print(f"Found {len(img_paths)} illustrations to package:")
    for path in img_paths:
        print(f"  - {os.path.basename(path)}")

    # Convert images to PDF losslessly
    print(f"\nCompiling PDF using img2pdf to: {output_pdf} ...")
    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(img_paths))
        print("🎉 Success! PDF generated successfully.")
    except Exception as e:
        print(f"❌ Error during PDF compilation: {e}")

if __name__ == "__main__":
    generate_pdf()
