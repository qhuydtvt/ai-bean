#!/bin/bash
# Check if img2pdf is already available
python3 -c "import img2pdf" 2>/dev/null
if [ $? -eq 0 ]; then
  echo "img2pdf is already installed."
  exit 0
fi

echo "Installing img2pdf..."
# Handle Homebrew/externally-managed PEP 668 warning
python3 -m pip install img2pdf --break-system-packages || python3 -m pip install img2pdf
