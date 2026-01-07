#!/bin/bash
# AI Power Pack v2.4 - Remote Installer for Linux/macOS
# Usage: curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/REPO_NAME/main/install.sh | bash

set -e

echo ""
echo "========================================"
echo "   AI Power Pack v2.4"
echo "   Remote Installer"
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check Python
echo -e "${CYAN}[1/5] Checking Python...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}  ✓ Python installed: $PYTHON_VERSION${NC}"
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    echo -e "${GREEN}  ✓ Python installed: $PYTHON_VERSION${NC}"
    PYTHON_CMD=python
else
    echo -e "${RED}  ✗ Python not installed${NC}"
    echo ""
    echo -e "${YELLOW}Please install Python 3.8+ from:${NC}"
    echo "https://www.python.org/downloads/"
    exit 1
fi

# Download package
echo ""
echo -e "${CYAN}[2/5] Downloading AI Power Pack...${NC}"
TEMP_DIR="/tmp/ai_power_pack"
ZIP_URL="https://github.com/GQSDGQWE/AIDevKit/archive/refs/heads/main.zip"

rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"

if command -v curl &> /dev/null; then
    curl -fsSL "$ZIP_URL" -o "$TEMP_DIR/package.zip"
elif command -v wget &> /dev/null; then
    wget -q "$ZIP_URL" -O "$TEMP_DIR/package.zip"
else
    echo -e "${RED}  ✗ Neither curl nor wget found${NC}"
    exit 1
fi

unzip -q "$TEMP_DIR/package.zip" -d "$TEMP_DIR"
EXTRACTED_DIR=$(find "$TEMP_DIR" -maxdepth 1 -type d ! -path "$TEMP_DIR" | head -n 1)

echo -e "${GREEN}  ✓ Package downloaded${NC}"

# Configure Claude Desktop
echo ""
echo -e "${CYAN}[3/5] Configuring Claude Desktop...${NC}"

# macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    CLAUDE_PATH="$HOME/Library/Application Support/Claude"
# Linux
else
    CLAUDE_PATH="$HOME/.config/Claude"
fi

if [ -d "$CLAUDE_PATH" ]; then
    CLAUDE_MD="$EXTRACTED_DIR/config/CLAUDE.md"
    if [ -f "$CLAUDE_MD" ]; then
        CONFIG_FILE="$CLAUDE_PATH/claude_desktop_config.json"
        CONTENT=$(cat "$CLAUDE_MD")
        
        cat > "$CONFIG_FILE" << EOF
{
  "customInstructions": {
    "global": $(echo "$CONTENT" | jq -Rs .),
    "version": "2.4",
    "source": "github",
    "installed": "$(date '+%Y-%m-%d %H:%M:%S')"
  }
}
EOF
        echo -e "${GREEN}  ✓ Claude Desktop configured${NC}"
    fi
else
    echo -e "${YELLOW}  - Claude Desktop not found, skipping${NC}"
fi

# Configure VSCode
echo ""
echo -e "${CYAN}[4/5] Configuring VSCode...${NC}"

# macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    VSCODE_PATH="$HOME/Library/Application Support/Code/User"
# Linux
else
    VSCODE_PATH="$HOME/.config/Code/User"
fi

if [ -d "$VSCODE_PATH" ]; then
    COPILOT_MD="$EXTRACTED_DIR/config/copilot-instructions.md"
    if [ -f "$COPILOT_MD" ]; then
        cp "$COPILOT_MD" "$VSCODE_PATH/copilot-instructions.md"
        
        SETTINGS_FILE="$VSCODE_PATH/settings.json"
        if [ -f "$SETTINGS_FILE" ]; then
            # Backup existing settings
            cp "$SETTINGS_FILE" "$SETTINGS_FILE.backup"
        fi
        
        # Create or update settings
        cat > "$SETTINGS_FILE" << 'EOF'
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": "copilot-instructions.md",
      "text": "Follow AI Power Pack v2.4 standards"
    }
  ],
  "github.copilot.enable": {
    "*": true,
    "plaintext": true,
    "markdown": true
  }
}
EOF
        echo -e "${GREEN}  ✓ VSCode configured${NC}"
    fi
else
    echo -e "${YELLOW}  - VSCode not found, skipping${NC}"
fi

# Install dependencies
echo ""
echo -e "${CYAN}[5/5] Installing Python dependencies...${NC}"
$PYTHON_CMD -m pip install -q requests cryptography pyside6 fastapi sqlmodel uvicorn 2>/dev/null || true
echo -e "${GREEN}  ✓ Dependencies installed${NC}"

# Cleanup
rm -rf "$TEMP_DIR"

# Complete
echo ""
echo -e "${CYAN}========================================${NC}"
echo -e "${GREEN}   Installation Complete! ✨${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""
echo -e "${YELLOW}📝 Next Steps:${NC}"
echo "  1. Restart Claude Desktop"
echo "  2. Restart VSCode"
echo "  3. Test: Ask Claude 'What coding standards do you follow?'"
echo ""
echo -e "${CYAN}🎉 Thank you for using AI Power Pack v2.4!${NC}"
echo ""
