#!/usr/bin/env pwsh
# AI Power Pack v2.4 - Remote Installer
# Usage: iwr -useb https://raw.githubusercontent.com/GQSDGQWE/AIDevKit/main/install.ps1 | iex

$ErrorActionPreference = 'SilentlyContinue'
$ProgressPreference = 'SilentlyContinue'

# 超时执行函数（防止卡住）
function Invoke-WithTimeout {
    param(
        [ScriptBlock]$ScriptBlock,
        [int]$TimeoutSeconds = 10
    )
    
    $job = Start-Job -ScriptBlock $ScriptBlock
    $completed = Wait-Job -Job $job -Timeout $TimeoutSeconds
    
    if ($completed) {
        $result = Receive-Job -Job $job
        Remove-Job -Job $job -Force
        return $result
    } else {
        Remove-Job -Job $job -Force
        throw "Operation timed out after $TimeoutSeconds seconds"
    }
}

# Check if running as administrator
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   AI Power Pack v2.4" -ForegroundColor Yellow
Write-Host "   Remote Installer" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if (-not $isAdmin) {
    Write-Host "Note: Not running as administrator" -ForegroundColor Yellow
    Write-Host "      Some operations may require admin rights" -ForegroundColor Gray
    Write-Host ""
}

# Check Python (optional)
Write-Host "[1/5] Checking Python..." -ForegroundColor Cyan
try {
    $pythonCheck = & python --version 2>&1
    if ($pythonCheck) {
        Write-Host "  ✓ Python detected" -ForegroundColor Green
    } else {
        Write-Host "  ○ Python not detected (optional)" -ForegroundColor Gray
    }
} catch {
    Write-Host "  ○ Python not detected (optional)" -ForegroundColor Gray
}

# Download package
Write-Host ""
Write-Host "[2/5] Downloading AI Power Pack..." -ForegroundColor Cyan
$tempDir = Join-Path $env:TEMP "ai_power_pack_$(Get-Random)"
$zipUrl = "https://github.com/GQSDGQWE/AIDevKit/archive/refs/heads/main.zip"

try {
    New-Item -ItemType Directory -Path $tempDir -Force | Out-Null
    
    $zipFile = Join-Path $tempDir "package.zip"
    Write-Host "  → Downloading from GitHub..." -ForegroundColor Gray
    
    # 使用 WebClient 更可靠
    $webClient = New-Object System.Net.WebClient
    $webClient.DownloadFile($zipUrl, $zipFile)
    $webClient.Dispose()
    
    Write-Host "  → Extracting..." -ForegroundColor Gray
    Expand-Archive -Path $zipFile -DestinationPath $tempDir -Force
    $extractedDir = Get-ChildItem $tempDir -Directory | Select-Object -First 1
    
    Write-Host "  ✓ Package downloaded" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Download failed: $($_.Exception.Message)" -ForegroundColor Red
    if (Test-Path $tempDir) { Remove-Item $tempDir -Recurse -Force -ErrorAction SilentlyContinue }
    Write-Host ""
    Write-Host "Please check your internet connection and try again." -ForegroundColor Yellow
    exit 1
}

# Configure Claude Desktop
Write-Host ""
Write-Host "[3/5] Configuring Claude Desktop..." -ForegroundColor Cyan
$claudePath = Join-Path $env:APPDATA "Claude"

