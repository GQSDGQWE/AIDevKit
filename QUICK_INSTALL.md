# 🚀 AI Power Pack v2.4 - 一键安装

## 快速安装（推荐）

### Windows (PowerShell)
```powershell
iwr -useb https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.ps1 | iex
```

### macOS / Linux (Bash)
```bash
curl -fsSL https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.sh | bash
```

---

## 🎯 使用说明

### 第 1 步：运行安装命令

根据您的操作系统选择对应命令：

**Windows 用户：**
1. 按 `Win + X`，选择 "Windows PowerShell (管理员)"
2. 复制粘贴以下命令：
```powershell
iwr -useb https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.ps1 | iex
```
3. 按回车执行

**macOS / Linux 用户：**
1. 打开终端
2. 复制粘贴以下命令：
```bash
curl -fsSL https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.sh | bash
```
3. 按回车执行

### 第 2 步：重启应用

安装完成后，重启以下应用：
- Claude Desktop
- VSCode

### 第 3 步：验证安装

**测试 Claude Desktop：**
```
问：你遵循什么开发标准？
答：应该提到 AI Power Pack v2.4
```

**测试 VSCode Copilot：**
- 生成任意代码
- 检查是否符合规范（PLAN-EXECUTE 模式、错误处理等）

---

## 📋 安装过程

安装脚本会自动完成以下步骤：

1. ✅ 检查 Python 安装
2. ✅ 从 GitHub 下载最新版本
3. ✅ 配置 Claude Desktop
4. ✅ 配置 VSCode
5. ✅ 安装 Python 依赖

---

## 🔧 手动安装（备选方案）

如果一键安装失败，可以手动安装：

### 方式 1：克隆仓库
```bash
# 克隆项目
git clone https://github.com/Buxiaomaomaozi/CONSOL.git
cd REPO_NAME

# Windows
.\AI-Power-Pack-Installer.bat

# macOS/Linux
python3 tools/deploy_config.py
```

### 方式 2：下载 ZIP
1. 访问 [GitHub 仓库](https://github.com/Buxiaomaomaozi/CONSOL)
2. 点击 "Code" → "Download ZIP"
3. 解压后运行 `INSTALL.bat` (Windows) 或 `install.py` (macOS/Linux)

---

## 💡 常见问题

### Q: 执行策略错误？
**A (Windows):** 如果遇到 "无法加载，因为在此系统上禁止运行脚本"：
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```

### Q: Python 未安装？
**A:** 从 https://www.python.org/downloads/ 下载安装 Python 3.8+

### Q: Claude 或 VSCode 未检测到？
**A:** 安装脚本会自动跳过未安装的应用，不会报错。安装后再运行一次即可。

### Q: 配置未生效？
**A:** 
1. 确保完全关闭 Claude Desktop 和 VSCode
2. 重新运行安装命令
3. 重启应用

---

## 🌐 替代安装链接

如果 GitHub raw 链接无法访问，可以使用：

**jsdelivr CDN (Windows):**
```powershell
iwr -useb https://cdn.jsdelivr.net/gh/Buxiaomaomaozi/CONSOL@main/install.ps1 | iex
```

**jsdelivr CDN (macOS/Linux):**
```bash
curl -fsSL https://cdn.jsdelivr.net/gh/Buxiaomaomaozi/CONSOL@main/install.sh | bash
```

---

## 📦 项目内容

安装后您将获得：

- ✅ **Claude Desktop 配置** - AI Power Pack v2.4 全局规则
- ✅ **VSCode Copilot 配置** - GitHub Copilot 指令
- ✅ **示例项目** - Cognis Vault, Aether Engine
- ✅ **示例应用** - 6 个完整的应用案例
- ✅ **完整文档** - 部署指南、Git 工作流等
- ✅ **自动化工具** - 清理、打包、部署工具

---

## 🔄 更新

要更新到最新版本，重新运行安装命令即可：

```powershell
# Windows
iwr -useb https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.ps1 | iex
```

```bash
# macOS/Linux
curl -fsSL https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.sh | bash
```

---

## 📚 更多信息

- **GitHub 仓库**: https://github.com/Buxiaomaomaozi/CONSOL
- **详细文档**: [README.md](README.md)
- **部署指南**: [docs/DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md)
- **问题反馈**: [GitHub Issues](https://github.com/Buxiaomaomaozi/CONSOL/issues)

---

## ⚙️ 系统要求

- **操作系统**: Windows 10/11, macOS 10.15+, Linux (Ubuntu 20.04+)
- **Python**: 3.8 或更高版本
- **可选**: Claude Desktop, VSCode (至少需要其中之一)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

**🎉 一行命令，开启 AI 增强开发之旅！**

```powershell
# Windows
iwr -useb https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.ps1 | iex
```

```bash
# macOS/Linux
curl -fsSL https://raw.githubusercontent.com/Buxiaomaomaozi/CONSOL/main/install.sh | bash
```

---

Made with ❤️ by CONSOL Team | 2026
