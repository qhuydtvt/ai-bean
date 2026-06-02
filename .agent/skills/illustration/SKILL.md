---
name: illustration
description: Generate, plan, and refine illustrations for stories, texts, or books using the generate_image tool. Supports parsing single/multiple target images and single/multiple art styles (e.g. Painterly, Coloring Book/Sheet B&W outlines, Flat Vector, Cartoon, Watercolor, Whimsical, Wimmelbuch, Mixed Media). Organizes outputs in style-specific folders within the target directory. Apply professional styling techniques and print preparation rules (bleed zones, safe margins). Create supplementary artifacts (character sheets, color palettes, layout guides) as needed. Make sure to use this skill whenever the user mentions illustrations, scene images, drawing, character designs, or wants to generate coloring book sheets/coloring pages, even if they do not explicitly ask for an 'illustration'.
---

# Illustration Skill

Use this skill to parse, plan, and guide the creation of digital illustrations and coloring pages in various art styles using the `generate_image` tool, organizing outputs into style-specific folders.

---

## Art Styles & Styling Rules

Before generating any illustrations, parse the input to determine if the user has requested one or more **ArtStyles**. If multiple styles are requested, organize the final files into style-specific directories under the target folder: `<target_folder>/<style_name>/` (e.g., `projects/pilot/illustration/painterly/`, `projects/pilot/illustration/coloring_book/`).

Use the following standard snake_case directory names for each style:
- `painterly` (for Painterly - Full Color or Painterly - Monochrome)
- `coloring_book` (for Coloring Book / Sheet outlines)
- `flat_vector` (for Flat Vector)
- `cartoon_playful` (for Cartoon / Playful)
- `watercolor` (for Watercolor)
- `whimsical_fantasy` (for Whimsical & Fantasy)
- `wimmelbuch` (for Wimmelbuch / Hidden Picture)
- `mixed_media` (for Mixed Media)

Adjust prompt generation and visual rules according to each selected style:

### 1. Painterly
*   **Full Color (Default)**: Sculpt forms using color blocks and light rather than outlines. Use textured wet oil brushstrokes, volumetric shading (deep cool blue-violet shadows, never pure black/grey), and warm golden highlights. Directory name: `painterly`
*   **Monochrome**: Render the same painterly textures, brushwork, volume, and lighting in grayscale. Use black ink washes, charcoal textures, rich gray tones, and white highlights. Useful for advanced grayscale coloring sheets. Directory name: `painterly`

### 2. Coloring Book / Coloring Sheet
*   **Prompt Instructions**: Specify "clean, crisp, black-and-white vector-style line art outlines".
*   **Styling Rules**:
    *   Strictly NO shading, NO gray values, and NO colors.
    *   Use "pure white fills and background, with sharp solid black outline borders".
    *   Ensure simple, clear shapes designed for children (Ages 2-5) to color in.
    *   Directory name: `coloring_book`

### 3. Flat Vector Illustration
*   **Prompt Instructions**: Use keywords like "flat vector illustration", "minimalist flat design", "clean geometric shapes", "bold solid colors".
*   **Styling Rules**:
    *   No textures, gradient fills, or volumetric shading.
    *   Use clean lines, sharp color blocks, and geometric simplicity.
    *   Directory name: `flat_vector`

### 4. Cartoon / Playful
*   **Prompt Instructions**: Use keywords like "playful cartoon style", "expressive characters", "bold outlines", "bright vibrant colors".
*   **Styling Rules**:
    *   Use bold, clean ink outline borders.
    *   Apply soft cel-shading or simple gradients.
    *   Emphasize friendly, exaggerated character expressions.
    *   Directory name: `cartoon_playful`

### 5. Watercolor
*   **Prompt Instructions**: Use keywords like "watercolor illustration", "delicate color washes", "wet-on-wet watercolor technique", "translucent overlays".
*   **Styling Rules**:
    *   Incorporate organic paper textures, soft bleeding edges, and translucent layering of pigments.
    *   Keep the look delicate, light, and artistic.
    *   Directory name: `watercolor`

### 6. Whimsical & Fantasy
*   **Prompt Instructions**: Use keywords like "dreamy whimsical illustration", "magical glowing elements", "fairytale atmosphere", "soft focal glows".
*   **Styling Rules**:
    *   Incorporate soft rim lighting, magical dust/sparks, and fairytale-inspired settings.
    *   Use a pastel or dreamy color palette with glowing light sources.
    *   Directory name: `whimsical_fantasy`

### 7. Wimmelbuch (Hidden Picture / Busy Book)
*   **Prompt Instructions**: Use keywords like "highly detailed Wimmelbuch style", "busy book layout", "micro-actions", "crowded detailed scene".
*   **Styling Rules**:
    *   Densely populate the scene with multiple characters and active micro-scenes.
    *   Keep all background and foreground elements sharp and clear (avoid heavy depth-of-field blur).
    *   Ensure the environment is highly detailed with small visual elements to discover.
    *   Directory name: `wimmelbuch`

### 8. Mixed Media
*   **Prompt Instructions**: Use keywords like "mixed media illustration", "textured paper collage", "cutout art", "stamping".
*   **Styling Rules**:
    *   Combine digital painting with physical textures (e.g. fabric patterns, newsprint, ink stamps).
    *   Emphasize paper layers, subtle drop shadows under cutouts, and rich tactile textures.
    *   Directory name: `mixed_media`

## Key Principles

The following principles provide a foundation for professional illustration output. Principles 1, 2, and 3 apply primarily to **Painterly** styles and should be adapted or bypassed for other styles (e.g., line-art coloring pages, flat vectors).

