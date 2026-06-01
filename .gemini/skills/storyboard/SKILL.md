---
name: storyboard
description: >
  Transform a children's story or any source material (topic, transcript, article, book excerpt) into a
  professionally structured picture book storyboard. Produces a spread-by-spread breakdown with beat mapping,
  art direction notes, composition guidance, and built-in quality verification. Supports both short-form
  (5–10 pages) and standard 32-page picture book formats.
  Use this skill whenever the user mentions storyboarding, picture book layout, page spreads, visual beats,
  book pagination, illustration planning, dummy book, art direction for children's books, or wants to turn
  a story into a page-by-page visual plan — even if they don't explicitly say "storyboard."
---

# Short-Form Picture Book Storyboard

Turn a story or source material into a production-ready picture book storyboard — a spread-by-spread blueprint with narrative text, art direction, and architectural verification.

For the detailed rules behind every decision in this skill, read `references/picture-book-architecture.md`. That document covers pagination tables, pacing formulas, gutter safety, perspective categories, and character consistency specs. Consult it whenever you need the exact rationale or parameters for a specific storyboard element.

## Accepted Inputs

The user may provide source material in any of these forms:

- **A finished children's story** — from the `story-telling` skill or written by hand. Skip straight to storyboarding.
- **Pasted text** — a topic, transcript, article, or free-form idea. You'll distill the narrative first.
- **File paths** — `.txt`, `.md`, `.srt`, or any readable text file. Read contents first.
- **URLs** — fetch page content and extract relevant text.

If the user provides only a vague topic (e.g., "a picture book about sharing"), treat it as creative input and build the narrative from scratch.

## Step 1 — Gather Context

Before generating anything, confirm these parameters. Ask the user if not provided:

1. **Format**:
   - **Short-form** (5–10 pages, 3–5 beats, <150 words) — the default
   - **Standard** (32 pages, 12–14 beats, <500 words)
2. **Target age group**:
   - **Ages 2–5** (Picture Books) — simple, rhythmic, repetitive
   - **Ages 5–7** (Early Readers) — short sentences, humor-driven
   - **Ages 7–12** (Chapter Books) — nuanced, suspenseful
3. **Preferences** — theme, characters, setting, tone, any stylistic references

## Step 2 — Extract Narrative Core

Whether working from a finished story or raw material, identify:

- **Core theme / lesson** (implicit, not preachy)
- **Protagonist** with a relatable flaw and agency (they solve their own problem)
- **Inciting incident** — what disrupts the world?
- **Escalation points** — how does the conflict deepen?
- **Resolution** — how does the world settle into a new state?
- **Emotional arc** — what should the reader feel at beginning, middle, and end?

If working from raw material, write a concise narrative draft (respecting word count limits for the chosen format) before moving to Step 3. This draft becomes the story text that gets divided into spreads.

## Step 3 — Allocate Structure

Apply the structural framework from the spec:

### Matter Allocation

For **short-form**: compress front/back matter aggressively.
- Combine title, copyright, dedication onto a single page or the back cover
- Begin the narrative on page 1 or 2

For **standard 32-page**: follow traditional allocation (4–6 pages for matter, 24–28 pages for story).

### Beat Mapping

Divide the narrative into beats — each beat is a pivotal moment where action or setting shifts:
- **Short-form**: 3 to 5 beats
- **Standard**: 12 to 14 beats

Assign each beat to a double-page spread.

### Pacing — The "Quarter-Half-Quarter" Rule

Distribute story pages (excluding matter) as:
- **1/4 Beginning** — world-building, character introduction, inciting incident
- **1/2 Middle** — conflict escalation, obstacles, climax
- **1/4 End** — resolution, emotional payoff

## Step 4 — Compose the Storyboard

Generate the spread-by-spread storyboard document. For each spread, provide:

### 4a. Narrative Text
The actual story text for this spread, word-count appropriate. In short-form, every word must earn its place.

### 4b. Art Direction Notes
Describe what the illustration should convey. Include:
- **Composition**: What's in the frame? Where are characters positioned?
- **Perspective**: Close-up, medium shot, or wide-angle panoramic? (Vary across spreads — see reference doc Section 4.)
- **Movement & Gaze Direction**: Characters and eyes should generally face right (left-to-right reading flow). Note any intentional exceptions.
- **Color Palette / Mood**: Warm vs. cool tones, lighting, time of day.
- **The "So What?" factor**: The illustration should show the *why* behind emotions, not just mirror the text. If text says "sad," the art shows the broken toy or empty chair.

