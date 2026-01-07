#!/usr/bin/env pwsh
# AI Power Pack v2.4 - Remote Installer
# Usage: iwr -useb https://raw.githubusercontent.com/YOUR_USERNAME/REPO_NAME/main/install.ps1 | iex

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   AI Power Pack v2.4" -ForegroundColor Yellow
Write-Host "   Remote Installer" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "[1/5] Checking Python..." -ForegroundColor Cyan
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  ✓ Python installed: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Python not installed" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python 3.8+ from:" -ForegroundColor Yellow
    Write-Host "https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Download package
Write-Host ""
Write-Host "[2/5] Downloading AI Power Pack..." -ForegroundColor Cyan
$tempDir = Join-Path $env:TEMP "ai_power_pack"
$zipUrl = "https://github.com/GQSDGQWE/AIDevKit/archive/refs/heads/main.zip"

try {
    if (Test-Path $tempDir) { Remove-Item $tempDir -Recurse -Force }
    New-Item -ItemType Directory -Path $tempDir | Out-Null
    
    $zipFile = Join-Path $tempDir "package.zip"
    Invoke-WebRequest -Uri $zipUrl -OutFile $zipFile -UseBasicParsing
    
    Expand-Archive -Path $zipFile -DestinationPath $tempDir -Force
    $extractedDir = Get-ChildItem $tempDir -Directory | Select-Object -First 1
    
    Write-Host "  ✓ Package downloaded" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Download failed: $_" -ForegroundColor Red
    exit 1
}

# Configure Claude Desktop
Write-Host ""
Write-Host "[3/5] Configuring Claude Desktop..." -ForegroundColor Cyan
$claudePath = Join-Path $env:APPDATA "Claude"
if (Test-Path $claudePath) {
    $claudeMd = Join-Path $extractedDir.FullName "config\CLAUDE.md"
    if (Test-Path $claudeMd) {
        try {
            $configFile = Join-Path $claudePath "claude_desktop_config.json"
            $content = Get-Content -Path $claudeMd -Encoding UTF8 -Raw
            
            $config = @{
                customInstructions = @{
                    global = $content
                    version = "2.4"
                    source = "github"
                    installed = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
                }
            }
            
            $config | ConvertTo-Json -Depth 10 | Set-Content -Path $configFile -Encoding UTF8
            Write-Host "  ✓ Claude Desktop configured" -ForegroundColor Green
        } catch {
            Write-Host "  ✗ Failed: $_" -ForegroundColor Red
        }
    }
} else {
    Write-Host "  ○ Claude Desktop not detected (skipping)" -ForegroundColor Gray
}

# Configure VSCode
Write-Host ""
Write-Host "[4/5] Configuring VSCode..." -ForegroundColor Cyan
$vscodePath = Join-Path $env:APPDATA "Code\User"
if (Test-Path $vscodePath) {
    $copilotMd = Join-Path $extractedDir.FullName "config\copilot-instructions.md"
    if (Test-Path $copilotMd) {
        try {
            $destPath = Join-Path $vscodePath "copilot-instructions.md"
            Copy-Item -Path $copilotMd -Destination $destPath -Force
            
            $settingsFile = Join-Path $vscodePath "settings.json"
            if (Test-Path $settingsFile) {
                $settings = Get-Content $settingsFile -Raw | ConvertFrom-Json
            } else {
                $settings = @{}
            }
            
            $settings | Add-Member -NotePropertyName "github.copilot.chat.codeGeneration.instructions" -NotePropertyValue @(
                @{
                    file = $destPath
                    text = "Follow AI Power Pack v2.4 standards"
                }
            ) -Force
            
            $settings | Add-Member -NotePropertyName "github.copilot.enable" -NotePropertyValue @{
                "*" = $true
                plaintext = $true
                markdown = $true
            } -Force
            
            $settings | ConvertTo-Json -Depth 10 | Set-Content -Path $settingsFile -Encoding UTF8
            Write-Host "  ✓ VSCode configured" -ForegroundColor Green
        } catch {
            Write-Host "  ✗ Failed: $_" -ForegroundColor Red
        }
    }
} else {
    Write-Host "  ○ VSCode not detected (skipping)" -ForegroundColor Gray
}

# Install dependencies
Write-Host ""
Write-Host "[5/5] Installing Python dependencies..." -ForegroundColor Cyan
Write-Host "  ○ Skipping (only config files installed)" -ForegroundColor Gray

# Cleanup
if (Test-Path $tempDir) { Remove-Item $tempDir -Recurse -Force }

# Complete
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Installation Complete! ✨" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📝 Next Steps:" -ForegroundColor Yellow
if (Test-Path (Join-Path $env:APPDATA "Claude")) {
    Write-Host "  • Restart Claude Desktop to apply new rules"
}
if (Test-Path (Join-Path $env:APPDATA "Code\User")) {
    Write-Host "  • Restart VSCode to apply Copilot instructions"
}
Write-Host ""
Write-Host "💡 Tip: Ask Claude 'What coding standards do you follow?'" -ForegroundColor Gray
Write-Host ""
Write-Host "🎉 Thank you for using AI Power Pack v2.4!" -ForegroundColor Cyan
Write-Host ""