### 1. Form-Thinking over Line-Thinking (Painterly Style)
Do not describe scene elements in terms of outlines, hard edges, or simple flat colors. Instead:
- Emphasize volume, mass, and color blocks.
- Focus on light and form sculpting (describing light falling on objects, highlights carving out shapes).

### 2. Digital Brushwork & Texture (Painterly/Watercolor Styles)
Replicate professional digital painting techniques (e.g., Photoshop, Procreate brush dynamics) in prompts:
- Describe textures such as "visible canvas textures", "textured oil/wet brushstrokes", and "soft blended transitions".
- Incorporate concepts of the Smudge and Blur tools: "soft, blended gradients for skin and backgrounds", and "softly smudged edges to blend details naturally into the main form".

### 3. Volumetric Shading (Painterly/Fantasy Styles)
Avoid flat black or dark grey shadows.
- Specify shadows using rich, cool tones (e.g., "cool blue and violet shadow undertones in skin and fabrics", "warm golden highlights contrasting with cool-toned shadows").
- Use dodge/burn lighting terminology: "cinematic volumetric lighting", "rim lighting highlighting silhouettes", and "contrasting highlights that bring out the three-dimensional depth".

### 4. Composition & Bleed (Universal Style Principle)
For storybooks and printing:
- Keep the main action and characters central to the page.
- Plan for a `0.125"` to `0.25"` bleed zone around the borders. Do not place critical text or character faces close to the edge of the image canvas.
- For non-Wimmelbuch styles, maintain a single, clear focal point using a shallow depth of field (blurry background elements) to direct the viewer's eyes.

---

## Step-by-Step Workflow

### Step 1: Input Parsing & Scenario Analysis
Parse the user's request to identify the configuration:
1. **Art Style(s)**: Is it a single style or multiple styles? (e.g. Painterly + Coloring Book).
2. **Quantity**: Is it a single image or multiple images/scenes?
3. **Target Folder**: Determine the base output directory (e.g., `projects/pilot/illustration/`).
4. **Scene Elements**: Identify key visual components: character descriptions, action, mood, environment, and lighting.
5. **Layout**: Determine aspect ratio, orientation, safe area (excluding bleed zone), and focal points.

### Step 2: Output Folder Initialization
For every identified style, create its target subdirectory:
- Structure: `<target_folder>/<style_name>/`
- Ensure folders are created before generating images (e.g. `projects/pilot/illustration/painterly/`, `projects/pilot/illustration/coloring_book/`).

### Step 3: Main Image Prompt Construction
For each target image/scene and each target style:
Assemble the prompt using the following structure:
- **Core Subject**: The main character, posture, action, and key expressions.
- **Environment**: Details of the background, setting, and props.
- **Style Keywords**: Select keywords corresponding to the current style (e.g., "painterly digital painting, rich textured brushstrokes" for painterly; "clean crisp black-and-white vector line art outlines, pure white fill" for coloring book).
- **Lighting & Color**: Specify lighting and colors suitable for the style (e.g., "deep blue-violet shadows, warm golden highlights" for painterly; "no shading, pure white background" for coloring sheets).
- **Composition & Camera**: "cinematic composition", "focal point on [subject]", "safe room for page margins", and depth-of-field rules matching the style.

### Step 4: Run the Image Generator & File Organization
For each image:
1. Call the `generate_image` tool to produce the illustration.
   - `Prompt`: The constructed prompt.
   - `ImageName`: Descriptive snake_case name (e.g., `wizard_cozy_library`).
2. Move or copy the generated image from the workspace/default folder to its style-specific subdirectory: `<target_folder>/<style_name>/<image_name>.png`.

### Step 5: Extract visual_specification.md (Visual Specification Sheet)
For multi-page/multi-scene projects, after the first illustration is successfully generated:
1. Document the exact style and character traits to ensure consistency.
2. Create a `visual_specification.md` file in the `<target_folder>/` listing:
   - **ArtStyle(s)**: The selected style(s) and sub-options.
   - **Color Palette**: Hex codes or descriptions of dominant and accent colors.
   - **Character Descriptors**: Specific physical features, clothing, hair, and accessories.
   - **Style Constraints**: Brush style, shadow color rule, lighting source type.
3. Reference this file's guidelines in all subsequent image generation tasks to prevent visual drift.

### Step 6: Generate Supplementary Assets (Afterward)
If supplementary assets (like coloring sheet variants, character sheets, expression sheets, turnaround studies, or color boards) are needed or requested:
1. Create them only *after* the main illustration has been generated.
2. Construct prompts that reference the style and specifications established in `visual_specification.md` to ensure they match perfectly.
3. For character turnaround sheets, specify "character design turnaround sheet, front, side, and 3/4 views, white clean background, matching the style of [Base Illustration Name]".
4. Save these assets in the appropriate `<target_folder>/<style_name>/` directory.

---

## Technical Audit Checklist
Always run this audit on generated illustrations:
- [ ] **Bleed Check**: Are all key subjects, faces, and text elements clear of the outer 10% edge?
- [ ] **Style & Outline Consistency**: Does the rendering strictly match the rules of the selected style folder? (e.g., no shading/gray gradients in Coloring Book; no outlines in Painterly; no textures in Flat Vector).
- [ ] **Focal Point & Layout**: Is the layout balanced? (If Painterly/Watercolor, is there a clear focal point with soft background elements? If Wimmelbuch, are details crisp across the frame?)
- [ ] **File Details**: Export the final images as high-quality PNGs or TIFFs. Avoid JPEG compression.
- [ ] **Output Destination**: Are the final images saved in the correct `<target_folder>/<style_name>/` directories?
- [ ] **Consistency Check**: If using a `visual_specification.md`, do the colors and character details align with it?
