# Agent Guidelines

To ensure project portability and clean rendering across different environments, all agents must adhere to the following rules:

## 1. Relative Markdown Links
*   **Relative Paths Only**: Every internal link or media reference inside any Markdown (`.md`) file must be written as a relative path from the containing file (e.g., `../song/transcript.txt`).
*   **No Absolute Paths**: Do not use absolute local system paths (such as `/Users/...` or `file:///Users/...`). These break when the project is cloned or executed on another machine.
*   **Link Verification**: Verify that the targeted file or directory actually exists on the filesystem.
*   **No Backticks in Link Text**: Keep the link text clean. Avoid formatting link text with backticks (e.g., use `[file.py](path/to/file.py)` instead of `[`file.py`](path/to/file.py)`).

## 2. Automated Check
Before completing tasks or committing changes, run the repository link validator to ensure all Markdown links are valid and relative:
```bash
python3 projects/pilot/scripts/verify_links.py
```