try {
    if (Test-Path $claudePath) {
        $claudeMd = Join-Path $extractedDir.FullName "config\CLAUDE.md"
        if (Test-Path $claudeMd) {
            Write-Host "  → Reading config file..." -ForegroundColor Gray
            $configFile = Join-Path $claudePath "claude_desktop_config.json"
            
            # 确保目录存在且可写
            if (-not (Test-Path $claudePath)) {
                New-Item -ItemType Directory -Path $claudePath -Force | Out-Null
            }
            
            # 测试写入权限
            $testFile = Join-Path $claudePath "test_write.tmp"
            try {
                [System.IO.File]::WriteAllText($testFile, "test", [System.Text.Encoding]::UTF8)
                Remove-Item $testFile -Force -ErrorAction SilentlyContinue
            } catch {
                Write-Host "  ○ No write permission to Claude folder (skipping)" -ForegroundColor Gray
                throw "No write permission"
            }
            
            Write-Host "  → Creating configuration..." -ForegroundColor Gray
            $content = [System.IO.File]::ReadAllText($claudeMd, [System.Text.Encoding]::UTF8)
            
            # 转义特殊字符
            $escapedContent = $content -replace '\\', '\\' -replace '"', '\"' -replace "`r", '' -replace "`n", '\n' -replace "`t", '\t'
            
            $jsonContent = @"
{
  "customInstructions": {
    "global": "$escapedContent",
    "version": "2.4",
    "source": "github"
  }
}
"@
            
            Write-Host "  → Writing to $configFile..." -ForegroundColor Gray
            [System.IO.File]::WriteAllText($configFile, $jsonContent, [System.Text.Encoding]::UTF8)
            Write-Host "  ✓ Claude Desktop configured" -ForegroundColor Green
        } else {
            Write-Host "  ○ Config file not found (skipping)" -ForegroundColor Gray
        }
    } else {
        Write-Host "  ○ Claude Desktop not detected (skipping)" -ForegroundColor Gray
    }
} catch {
    Write-Host "  ○ Claude config skipped: $($_.Exception.Message)" -ForegroundColor Gray
}

# Configure VSCode
Write-Host ""
Write-Host "[4/5] Configuring VSCode..." -ForegroundColor Cyan
$vscodePath = Join-Path $env:APPDATA "Code\User"

try {
    if (Test-Path $vscodePath) {
        $copilotMd = Join-Path $extractedDir.FullName "config\copilot-instructions.md"
        if (Test-Path $copilotMd) {
            Write-Host "  → Copying config file..." -ForegroundColor Gray
            
            # 测试写入权限
            $testFile = Join-Path $vscodePath "test_write.tmp"
            try {
                [System.IO.File]::WriteAllText($testFile, "test", [System.Text.Encoding]::UTF8)
                Remove-Item $testFile -Force -ErrorAction SilentlyContinue
            } catch {
                Write-Host "  ○ No write permission to VSCode folder (skipping)" -ForegroundColor Gray
                throw "No write permission"
            }
            
            # 复制配置文件
            $destPath = Join-Path $vscodePath "copilot-instructions.md"
            Copy-Item -Path $copilotMd -Destination $destPath -Force
            
            Write-Host "  → Updating settings..." -ForegroundColor Gray
            # 更新 settings.json
            $settingsFile = Join-Path $vscodePath "settings.json"
            $settingsContent = @"
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
"@
            
            # 如果已有 settings.json，备份
            if (Test-Path $settingsFile) {
                Copy-Item -Path $settingsFile -Destination "$settingsFile.backup" -Force -ErrorAction SilentlyContinue
            }
            
            [System.IO.File]::WriteAllText($settingsFile, $settingsContent, [System.Text.Encoding]::UTF8)
            Write-Host "  ✓ VSCode configured" -ForegroundColor Green
        } else {
            Write-Host "  ○ Config file not found (skipping)" -ForegroundColor Gray
        }
    } else {
        Write-Host "  ○ VSCode not detected (skipping)" -ForegroundColor Gray
    }
} catch {
    Write-Host "  ○ VSCode config skipped: $($_.Exception.Message)" -ForegroundColor Gray
}

# Install dependencies
Write-Host ""
Write-Host "[5/5] Finalizing..." -ForegroundColor Cyan
Write-Host "  ○ Config files installed" -ForegroundColor Gray

# Cleanup
try {
    if (Test-Path $tempDir) { 
        Remove-Item $tempDir -Recurse -Force -ErrorAction SilentlyContinue 
    }
} catch {
    # Ignore cleanup errors
}

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
