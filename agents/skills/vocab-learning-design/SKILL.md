---
name: vocab-learning-design
description: "Analyze vocabulary from any English text (video/audio transcripts, textbook chapters, articles, song lyrics, stories) and produce a comprehensive vocabulary learning report. Extracts key words with IPA transcription, vocabulary tier (Tier 1/2/3), frequency ranking, definitions, and source sentences. Includes summary statistics, thematic grouping, and learning priority recommendations. Actions: analyze vocabulary, extract vocab, vocab report, vocabulary analysis, study words. Accepts optional proficiency level filter (A1–C2)."
---

# Vocab Learning Design

## Overview

Analyze any English text input and produce a **single comprehensive vocabulary analysis report** in markdown format. The skill extracts learning-valuable words, categorizes them by tier and frequency, and organizes them into actionable study material.

Supports any text source: video/audio transcripts (e.g., output from the video-summarizer skill), textbook chapters, articles, song lyrics, stories, or raw pasted text.

## Trigger Conditions

Activate this skill when the user:
- Says "analyze vocabulary", "extract vocab", "vocab report", "vocabulary analysis"
- Provides a text and asks to "learn words from this", "study vocabulary", "what words should I learn"
- Provides a transcript (from video-summarizer or elsewhere) and asks for vocabulary work
- Says "vocab learning design" or "vocabulary breakdown"
- Asks to "find important words" or "extract key terms" from a text

## Inputs

### Required
- **Source text**: One of the following:
  - Inline text pasted by the user
  - A file path to a text file (`.txt`, `.md`, `.vtt`, `.srt`, or any plain text)
  - A transcript directory from the video-summarizer skill (read `transcript.txt` or `subtitle.vtt`)

### Optional
- **Proficiency level filter**: User can specify a minimum CEFR level (e.g., "only B1+ words", "intermediate and above"). When provided, skip words below that level.
  - Mapping: A1 = beginner, A2 = elementary, B1 = intermediate, B2 = upper-intermediate, C1 = advanced, C2 = proficiency
- **Source title**: If not provided, infer from filename or first line of text.

## Workflow

### Step 1: Read and Prepare the Source Text

1. If the user provides a file path, read the file contents.
2. If the user points to a video-summarizer output directory, look for `transcript.txt` first, then `subtitle.vtt`.
3. For `.vtt` or `.srt` files, strip timestamp lines and formatting markers to get plain text.
4. Store the clean text for analysis.

### Step 2: Analyze Vocabulary

Perform the following analysis on the source text:

#### 2a. Tokenization and Filtering
- Tokenize the text into individual words.
- Normalize to lowercase for deduplication (but preserve original casing for display).
- **Remove** ultra-common function words that have minimal learning value:
  - Articles: a, an, the
  - Pronouns: I, you, he, she, it, we, they, me, him, her, us, them, my, your, his, its, our, their
  - Prepositions: in, on, at, to, for, with, by, from, of, about, into, through, during, before, after, between, under, above, over, below
  - Conjunctions: and, but, or, nor, so, yet, for
  - Auxiliaries: is, am, are, was, were, be, been, being, have, has, had, do, does, did, will, would, shall, should, can, could, may, might, must
  - Common adverbs: not, very, also, just, then, now, here, there
  - Determiners: this, that, these, those, some, any, every, each, all, both, few, many, much, more, most, other, another
  - Common verbs with minimal learning value: get, go, come, make, take, give, say, tell, know, think, see, look, want, need, use, find, put, let
- **Keep** all remaining content words: nouns, verbs, adjectives, adverbs, and domain-specific terms.

#### 2b. Categorize Each Word

For each selected word, determine:

