import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

# Set the root scan directory to repository root
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent

# Regex to find markdown links: [text](link) or ![alt](link)
# We capture the link inside the parentheses
LINK_REGEX = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')

def verify_links():
    # Find all markdown files, excluding the .git folder
    all_markdown_files = list(REPO_ROOT.rglob("*.md"))
    markdown_files = [p for p in all_markdown_files if ".git" not in p.parts]
    
    total_links_checked = 0
    errors_found = 0
    
    print(f"🔍 Scanning {len(markdown_files)} Markdown files in the repository root...\n")
    
    for md_path in sorted(markdown_files):
        # We want to display paths relative to the workspace root for clarity
        display_path = md_path.relative_to(REPO_ROOT)
        
        try:
            content = md_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"❌ Error reading {display_path}: {e}")
            errors_found += 1
            continue
            
        # Strip code blocks to avoid checking examples
        # Remove triple-backtick code blocks
        clean_content = re.sub(r'```[\s\S]*?```', '', content)
        # Remove double-backtick code blocks
        clean_content = re.sub(r'``[\s\S]*?``', '', clean_content)
        # Remove single-backtick inline code spans
        clean_content = re.sub(r'`[^`\n]*`', '', clean_content)
        
        # Parse links
        links = LINK_REGEX.findall(clean_content)
        if not links:
            continue
            
        file_header_printed = False
        
        for link in links:
            # Clean link: strip leading/trailing spaces
            link = link.strip()
            
            # Skip empty links, external web links, mailto links, or anchor-only links
            if not link or link.startswith(("http://", "https://", "mailto:", "#")):
                continue
                
            total_links_checked += 1
            
            # Check for absolute paths
            if link.startswith("file:///") or link.startswith("/") or "Users/" in link:
                if not file_header_printed:
                    print(f"📄 {display_path}")
                    file_header_printed = True
                print(f"  ❌ Absolute path violation: '{link}'")
                errors_found += 1
                continue
                
            # Parse relative path, removing anchor/query parts (e.g., file.md#section -> file.md)
            clean_link = link.split('#')[0].split('?')[0]
            if not clean_link:
                # If it was just an anchor pointing to another file's header but clean_link is empty
                # which shouldn't happen unless it was just '#' which we already skipped
                continue
                
            # URL unquote (e.g., %20 -> space)
            clean_link = unquote(clean_link)
            
            # Resolve target path relative to the markdown file's directory
            target_path = (md_path.parent / clean_link).resolve()
            
            # Check if target exists
            if not target_path.exists():
                if not file_header_printed:
                    print(f"📄 {display_path}")
                    file_header_printed = True
                print(f"  ❌ Broken relative link: '{link}' (Resolved to: {target_path})")
                errors_found += 1
                
    print("\n--- Scan Results ---")
    print(f"Total Markdown files scanned: {len(markdown_files)}")
    print(f"Total internal links checked: {total_links_checked}")
    
    if errors_found > 0:
        print(f"❌ Completed with {errors_found} errors found.")
        sys.exit(1)
    else:
        print("✅ All internal links are relative and valid! No broken links found.")
        sys.exit(0)

if __name__ == "__main__":
    verify_links()
