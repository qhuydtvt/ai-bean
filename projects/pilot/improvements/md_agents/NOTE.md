# MD Agent Guideline: Markdown Link & Quality Standards

This document establishes the guidelines and automated checks for AI agents and human contributors when creating or editing Markdown (`.md`) files within this repository. 

To maintain project portability, clean rendering, and link integrity, all markdown files must comply with the rules below.

---

## Core Rules

### 1. Repository Portability (Relative Paths Only)
*   **No Absolute Local System Paths**: Do not use local file system paths starting with `file:///Users/...` or `/Users/...` for internal project resources. These absolute paths break when the repository is cloned, shared, or run on another machine.
*   **Strict Relative Links**: Always use paths relative to the directory containing the markdown file.
    *   *Correct*: `[Transcript](../song/transcript.txt)` (from `projects/pilot/vocab/VOCAB.md`)
    *   *Incorrect*: ``[Transcript](file:///Users/username/Learn/ai-bean/projects/pilot/song/transcript.txt)``
*   **Applies to All References**: This rule covers all internal text links, image embeds, code file links, and references to assets within the project workspace.

### 2. Formatting & Clean Rendering
*   **No Backticks inside Markdown Link Text**: Avoid wrapping link text in backticks if it prevents or interferes with link rendering in your environment.
    *   *Correct*: `[utils.py](../scripts/utils.py)`
    *   *Incorrect*: ``[`utils.py`](../scripts/utils.py)``
*   **Handle Spaces Correctly**: If relative file paths contain spaces, use standard URL encoding (e.g., `%20` for space) or keep them clean by using hyphens or underscores in filenames.

### 3. Link Validity & Integrity
*   **Verify Anchors**: When linking to headers inside files (e.g., ``[Overview](#overview)`` or ``[link](file.md#header-name)``), ensure the target header matches the slugified format: lowercase, alphanumeric characters, and hyphens representing spaces.
*   **No Placeholders**: Never include empty link brackets `[]()` or TODO placeholders for internal files. Every link must point to a valid, existing destination at the time of commit.

---

## Automated Verification

We have created an automated link check script to scan and validate all Markdown links:
👉 [verify_links.py](../../scripts/verify_links.py)

### What it checks:
1. Searches for all `.md` files under the pilot project.
2. Identifies all internal markdown links (`[text](url)` and `![alt](url)`).
3. Detects any absolute paths (e.g., `file:///`, `/Users/`, etc.).
4. Resolves relative paths and verifies if the targeted file or directory actually exists on disk.
5. Returns a non-zero exit code if any broken links or absolute path violations are found, making it suitable for pre-commit hooks or CI/CD pipelines.

### How to Run:
Run the script from the workspace root directory:
```bash
python3 projects/pilot/scripts/verify_links.py
```
