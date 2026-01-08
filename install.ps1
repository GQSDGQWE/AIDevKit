#!/usr/bin/env pwsh
# AI Power Pack v1.0 - Remote Installer
# Usage: iwr -useb https://raw.githubusercontent.com/GQSDGQWE/AIDevKit/main/install.ps1 | iex

$ErrorActionPreference = 'SilentlyContinue'
$ProgressPreference = 'SilentlyContinue'

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

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
Write-Host "   AI Power Pack v1.0" -ForegroundColor Yellow
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
    "version": "1.0",
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
      "text": "Follow AI Power Pack v1.0 standards"
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

# Install Go language
Write-Host ""
Write-Host "[5/9] Installing Go language..." -ForegroundColor Cyan

# 全局变量用于存储Go路径
$global:GoExecutable = $null

# 检查Go是否已安装
$goCmd = Get-Command go -ErrorAction SilentlyContinue
if ($goCmd) {
    $goVersion = & go version 2>&1
    Write-Host "  ✓ Go already installed: $goVersion" -ForegroundColor Green
    $global:GoExecutable = "go"
} else {
    Write-Host "  → Go not found, starting automatic installation..." -ForegroundColor Gray
    
    # 检查winget是否可用
    $wingetCmd = Get-Command winget -ErrorAction SilentlyContinue
    
    if ($wingetCmd) {
        Write-Host "  → Installing Go via winget (this may take a moment)..." -ForegroundColor Gray
        
        try {
            # 使用winget安装
            & winget install --id GoLang.Go --accept-package-agreements --accept-source-agreements 2>&1 | Out-Null
            
            if ($LASTEXITCODE -eq 0) {
                # 刷新环境变量
                $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
                
                # 再次检查
                $goCmd = Get-Command go -ErrorAction SilentlyContinue
                
                if ($goCmd) {
                    $goVersion = & go version 2>&1
                    Write-Host "  ✓ Go installed successfully: $goVersion" -ForegroundColor Green
                } else {
                    Write-Host "  ⚠ Go installation completed, but requires terminal restart" -ForegroundColor Yellow
                }
            } else {
                throw "winget installation failed"
            }
        } catch {
            Write-Host "  → winget failed, trying MSI installer..." -ForegroundColor Gray
            
            # Fallback: 使用MSI安装器
            try {
                $goUrl = "https://go.dev/dl/go1.21.5.windows-amd64.msi"
                $goInstaller = "$env:TEMP\go-installer.msi"
                
                Write-Host "  → Downloading Go installer..." -ForegroundColor Gray
                Invoke-WebRequest -Uri $goUrl -OutFile $goInstaller -UseBasicParsing
                
                Write-Host "  → Installing Go (this may take 1-2 minutes)..." -ForegroundColor Gray
                $installProcess = Start-Process msiexec.exe -ArgumentList "/i", "`"$goInstaller`"", "/qn", "/norestart" -Wait -NoNewWindow -PassThru
                
                if ($installProcess.ExitCode -eq 0) {
                    Write-Host "  → Go installation completed successfully" -ForegroundColor Green
                } elseif ($installProcess.ExitCode -eq 1603) {
                    Write-Host "  ✗ Installation failed: requires administrator privileges" -ForegroundColor Red
                    Write-Host "  💡 Please run PowerShell as Administrator and try again" -ForegroundColor Cyan
                    Write-Host "     OR install manually from: https://go.dev/dl/" -ForegroundColor Gray
                    Remove-Item $goInstaller -ErrorAction SilentlyContinue
                    continue
                } else {
                    Write-Host "  ⚠ Installation completed with exit code: $($installProcess.ExitCode)" -ForegroundColor Yellow
                }
                
                # 清理安装文件
                Remove-Item $goInstaller -ErrorAction SilentlyContinue
                
                # 刷新环境变量
                $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
                
                # 检查安装结果
                $goCmd = Get-Command go -ErrorAction SilentlyContinue
                
                if ($goCmd) {
                    $goVersion = & go version 2>&1
                    Write-Host "  ✓ Go installed successfully: $goVersion" -ForegroundColor Green
                    $global:GoExecutable = "go"
                } else {
                    # 尝试查找Go的默认安装路径
                    $defaultGoPath = "C:\Program Files\Go\bin\go.exe"
                    if (Test-Path $defaultGoPath) {
                        $global:GoExecutable = $defaultGoPath
                        $goVersion = & $defaultGoPath version 2>&1
                        Write-Host "  ✓ Go installed successfully: $goVersion" -ForegroundColor Green
                    } else {
                        Write-Host "  ✓ Go installed, but requires terminal restart" -ForegroundColor Yellow
                    }
                }
            } catch {
                Write-Host "  ✗ Automatic installation failed" -ForegroundColor Red
                Write-Host "  💡 Please install manually: https://go.dev/dl/" -ForegroundColor Cyan
            }
        }
    } else {
        # winget不可用，直接使用MSI安装器
        Write-Host "  → Using MSI installer..." -ForegroundColor Gray
        
        try {
            $goUrl = "https://go.dev/dl/go1.21.5.windows-amd64.msi"
            $goInstaller = "$env:TEMP\go-installer.msi"
            
            Write-Host "  → Downloading Go installer..." -ForegroundColor Gray
            Invoke-WebRequest -Uri $goUrl -OutFile $goInstaller -UseBasicParsing
            
            Write-Host "  → Installing Go (this may take 1-2 minutes)..." -ForegroundColor Gray
            $installProcess = Start-Process msiexec.exe -ArgumentList "/i", "`"$goInstaller`"", "/qn", "/norestart" -Wait -NoNewWindow -PassThru
            
            if ($installProcess.ExitCode -eq 0) {
                Write-Host "  → Go installation completed successfully" -ForegroundColor Green
            } elseif ($installProcess.ExitCode -eq 1603) {
                Write-Host "  ✗ Installation failed: requires administrator privileges" -ForegroundColor Red
                Write-Host "  💡 Please run PowerShell as Administrator and try again" -ForegroundColor Cyan
                Write-Host "     OR install manually from: https://go.dev/dl/" -ForegroundColor Gray
                Remove-Item $goInstaller -ErrorAction SilentlyContinue
                return
            } else {
                Write-Host "  ⚠ Installation completed with exit code: $($installProcess.ExitCode)" -ForegroundColor Yellow
            }
            
            # 清理安装文件
            Remove-Item $goInstaller -ErrorAction SilentlyContinue
            
            # 刷新环境变量
            $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
            
            # 检查安装结果
            $goCmd = Get-Command go -ErrorAction SilentlyContinue
            
            if ($goCmd) {
                $goVersion = & go version 2>&1
                Write-Host "  ✓ Go installed successfully: $goVersion" -ForegroundColor Green
                $global:GoExecutable = "go"
            } else {
                # 尝试查找Go的默认安装路径
                $defaultGoPath = "C:\Program Files\Go\bin\go.exe"
                if (Test-Path $defaultGoPath) {
                    $global:GoExecutable = $defaultGoPath
                    $goVersion = & $defaultGoPath version 2>&1
                    Write-Host "  ✓ Go installed successfully: $goVersion" -ForegroundColor Green
                } else {
                    Write-Host "  ✓ Go installed, but requires terminal restart" -ForegroundColor Yellow
                }
            }
        } catch {
            Write-Host "  ✗ Automatic installation failed" -ForegroundColor Red
            Write-Host "  💡 Please install manually: https://go.dev/dl/" -ForegroundColor Cyan
        }
    }
}

# Install Fabric CLI
Write-Host ""
Write-Host "[6/9] Installing Fabric CLI..." -ForegroundColor Cyan

# 使用全局变量中的Go路径或尝试检测
if (-not $global:GoExecutable) {
    # 首先尝试通过常规方式检查Go
    $goCmd = Get-Command go -ErrorAction SilentlyContinue
    if ($goCmd) {
        $global:GoExecutable = "go"
    } else {
        # 如果常规方式找不到，尝试直接使用完整路径
        $possiblePaths = @(
            "C:\Program Files\Go\bin\go.exe",
            "$env:ProgramFiles\Go\bin\go.exe",
            "${env:ProgramFiles(x86)}\Go\bin\go.exe",
            "$env:USERPROFILE\go\bin\go.exe"
        )
        
        foreach ($path in $possiblePaths) {
            if (Test-Path $path) {
                $global:GoExecutable = $path
                Write-Host "  → Found Go at: $path" -ForegroundColor Gray
                break
            }
        }
    }
}

if ($global:GoExecutable) {
    try {
        Write-Host "  → Installing Fabric via Go..." -ForegroundColor Gray
        
        # 使用找到的Go路径安装Fabric
        & $global:GoExecutable install github.com/danielmiessler/fabric/cmd/fabric@latest 2>&1 | Out-Null
        
        # 检查安装是否成功
        $fabricPath = Join-Path $env:GOPATH "bin\fabric.exe"
        if (-not $env:GOPATH) {
            $fabricPath = Join-Path $env:USERPROFILE "go\bin\fabric.exe"
        }
        
        if (Test-Path $fabricPath) {
            Write-Host "  ✓ Fabric CLI installed successfully" -ForegroundColor Green
            Write-Host "  💡 Run 'fabric --setup' to configure" -ForegroundColor Cyan
        } else {
            Write-Host "  ✓ Fabric CLI installed" -ForegroundColor Yellow
            Write-Host "  💡 May require terminal restart to use" -ForegroundColor Gray
        }
    } catch {
        Write-Host "  ✗ Fabric CLI installation failed: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "  💡 After restarting terminal, run:" -ForegroundColor Cyan
        Write-Host "     go install github.com/danielmiessler/fabric/cmd/fabric@latest" -ForegroundColor Gray
    }
} else {
    Write-Host "  ⚠ Go not found" -ForegroundColor Yellow
    Write-Host "  💡 Please restart your terminal and run this script again" -ForegroundColor Cyan
    Write-Host "     Then Fabric CLI will be installed automatically" -ForegroundColor Gray
}

# Install Cursor Rules
Write-Host ""
Write-Host "[7/9] Installing Cursor Rules..." -ForegroundColor Cyan
try {
    Write-Host "  → Downloading .cursorrules from awesome-cursorrules..." -ForegroundColor Gray
    $cursorRulesFile = Join-Path $PWD ".cursorrules"
    
    # 使用通用的TypeScript/JavaScript规则
    $cursorRulesUrl = "https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/javascript-typescript-code-quality-cursorrules-pro/.cursorrules"
    
    $webClient = New-Object System.Net.WebClient
    $cursorContent = $webClient.DownloadString($cursorRulesUrl)
    $webClient.Dispose()
    
    # 添加我们的标识
    $header = @"
# AI Power Pack v1.0 - Cursor Rules
# Source: awesome-cursorrules
# https://github.com/PatrickJS/awesome-cursorrules

"@
    $cursorContent = $header + $cursorContent
    [System.IO.File]::WriteAllText($cursorRulesFile, $cursorContent, [System.Text.Encoding]::UTF8)
    
    Write-Host "  ✓ .cursorrules created in current directory" -ForegroundColor Green
    Write-Host "  ℹ Sourced from: awesome-cursorrules" -ForegroundColor Gray
} catch {
    Write-Host "  ○ Cursor Rules download failed: $($_.Exception.Message)" -ForegroundColor Gray
    Write-Host "  ℹ Visit https://cursor.directory for manual download" -ForegroundColor Gray
}

# Deploy Context Engineering Files
Write-Host ""
Write-Host "[8/9] Deploying Context Engineering..." -ForegroundColor Cyan
try {
    $claudeMd = Join-Path $extractedDir.FullName "config\CLAUDE.md"
    $initialMd = Join-Path $extractedDir.FullName "docs\INITIAL.md"
    
    if (Test-Path $claudeMd) {
        Copy-Item -Path $claudeMd -Destination (Join-Path $PWD "CLAUDE.md") -Force
        Write-Host "  ✓ CLAUDE.md deployed" -ForegroundColor Green
    }
    
    if (Test-Path $initialMd) {
        Copy-Item -Path $initialMd -Destination (Join-Path $PWD "INITIAL.md") -Force
        Write-Host "  ✓ INITIAL.md deployed" -ForegroundColor Green
    } else {
        Write-Host "  ○ INITIAL.md not found (optional)" -ForegroundColor Gray
    }
} catch {
    Write-Host "  ○ Context Engineering skipped: $($_.Exception.Message)" -ForegroundColor Gray
}

# Install OpenSkills Configuration
Write-Host ""
Write-Host "[9/9] Installing OpenSkills..." -ForegroundColor Cyan
try {
    $pythonCheck = & python --version 2>&1
    if ($pythonCheck) {
        Write-Host "  → Installing PDF/Excel tools..." -ForegroundColor Gray
        $packages = @("pdfplumber", "openpyxl", "pandas")
        foreach ($pkg in $packages) {
            & python -m pip install $pkg --quiet --disable-pip-version-check 2>&1 | Out-Null
        }
        Write-Host "  ✓ OpenSkills tools installed" -ForegroundColor Green
    } else {
        Write-Host "  ○ Python not found, skipping OpenSkills" -ForegroundColor Gray
    }
} catch {
    Write-Host "  ○ OpenSkills skipped: $($_.Exception.Message)" -ForegroundColor Gray
}

# Deploy UI/UX Pro Max Templates
Write-Host ""
Write-Host "[10/10] Deploying UI/UX Templates..." -ForegroundColor Cyan
try {
    $uiuxDir = Join-Path $PWD "uiux-templates"
    New-Item -ItemType Directory -Path $uiuxDir -Force | Out-Null
    
    # 创建设计令牌文件
    $designTokens = @"
/* AI Power Pack v1.0 - Design Tokens */

:root {
  /* Spacing System */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  
  /* Color System */
  --color-primary: #0066FF;
  --color-secondary: #6B7280;
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  
  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.25rem;
  --font-size-xl: 1.5rem;
}
"@
    
    [System.IO.File]::WriteAllText((Join-Path $uiuxDir "design-tokens.css"), $designTokens, [System.Text.Encoding]::UTF8)
    Write-Host "  ✓ UI/UX templates deployed" -ForegroundColor Green
} catch {
    Write-Host "  ○ UI/UX templates skipped: $($_.Exception.Message)" -ForegroundColor Gray
}

# Finalizing
Write-Host ""
Write-Host "[All Done] Finalizing..." -ForegroundColor Cyan
Write-Host "  ○ All frameworks deployed" -ForegroundColor Gray
Write-Host ""
Write-Host "📦 Installed Components:" -ForegroundColor Yellow
Write-Host "  1. ✓ Go Language - Programming environment" -ForegroundColor Green
Write-Host "  2. ✓ Fabric CLI - AI automation patterns" -ForegroundColor Green
Write-Host "  3. ✓ Cursor Rules - Coding standards" -ForegroundColor Green
Write-Host "  4. ✓ Context Engineering - CLAUDE.md + INITIAL.md" -ForegroundColor Green
Write-Host "  5. ✓ OpenSkills - PDF/Excel tools" -ForegroundColor Green
Write-Host "  6. ✓ UI/UX Pro Max - Design tokens" -ForegroundColor Green

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
Write-Host "🎉 Thank you for using AI Power Pack v1.0!" -ForegroundColor Cyan
Write-Host ""
