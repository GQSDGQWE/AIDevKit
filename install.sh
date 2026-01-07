#!/bin/bash
# AI Power Pack v2.4 - Remote Installer for Linux/macOS
# Usage: curl -fsSL https://raw.githubusercontent.com/GQSDGQWE/AIDevKit/main/install.sh | bash

set -e

# Disable interactive prompts
export DEBIAN_FRONTEND=noninteractive

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
GRAY='\033[0;37m'
NC='\033[0m' # No Color

# Check Python (optional)
echo -e "${CYAN}[1/5] Checking Python...${NC}"
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}  ✓ Python3 detected${NC}"
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    echo -e "${GREEN}  ✓ Python detected${NC}"
    PYTHON_CMD=python
else
    echo -e "${GRAY}  ○ Python not detected (optional)${NC}"
    PYTHON_CMD=""
fi

# Download package
echo ""
echo -e "${CYAN}[2/5] Downloading AI Power Pack...${NC}"
TEMP_DIR="/tmp/ai_power_pack_$$"
ZIP_URL="https://github.com/GQSDGQWE/AIDevKit/archive/refs/heads/main.zip"

mkdir -p "$TEMP_DIR"

echo -e "${GRAY}  → Downloading from GitHub...${NC}"
if command -v curl &> /dev/null; then
    curl -fsSL --connect-timeout 30 --max-time 60 "$ZIP_URL" -o "$TEMP_DIR/package.zip" || {
        echo -e "${RED}  ✗ Download failed${NC}"
        rm -rf "$TEMP_DIR"
        exit 1
    }
elif command -v wget &> /dev/null; then
    wget --timeout=30 -q "$ZIP_URL" -O "$TEMP_DIR/package.zip" || {
        echo -e "${RED}  ✗ Download failed${NC}"
        rm -rf "$TEMP_DIR"
        exit 1
    }
else
    echo -e "${RED}  ✗ Neither curl nor wget found${NC}"
    rm -rf "$TEMP_DIR"
    exit 1
fi

echo -e "${GRAY}  → Extracting...${NC}"
unzip -q "$TEMP_DIR/package.zip" -d "$TEMP_DIR" 2>/dev/null || {
    echo -e "${RED}  ✗ Extraction failed${NC}"
    rm -rf "$TEMP_DIR"
    exit 1
}

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
        
        # 使用 jq 如果可用，否则使用简单方法
        if command -v jq &> /dev/null; then
            CONTENT=$(cat "$CLAUDE_MD")
            cat > "$CONFIG_FILE" << EOF
{
  "customInstructions": {
    "global": $(echo "$CONTENT" | jq -Rs .),
    "version": "2.4",
    "source": "github"
  }
}
EOF
        else
            # 简单复制，不使用 jq
            cp "$CLAUDE_MD" "$CLAUDE_PATH/CLAUDE_RULES.md" 2>/dev/null || true
        fi
        
        echo -e "${GREEN}  ✓ Claude Desktop configured${NC}"
    else
        echo -e "${GRAY}  ○ Config file not found (skipping)${NC}"
    fi
else
    echo -e "${GRAY}  ○ Claude Desktop not detected (skipping)${NC}"
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
        cp "$COPILOT_MD" "$VSCODE_PATH/copilot-instructions.md" 2>/dev/null || {
            echo -e "${GRAY}  ○ VSCode config copy failed (skipping)${NC}"
        }
        
        SETTINGS_FILE="$VSCODE_PATH/settings.json"
        # 备份现有设置
        if [ -f "$SETTINGS_FILE" ]; then
            cp "$SETTINGS_FILE" "$SETTINGS_FILE.backup" 2>/dev/null || true
        fi
        
        # 写入简单配置
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
    else
        echo -e "${GRAY}  ○ Config file not found (skipping)${NC}"
    fi
else
    echo -e "${GRAY}  ○ VSCode not detected (skipping)${NC}"
fi

# Install dependencies
echo ""
echo -e "${CYAN}[5/5] Finalizing...${NC}"
echo -e "${GRAY}  ○ Config files installed${NC}"

# Cleanup
rm -rf "$TEMP_DIR" 2>/dev/null || true

# Complete
echo ""
echo -e "${CYAN}========================================${NC}"
echo -e "${GREEN}   Installation Complete! ✨${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""
echo -e "${YELLOW}📝 Next Steps:${NC}"
if [ -d "$CLAUDE_PATH" ]; then
    echo "  • Restart Claude Desktop to apply new rules"
fi
if [ -d "$VSCODE_PATH" ]; then
    echo "  • Restart VSCode to apply Copilot instructions"
fi
echo ""
echo -e "💡 Tip: Ask Claude 'What coding standards do you follow?'"
echo ""
echo -e "${CYAN}🎉 Thank you for using AI Power Pack v2.4!${NC}"
echo ""
