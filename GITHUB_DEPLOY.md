# 📝 GitHub 部署指南

## 🎯 将项目上传到 GitHub 后的使用说明

### 第 1 步：完成 GitHub 上传

确保您已经将项目推送到 GitHub：

```bash
# 如果还没有推送，执行以下命令：
git add .
git commit -m "feat: AI Power Pack v2.4 - 完整版本"
git push origin main
```

### 第 2 步：获取您的仓库信息

访问您的 GitHub 仓库，复制以下信息：
- **用户名**: 例如 `Buxiaomaomaozi`
- **仓库名**: 例如 `CONSOL` 或 `ai-power-pack`

完整 URL 格式：`https://github.com/用户名/仓库名`

### 第 3 步：更新安装链接

需要更新以下文件中的 `YOUR_USERNAME/REPO_NAME`：

#### 文件 1: `install.ps1`
```powershell
# 第 24 行，将：
$zipUrl = "https://github.com/YOUR_USERNAME/REPO_NAME/archive/refs/heads/main.zip"

# 改为：
$zipUrl = "https://github.com/Buxiaomaomaozi/CONSOL/archive/refs/heads/main.zip"
```

#### 文件 2: `install.sh`
```bash
# 第 30 行，将：
ZIP_URL="https://github.com/YOUR_USERNAME/REPO_NAME/archive/refs/heads/main.zip"

# 改为：
ZIP_URL="https://github.com/Buxiaomaomaozi/CONSOL/archive/refs/heads/main.zip"
```

#### 文件 3: `README.md`
更新安装命令中的链接。

#### 文件 4: `QUICK_INSTALL.md`
更新所有安装命令和链接。

### 第 4 步：重新提交

```bash
# 更新后重新提交
git add install.ps1 install.sh README.md QUICK_INSTALL.md
git commit -m "fix: 更新安装链接为实际仓库地址"
git push origin main
```

---

## 🚀 分发给用户

更新完成后，用户只需运行一行命令即可安装：

### Windows 用户
```powershell
iwr -useb https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.ps1 | iex
```

### macOS / Linux 用户
```bash
curl -fsSL https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.sh | bash
```

---

## 📋 快速替换脚本

使用以下 PowerShell 脚本快速替换所有文件中的占位符：

```powershell
# 设置您的 GitHub 信息
$username = "Buxiaomaomaozi"  # 替换为您的 GitHub 用户名
$reponame = "CONSOL"          # 替换为您的仓库名

# 替换文件中的占位符
$files = @(
    "install.ps1",
    "install.sh",
    "README.md",
    "QUICK_INSTALL.md"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        (Get-Content $file -Raw) `
            -replace "YOUR_USERNAME/REPO_NAME", "$username/$reponame" `
            -replace "YOUR_USERNAME", $username `
            -replace "REPO_NAME", $reponame |
        Set-Content $file -NoNewline
        Write-Host "✓ 已更新 $file" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "✨ 所有文件已更新完成！" -ForegroundColor Cyan
Write-Host ""
Write-Host "现在提交更改：" -ForegroundColor Yellow
Write-Host "git add install.ps1 install.sh README.md QUICK_INSTALL.md"
Write-Host "git commit -m 'fix: 更新安装链接为实际仓库地址'"
Write-Host "git push origin main"
```

保存为 `update-links.ps1` 并运行：
```powershell
.\update-links.ps1
```

---

## 🎯 验证安装链接

确保以下 URL 可以访问：

1. **PowerShell 安装脚本**
   ```
   https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.ps1
   ```

2. **Bash 安装脚本**
   ```
   https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.sh
   ```

3. **ZIP 下载**
   ```
   https://github.com/Buxiaomaomaozi/CONSOL/archive/refs/heads/main.zip
   ```

在浏览器中访问这些链接，确保都能正常访问。

---

## 📝 在 README 中添加徽章（可选）

在 README.md 顶部添加：

```markdown
[![GitHub Stars](https://img.shields.io/github/stars/Buxiaomaomaozi/CONSOL?style=social)](https://github.com/Buxiaomaomaozi/CONSOL)
[![GitHub Forks](https://img.shields.io/github/forks/Buxiaomaomaozi/CONSOL?style=social)](https://github.com/Buxiaomaomaozi/CONSOL/fork)
[![GitHub Issues](https://img.shields.io/github/issues/Buxiaomaomaozi/CONSOL)](https://github.com/Buxiaomaomaozi/CONSOL/issues)
```

---

## 🌐 使用 CDN 加速（可选）

如果 GitHub raw 链接访问慢，可以使用 jsdelivr CDN：

### Windows
```powershell
iwr -useb https://cdn.jsdelivr.net/gh/Buxiaomaomaozi/CONSOL@main/install.ps1 | iex
```

### macOS / Linux
```bash
curl -fsSL https://cdn.jsdelivr.net/gh/Buxiaomaomaozi/CONSOL@main/install.sh | bash
```

---

## 📢 分发建议

### 1. GitHub README
在仓库 README 顶部突出显示一键安装命令

### 2. GitHub Releases
创建 Release 并附加 ZIP 包：
```bash
# 创建标签
git tag -a v2.4.0 -m "AI Power Pack v2.4.0"
git push origin v2.4.0

# 在 GitHub 创建 Release
# 上传 dist/packages/AI_Power_Pack_v2.4_*.zip
```

### 3. 社交媒体
分享安装命令：
```
🚀 AI Power Pack v2.4 现已发布！

一行命令即可安装，将 AI 助手提升为专业级工程师！

Windows:
iwr -useb https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.ps1 | iex

macOS/Linux:
curl -fsSL https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.sh | bash

⭐ GitHub: https://github.com/Buxiaomaomaozi/CONSOL
```

---

## ✅ 检查清单

部署前确保：

- [ ] 已将代码推送到 GitHub
- [ ] 已更新所有文件中的 `YOUR_USERNAME/REPO_NAME`
- [ ] 已验证 raw URL 可以访问
- [ ] 已测试安装脚本
- [ ] 已更新 README 的安装说明
- [ ] 已创建 GitHub Release（可选）
- [ ] 已添加 GitHub 徽章（可选）

---

## 🎉 完成！

现在用户可以通过一行命令安装您的 AI Power Pack！

**Windows:**
```powershell
iwr -useb https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.ps1 | iex
```

**macOS/Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.sh | bash
```

简单、快速、专业！✨