1. **Part of Speech**: noun, verb, adjective, adverb, etc. (based on how it's used in the source text)
2. **Vocabulary Tier**:
   - **Tier 1 (Everyday)**: Common words most people know from daily conversation (e.g., happy, run, house)
   - **Tier 2 (Academic/Cross-domain)**: High-utility words that appear across many contexts but aren't basic (e.g., analyze, significant, demonstrate, facilitate). **These are the highest-priority learning words.**
   - **Tier 3 (Domain-specific)**: Technical or specialized terms tied to a particular field (e.g., phonemic, mnemonic, quasi-experimental)
3. **Frequency Rank**: Estimate how common the word is in general English:
   - **High frequency**: Among the top ~2,000 most common English words
   - **Medium frequency**: Roughly 2,001–8,000 range
   - **Low frequency**: Beyond the top 8,000
4. **IPA Transcription**: Provide the International Phonetic Alphabet pronunciation (e.g., /ˈæn.ə.laɪz/ for "analyze")
5. **Definition**: A clear, concise definition appropriate to how the word is used in the source text (not all possible meanings — the contextual meaning)
6. **Source Sentence**: Extract the sentence (or a meaningful clause) from the source text where this word appears

#### 2c. Identify Themes

Group the extracted vocabulary into **thematic clusters** based on the content of the source text. For example, if the text is about cooking, themes might be: "Ingredients", "Cooking Actions", "Kitchen Equipment", "Flavor Descriptions".

Each word should belong to exactly one theme. Create 3–7 themes depending on the breadth of the text.

#### 2d. Determine Learning Priorities

Rank words by learning value using this priority formula:
1. **Tier 2 words** are always highest priority (most transferable value)
2. Within the same tier, **medium-frequency** words outrank high-frequency (already likely known) and low-frequency (too niche)
3. Words that appear **multiple times** in the source text get a boost (the text itself provides natural repetition)
4. **Tier 3 words** are prioritized only if the user is likely studying the specific domain

### Step 3: Generate the Report

Produce a single markdown file with the following structure:

---

```markdown
# Vocabulary Analysis: [Source Title]

> **Source:** [filename or "User-provided text"]
> **Date:** [current date]
> **Total words analyzed:** [count of unique content words before filtering]
> **Words selected:** [count of words in the report]
> **Proficiency filter:** [specified level or "None"]

---

## 1. Source Summary

[2–3 sentences summarizing what the source text is about, its topic, and its general context. This helps the learner understand the domain before studying individual words.]

---

## 2. Summary Statistics

| Metric | Count |
|--------|-------|
| Total unique content words | [N] |
| Words selected for study | [N] |
| Tier 1 (Everyday) | [N] |
| Tier 2 (Academic) | [N] |
| Tier 3 (Domain-specific) | [N] |

**By Part of Speech:**

| Part of Speech | Count |
|----------------|-------|
| Nouns | [N] |
| Verbs | [N] |
| Adjectives | [N] |
| Adverbs | [N] |
| Other | [N] |

---

## 3. Vocabulary Table

| # | Word | IPA | POS | Tier | Frequency | Definition | Source Sentence |
|---|------|-----|-----|------|-----------|------------|-----------------|
| 1 | [word] | /[ipa]/ | [pos] | [tier] | [freq] | [definition] | "[sentence from text]" |
| 2 | ... | ... | ... | ... | ... | ... | ... |

---

## 4. Thematic Grouping

### Theme: [Theme Name 1]
[Brief description of this theme]

| Word | Tier | Definition |
|------|------|------------|
| [word] | [tier] | [definition] |
| ... | ... | ... |

### Theme: [Theme Name 2]
...

[Repeat for each theme]

---

## 5. Learning Priorities

### 🔴 Learn First (Highest Value)
[List of words with brief rationale for why they're top priority]

| Priority | Word | Tier | Frequency | Why Learn This |
|----------|------|------|-----------|----------------|
| 1 | [word] | Tier 2 | Medium | [rationale] |
| 2 | ... | ... | ... | ... |

### 🟡 Learn Next (High Value)
[Second batch of words]

| Priority | Word | Tier | Frequency | Why Learn This |
|----------|------|------|-----------|----------------|
| ... | ... | ... | ... | ... |

### 🟢 Learn Later (Supplementary)
[Lower priority words — either too common or too niche]

| Priority | Word | Tier | Frequency | Why Learn This |
|----------|------|------|-----------|----------------|
| ... | ... | ... | ... | ... |
```

---

### Step 4: Save the Report

Save the report as a markdown file:

- If the source is from a video-summarizer output directory: save as `vocab-report.md` in the same directory (alongside `transcript.txt`, `summary.md`, etc.)
- If the source is a standalone file: save to `./downloads/[source-title]/vocab-report.md`
- If the source is inline text: save to `./downloads/vocab-report-[timestamp]/vocab-report.md`

Tell the user the file path after saving.

## Key Pedagogical Principles

These principles should guide word selection and report design:

1. **Tier 2 words are the sweet spot.** They are high-utility academic words that transfer across subjects and contexts. Learners get the most return on investment from mastering these words.

2. **Context over isolation.** Always provide the source sentence so learners encounter words in natural context, not as isolated definitions. This mirrors how music and authentic materials create neural pathways for retention.

3. **Thematic clustering aids memory.** Grouping words by topic leverages pattern recognition — the brain retains related concepts more effectively than random word lists.

4. **Frequency awareness prevents wasted effort.** Don't ask learners to study words they already know (high-frequency Tier 1) or words they'll rarely encounter again (very low-frequency Tier 3), unless domain-relevant.

5. **Repetition signals importance.** Words appearing multiple times in the source text are naturally reinforced by the material itself — flag these as higher priority.

## Word Count Guidelines

- For **short texts** (< 500 words): Extract 10–20 vocabulary items
- For **medium texts** (500–2000 words): Extract 20–40 vocabulary items
- For **long texts** (> 2000 words): Extract 30–60 vocabulary items (cap at 60 to keep the report actionable)

If a proficiency filter is applied, the final count may be lower.

## Example Usage

### Basic usage
```
User: "Analyze the vocabulary in this transcript: [pastes text]"
Agent: [Produces vocab-report.md with all 5 sections]
```

### With proficiency filter
```
User: "Extract B2+ vocabulary from ./downloads/ted-talk/transcript.txt"
Agent: [Produces vocab-report.md filtering out A1–B1 level words]
```

### From video-summarizer output
```
User: "Generate a vocab report from ./downloads/my-video/"
Agent: [Reads transcript.txt from that directory, produces vocab-report.md in the same directory]
```

## Notes

1. **Accuracy**: IPA transcriptions should follow standard British or American English pronunciation. If a word has notably different British/American pronunciations, prefer American English unless the source text is clearly British.
2. **Contextual definitions**: Always define words based on their meaning in the source text, not their most common dictionary meaning (e.g., "bank" in a river context means riverbank, not financial institution).
3. **No exercises**: This skill focuses on vocabulary analysis and reporting. It does not generate exercises, quizzes, or lesson plans. A separate skill could consume this report to generate learning activities.
4. **Integration**: This skill pairs naturally with the video-summarizer skill — first download and transcribe a video, then analyze its vocabulary.
