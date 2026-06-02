---
name: illustration
description: Generate, plan, and refine illustrations for stories, texts, or books using the generate_image tool. Apply professional digital painting techniques (form-based blocking, painterly styling, volumetric shading, focal point definition) and print preparation rules (bleed zones, high-resolution formats). Create supplementary artifacts (character sheets, color palettes, layout guides) as needed AFTER generating the primary illustrations. Use this skill whenever the user wants to illustrate scenes, stories, or create character/concept art.
---

# Illustration Skill

Use this skill to guide the creation of painterly, consistent digital illustrations for books, stories, and texts using the `generate_image` tool.

## Key Principles

### 1. Form-Thinking over Line-Thinking
Do not describe scene elements in terms of outlines, hard edges, or simple flat colors. Instead:
- Emphasize volume, mass, and color blocks.
- Focus on light and form sculpting (describing light falling on objects, highlights carving out shapes).

### 2. Digital Brushwork & Texture
Replicate professional digital painting techniques (e.g., Photoshop, Procreate brush dynamics) in prompts:
- Describe textures such as "visible canvas textures", "textured oil/wet brushstrokes", and "soft blended transitions".
- Incorporate concepts of the Smudge and Blur tools: "soft, blended gradients for skin and backgrounds", and "softly smudged edges to blend details naturally into the main form".

### 3. Volumetric Shading
Avoid flat black or dark grey shadows.
- Specify shadows using rich, cool tones (e.g., "cool blue and violet shadow undertones in skin and fabrics", "warm golden highlights contrasting with cool-toned shadows").
- Use dodge/burn lighting terminology: "cinematic volumetric lighting", "rim lighting highlighting silhouettes", and "contrasting highlights that bring out the three-dimensional depth".

### 4. Composition & Bleed
For storybooks and printing:
- Keep the main action and characters central to the page.
- Plan for a `0.125"` to `0.25"` bleed zone around the borders. Do not place critical text or character faces close to the edge of the image canvas.
- Maintain a single, clear focal point per illustration. Use a shallow depth of field (blurry background elements) to direct the viewer's eyes.

---

## Step-by-Step Workflow

### Step 1: Scenario Analysis & Composition Planning
1. Identify the key visual components of the target scene: character descriptions, action, mood, environment, and lighting.
2. Determine the canvas aspect ratio and orientation (e.g., landscape, portrait, square).
3. Plan the safe area (excluding the bleed zone) and the focal point.

### Step 2: Main Image Prompt Construction
Assemble the prompt using the following structure:
- **Core Subject**: The main character, posture, action, and key expressions.
- **Environment**: Details of the background, setting, and props.
- **Style Keywords**: "painterly digital painting", "rich textured brushstrokes", "volumetric rendering", "digital clay sculpting", "wet paint blending".
- **Lighting & Color**: Specify the lighting source (e.g., "dramatic chiaroscuro", "warm sunlight filtering through foliage") and shadow colors (e.g., "deep blue-violet shadows").
- **Composition & Camera**: "cinematic composition", "focal point on [subject]", "softly blurred background elements", "room for page margins".

### Step 3: Run the Image Generator
Call the `generate_image` tool to produce the illustration.
- `Prompt`: The constructed prompt.
- `ImageName`: Descriptive snake_case name (e.g., `wizard_cozy_library`).

### Step 4: Extract visual_specification.md (Visual Specification Sheet)
For multi-page/multi-scene projects, after the first illustration is successfully generated:
1. Document the exact style and character traits to ensure consistency.
2. Create a `visual_specification.md` file listing:
   - **Color Palette**: Hex codes or descriptions of dominant and accent colors.
   - **Character Descriptors**: Specific physical features, clothing, hair, and accessories.
   - **Style Constraints**: Brush style, shadow color rule, lighting source type.
3. Reference this file's guidelines in all subsequent image generation tasks to prevent visual drift.

### Step 5: Generate Supplementary Assets (Afterward)
If supplementary assets (like character sheets, expression sheets, turnaround studies, or color boards) are needed or requested:
1. Create them only *after* the main illustration has been generated.
2. Construct prompts that reference the style and specifications established in `visual_specification.md` to ensure they match perfectly.
3. For character turnaround sheets, specify "character design turnaround sheet, front, side, and 3/4 views, white clean background, matching the style of [Base Illustration Name]".

---

## Technical Audit Checklist
Always run this audit on generated illustrations:
- [ ] **Bleed Check**: Are all key subjects, faces, and text elements clear of the outer 10% edge?
- [ ] **Form & Volume**: Does the shading feel volumetric, or is it flat/linear? Are shadows colored (not pure black)?
- [ ] **Focal Point**: Is the center of attention sharp, while secondary elements are softer/blended?
- [ ] **File Details**: Export the final images as high-quality PNGs or TIFFs. Avoid JPEG compression.
- [ ] **Consistency Check**: If using a `visual_specification.md`, do the colors and character details align with it?
