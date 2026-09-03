#!/bin/bash
set -e

# PhishGuard CLI One-Line Installer
# Author: Moch. Erik Irriansyah (NIM 04123003 — Universitas Narotama)

echo "🛡️ Installing PhishGuard CLI..."

INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"

TARGET="$INSTALL_DIR/phishguard"
URL="https://raw.githubusercontent.com/MochErik/phishguard/main/bin/phishguard"

if command -v curl &> /dev/null; then
    curl -fsSL "$URL" -o "$TARGET"
elif command -v wget &> /dev/null; then
    wget -qO "$TARGET" "$URL"
else
    echo "❌ Error: curl or wget is required."
    exit 1
fi

chmod +x "$TARGET"

# Check if ~/.local/bin is in PATH
SHELL_RC=""
if [ -n "$ZSH_VERSION" ] || [ "$SHELL" = "/bin/zsh" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ] || [ "$SHELL" = "/bin/bash" ]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    if [ -n "$SHELL_RC" ] && [ -f "$SHELL_RC" ]; then
        if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$SHELL_RC"; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
            echo "✅ Added $INSTALL_DIR to PATH in $SHELL_RC"
        fi
    fi
    export PATH="$INSTALL_DIR:$PATH"
fi

echo "✨ PhishGuard CLI installed successfully to $TARGET!"
echo ""
echo "🚀 Cara Menjalankan:"
echo "   phishguard                           # Buka mode interaktif"
echo "   phishguard scan https://domain.xyz  # Pindai tautan URL langsung"
echo "   phishguard text \"pesan scam...\"     # Pindai teks pesan"
echo ""
"$TARGET" -h || true