### 4c. Layout Metadata
- **Visual pacing**: Is this a "busy" (energetic, detailed) or "quiet" (white space, dramatic pause) spread?
- **Gutter safety**: Flag any elements that risk falling into the binding fold. Faces, text, and key objects must stay in the center-left or center-right safety zones.
- **Foreshadowing**: If the right-hand page shows a "future" destination or outcome, note this intentional foreshadowing cue.
- **Page-turn hook**: What on this spread compels the reader to turn the page? (An unfinished sentence, a visual cliffhanger, a question raised.)

### 4d. Character Notes (on first appearance)
On the spread where a character first appears, include a brief character sheet:
- Key physical features and defining props
- Emotional range (how they look in different moods)
- Consistency anchors — what must stay identical across every spread

### Output Template

Use this structure:

```
# [Book Title]

**Format**: [Short-form / Standard 32-page]
**Target Age**: [Age range]
**Total Word Count**: [X words]
**Beat Count**: [N beats across N spreads]

---

## Front Matter

**Page 1** (Title Page)
- *Text*: [Title, author, illustrator]
- *Art direction*: [Cover/title page visual description]

---

## Spread 1 — [Beat Name] (Beginning)

**Pages [X–Y]**

**Story Text**:
> [The actual narrative text for this spread]

**Art Direction**:
- Composition: [description]
- Perspective: [close-up / medium / wide]
- Movement direction: [left-to-right / other with justification]
- Color/mood: [palette and lighting]
- "So What?": [what the illustration reveals beyond the text]

**Layout**:
- Visual pacing: [busy / quiet]
- Gutter safety: [any flagged elements]
- Foreshadowing: [right-page setup, if any]
- Page-turn hook: [what drives the turn]

**Character Sheet** (if first appearance):
- [Character name]: [defining features, props, emotional range]

---

## Spread 2 — [Beat Name] (Middle)
[... same structure ...]

---

## Back Matter

**Back Cover**:
- [ISBN, copyright, barcode placement, brief synopsis if applicable]
```

## Step 5 — Verify (QA Checklist)

After generating the storyboard, run these checks automatically and present results to the user. This is not optional — every storyboard must be audited.

### Plot-Push Test
For each spread, verify:
- [ ] This spread advances the plot (not stalled on exposition or facts)
- [ ] Action moves toward resolution, not lingering
- [ ] The illustration concept expands on the "why," not just repeating text

### Pacing Audit
- [ ] Beginning spreads ≈ 1/4 of story pages
- [ ] Middle spreads ≈ 1/2 of story pages
- [ ] End spreads ≈ 1/4 of story pages
- [ ] Conflict introduced by page 1 or 2 (short-form) or within first quarter (standard)

### Composition & Flow
- [ ] Directional flow is predominantly left-to-right across spreads
- [ ] No critical elements (faces, text, key objects) placed in the gutter zone
- [ ] At least one foreshadowing cue uses right-page "future" logic

### Visual Variety
- [ ] Perspective varies across spreads (not all medium shots)
- [ ] Busy and quiet spreads alternate to create rhythm
- [ ] At least one close-up and one wide-angle spread exist

### Character Consistency
- [ ] Each character has a defined sheet on first appearance
- [ ] Defining features and props are noted for consistency tracking
- [ ] Emotional range is mapped (high and low moments)

### Read-Aloud Timing
- [ ] Page-turn hooks are present on every spread (except the final resolution)
- [ ] Cliffhangers on right-hand pages resolve on the next spread
- [ ] Text rhythm feels natural when read aloud (no stumble points flagged)

### Presentation Format

```
## ✅ Storyboard Quality Review

- [x] **Plot-Push Test** — all spreads advance the plot
- [x] **Pacing Audit** — 1/4-1/2-1/4 ratio met (2 beginning, 3 middle, 2 end)
- [ ] **Composition** — Spread 3 has a character face near the gutter; recommend shifting right
- [x] **Visual Variety** — 2 close-ups, 3 medium shots, 2 wide angles
- [x] **Character Consistency** — Luna's ribbon and Milo's scarf tracked across all spreads
- [x] **Read-Aloud Timing** — all page-turn hooks verified

### Issues to Address
1. [specific issue with spread number and recommended fix]
2. [specific issue with spread number and recommended fix]

Would you like me to fix these issues, adjust the pacing, or change any art direction?
```

## Step 6 — Present and Iterate

Deliver the storyboard and the QA checklist together. Then offer refinement:

- Should any beat be split or merged?
- Does the visual pacing feel right — too energetic, too quiet?
- Are the art direction notes detailed enough for an illustrator?
- Should the word count be adjusted up or down?
- Would you like to change the format (short-form ↔ standard)?

Apply changes and re-run the QA checklist on modified sections.
