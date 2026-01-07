# AI Power Pack v2.4 - Verification Script

$ErrorActionPreference = 'SilentlyContinue'

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "AI Power Pack v2.4 - Verification" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

$claudeConfig = "$env:APPDATA\Claude\claude_desktop_config.json"
$vscodeInstructions = "$env:APPDATA\Code\User\copilot-instructions.md"
$vscodeSettings = "$env:APPDATA\Code\User\settings.json"

# Check Claude Desktop
Write-Host "[1/2] Checking Claude Desktop..." -ForegroundColor Yellow
if (Test-Path $claudeConfig) {
    try {
        $config = Get-Content $claudeConfig -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($config.customInstructions.global -match "AI Power Pack v2\.4") {
            Write-Host "  OK - Claude configured correctly" -ForegroundColor Green
            Write-Host "  Version: $($config.customInstructions.version)" -ForegroundColor Gray
        } else {
            Write-Host "  ERROR - Configuration incorrect" -ForegroundColor Red
        }
    } catch {
        Write-Host "  ERROR - Cannot read config file" -ForegroundColor Red
    }
} else {
    Write-Host "  SKIP - Claude not installed" -ForegroundColor Yellow
}

# Check VSCode
Write-Host ""
Write-Host "[2/2] Checking VSCode..." -ForegroundColor Yellow
if (Test-Path $vscodeInstructions) {
    $content = Get-Content $vscodeInstructions -Raw -Encoding UTF8
    if ($content -match "AI Power Pack v2\.4") {
        Write-Host "  OK - Copilot instructions configured" -ForegroundColor Green
    } else {
        Write-Host "  ERROR - Instructions incorrect" -ForegroundColor Red
    }
    
    if (Test-Path $vscodeSettings) {
        try {
            $settings = Get-Content $vscodeSettings -Raw -Encoding UTF8 | ConvertFrom-Json
            if ($settings.'github.copilot.chat.codeGeneration.instructions') {
                Write-Host "  OK - settings.json configured" -ForegroundColor Green
            } else {
                Write-Host "  WARN - settings.json not configured" -ForegroundColor Yellow
            }
        } catch {
            Write-Host "  ERROR - Cannot read settings.json" -ForegroundColor Red
        }
    }
} else {
    Write-Host "  SKIP - VSCode not installed" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "Test Instructions" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ask Claude:" -ForegroundColor Yellow
Write-Host "  'What coding standards do you follow?'" -ForegroundColor White
Write-Host ""
Write-Host "Expected answer should include:" -ForegroundColor Gray
Write-Host "  - AI Power Pack v2.4" -ForegroundColor Gray
Write-Host "  - PLAN-EXECUTE pattern" -ForegroundColor Gray
Write-Host "  - 5 Code Quality Standards" -ForegroundColor Gray
Write-Host "  - API-First principle" -ForegroundColor Gray
Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
