---
name: story-telling
description: >
  Transform any text (topics, video transcripts, books, articles, subtitles, or any source material) into engaging
  children's stories. Use this skill whenever the user wants to create a children's story, retell content as a
  narrative for kids, adapt educational material into story form, generate bedtime stories, or asks for creative
  storytelling from any input text — even if they don't explicitly say "children's story." Also trigger when the
  user mentions story writing, narrative creation, tale crafting, read-aloud stories, or picture book text.
---

# Story-Telling Skill

Turn any source material into a polished, age-appropriate children's story grounded in professional narrative craft.

## Accepted Inputs

The user may provide source material in any of these forms — support all of them:

- **Pasted text** — a topic sentence, transcript, article excerpt, book passage, or free-form idea
- **File paths** — `.txt`, `.md`, `.srt` (subtitles), or any readable text file. Read the file contents first.
- **URLs** — fetch the page content and extract the relevant text before writing.

If the user provides only a vague topic (e.g., "a story about friendship"), that's fine — treat the topic itself as the source material and expand creatively.

## Step 1 — Gather Context

Before writing anything, make sure you know:

1. **Source material** — read/fetch all provided inputs and identify the core content.
2. **Target age group** — this is required. If the user hasn't specified, ask:
   - **Ages 2–5** (Picture Books) — simple, rhythmic, highly repetitive. Familiar words, heavy musicality, sound patterns.
   - **Ages 5–7** (Early Readers) — short sentences, direct action. Humor-focused, relatable energy, concrete imagery.
   - **Ages 7–12** (Chapter Books) — expressive, nuanced, split-level writing. Withholding info for suspense, unique character quirks.
3. **Any preferences** — length, characters, setting, moral/theme, tone. Use sensible defaults if not specified.

## Step 2 — Extract Core Themes

Analyze the source material and identify:

- Key ideas, facts, or lessons worth conveying
- Potential characters (or invent ones that embody the themes)
- Settings that ground the narrative in sensory detail
- Emotional arcs — what should the reader feel at the beginning, middle, and end?

Briefly note these internally before drafting. You don't need to present them to the user unless they ask.

## Step 3 — Draft the Story

Write the story in **Markdown** using the narrative craft framework. Read `references/craft-framework.md` for the full set of techniques — here's the essence:

### Show, Don't Tell
- Replace static verbs ("is," "are," "was") with precision verbs and concrete nouns.
- Engage multiple senses — sight, sound, smell, touch, taste.
- Create "illustratable moments" — specific actions an artist could draw.

### Prose Musicality
- Use onomatopoeia, alliteration, and internal rhymes to give the text a beat.
- Place hooks at the end of scenes to drive the "page-turn factor."

### Authentic Dialogue
- Keep dialogue snappy and purposeful — every line advances plot or deepens character.
- Avoid narrator-in-disguise exposition. Let characters sound like real people.
- Prefer "said" over creative tags. Use action beats to convey emotion.
- Give each character a unique voice — varying line lengths, quirks, catchphrases.

### Age-Appropriate Language
- Match vocabulary, sentence structure, and complexity to the target age group.
- Replace abstract jargon with concrete imagery (e.g., "a locked door with no key" instead of "bureaucratic obstacle").

### Narrative Mechanics
- Start with a "What If?" premise that sparks curiosity.
- Give the protagonist a relatable flaw — perfection kills engagement.
- Use signposts in longer stories to keep the reader oriented.
- Build suspense through withholding and cliffhangers at scene breaks.

### Output Structure

Format the story as:

```
# [Story Title]

## [Chapter/Scene 1 Title]

[Story text with dialogue, action, sensory detail...]

## [Chapter/Scene 2 Title]

[Continued...]

---
*[Optional: a one-line moral or reflection, if appropriate for the age group]*
```

For picture book age (2–5), skip chapter headings — write as a flowing sequence of short, rhythmic paragraphs.

## Step 4 — Self-Review (Verification Checklist)

After drafting, run the story through these quality checks. Present the results to the user as a checklist.

### The "Is/Are/Was" Scan
Search for passive "telling" verbs (is, are, was, were, had been). Flag any sentence that relies on them and suggest a "showing" alternative.

### Visual Verification
For each key scene, ask: "Can an artist draw this?" If a passage is abstract or internal with no externalized action, flag it and rewrite to add a concrete, illustratable moment.

### Relatability Check
- Would a child of the target age actually understand and relate to this?
- Are characters' emotions shown through behavior, not just named?
- Does the protagonist have a genuine flaw?

### Age-Appropriateness Audit
- Vocabulary matches the developmental stage
- Sentence length and complexity are appropriate
- Tone matches the age energy (curiosity for young, rebellion/nuance for older)

### Dialogue Quality
- Read-aloud test: does every line of dialogue sound natural when spoken?
- Brevity: no dialogue lines serving as exposition dumps
- Voice differentiation: can you tell characters apart by how they speak?

### Presentation Format

Present the checklist like this:

```
## ✅ Story Quality Review

- [x] **Is/Are/Was Scan** — 2 instances found and revised (see lines X, Y)
- [x] **Visual Verification** — all scenes are illustratable
- [ ] **Relatability** — the ending feels rushed; consider expanding the resolution
- [x] **Age-Appropriateness** — vocabulary matches ages 5–7
- [x] **Dialogue Quality** — all voices distinct, natural rhythm

### Suggested Improvements
1. [specific, actionable suggestion]
2. [specific, actionable suggestion]

Would you like me to apply these improvements, or adjust anything else?
```

## Step 5 — Present and Iterate

Deliver the story and the checklist together. Then ask follow-up questions to help the user refine:

- Are there scenes that feel flat or need more sensory detail?
- Should any characters be developed further?
- Is the pacing right — too fast, too slow?
- Would you like me to adjust the reading level up or down?
- Should I add or remove humor, suspense, or emotional weight?

Apply requested changes and re-run the checklist on modified sections.
