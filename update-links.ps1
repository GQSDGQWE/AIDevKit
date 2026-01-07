# AI Power Pack - GitHub 链接更新脚本
# 自动替换所有安装文件中的占位符

param(
    [string]$Username = "YOUR_USERNAME",
    [string]$RepoName = "REPO_NAME"
)

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  AI Power Pack - 链接更新工具" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# 检查参数
if ($Username -eq "YOUR_USERNAME" -or $RepoName -eq "REPO_NAME") {
    Write-Host "请输入您的 GitHub 信息：" -ForegroundColor Yellow
    Write-Host ""
    
    $Username = Read-Host "GitHub 用户名"
    $RepoName = Read-Host "仓库名称"
    
    if ([string]::IsNullOrWhiteSpace($Username) -or [string]::IsNullOrWhiteSpace($RepoName)) {
        Write-Host ""
        Write-Host "❌ 用户名和仓库名不能为空！" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "📝 配置信息：" -ForegroundColor Green
Write-Host "   用户名: $Username" -ForegroundColor White
Write-Host "   仓库名: $RepoName" -ForegroundColor White
Write-Host "   完整 URL: https://github.com/$Username/$RepoName" -ForegroundColor White
Write-Host ""

# 确认
$confirm = Read-Host "确认更新？(Y/N)"
if ($confirm -ne "Y" -and $confirm -ne "y") {
    Write-Host "已取消操作。" -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "🔄 开始更新文件..." -ForegroundColor Cyan
Write-Host ""

# 需要更新的文件列表
$files = @(
    "install.ps1",
    "install.sh",
    "README.md",
    "QUICK_INSTALL.md"
)

$updatedCount = 0
$failedFiles = @()

foreach ($file in $files) {
    if (Test-Path $file) {
        try {
            $content = Get-Content $file -Raw -Encoding UTF8
            $originalContent = $content
            
            # 替换占位符
            $content = $content -replace "YOUR_USERNAME/REPO_NAME", "$Username/$RepoName"
            $content = $content -replace "YOUR_USERNAME", $Username
            $content = $content -replace "REPO_NAME", $RepoName
            
            # 只有内容改变时才写入
            if ($content -ne $originalContent) {
                $content | Set-Content $file -Encoding UTF8 -NoNewline
                Write-Host "  ✓ $file" -ForegroundColor Green
                $updatedCount++
            } else {
                Write-Host "  ○ $file (无需更新)" -ForegroundColor Gray
            }
        } catch {
            Write-Host "  ✗ $file (失败: $_)" -ForegroundColor Red
            $failedFiles += $file
        }
    } else {
        Write-Host "  ? $file (文件不存在)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan

if ($failedFiles.Count -eq 0) {
    Write-Host "✨ 更新完成！" -ForegroundColor Green
    Write-Host "   已更新 $updatedCount 个文件" -ForegroundColor White
    Write-Host ""
    Write-Host "📤 下一步：提交到 GitHub" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "运行以下命令：" -ForegroundColor Cyan
    Write-Host "   git add install.ps1 install.sh README.md QUICK_INSTALL.md" -ForegroundColor White
    Write-Host "   git commit -m `"fix: 更新安装链接为实际仓库地址`"" -ForegroundColor White
    Write-Host "   git push origin main" -ForegroundColor White
    Write-Host ""
    Write-Host "🎯 分发命令：" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Windows:" -ForegroundColor Cyan
    Write-Host "   iwr -useb https://raw.githubusercontent.com/$Username/$RepoName/main/install.ps1 | iex" -ForegroundColor White
    Write-Host ""
    Write-Host "macOS/Linux:" -ForegroundColor Cyan
    Write-Host "   curl -fsSL https://raw.githubusercontent.com/$Username/$RepoName/main/install.sh | bash" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host "⚠️  更新完成，但有错误" -ForegroundColor Yellow
    Write-Host "   成功: $updatedCount 个文件" -ForegroundColor Green
    Write-Host "   失败: $($failedFiles.Count) 个文件" -ForegroundColor Red
    Write-Host ""
    Write-Host "失败的文件：" -ForegroundColor Red
    foreach ($f in $failedFiles) {
        Write-Host "   - $f" -ForegroundColor Red
    }
}

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
