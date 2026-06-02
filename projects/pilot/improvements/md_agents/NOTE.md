# MD Agent Improvement Note: Relative Path Rule

When linking to files or resources within the project repository from any Markdown (`.md`) files, you must always use relative paths instead of absolute local file system paths (e.g., `file:///Users/...`).

## Rules
1. **No Absolute Local Paths**: Do not use local system URIs starting with `file:///` for internal project links. These links break when cloned or run on another machine.
2. **Relative Paths**: Always use paths relative to the file containing the link (e.g., `../song/transcript.txt` or `./VOCAB.md`).
3. **Markdown References**: Apply this rule to all references, sources, images, and anchors referencing internal assets.
