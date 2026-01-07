# 🎁 AI Power Pack v2.4 - 一键安装包使用指南

## 📦 安装包说明

我为您创建了**三种**安装方式，选择最适合您的：

### 方式 1: 本地一键安装（推荐给开发者）✅

**适合：** 已有完整项目文件的用户

**文件：** `AI-Power-Pack-Installer.bat` 或 `AI-Power-Pack-Installer.ps1`

**使用方法：**

#### Windows 批处理版本（简单）
```bash
# 双击运行
AI-Power-Pack-Installer.bat

# 或在命令行运行
.\AI-Power-Pack-Installer.bat
```

#### PowerShell 版本（推荐）
```powershell
# 右键以管理员身份运行 PowerShell
# 然后执行：
.\AI-Power-Pack-Installer.ps1

# 或静默安装
.\AI-Power-Pack-Installer.ps1 -Silent
```

**功能：**
- ✅ 自动检测 Python 安装
- ✅ 自动配置 Claude Desktop
- ✅ 自动配置 VSCode
- ✅ 自动安装 Python 依赖
- ✅ 完整的错误处理

---

### 方式 2: 分发包安装（推荐给最终用户）✅

**适合：** 需要分发给团队或其他用户

**文件：** `dist/packages/AI_Power_Pack_v2.4_*.zip`

**使用方法：**
1. 解压 ZIP 文件
2. 运行 `INSTALL.bat`（Windows）或 `install.py`（跨平台）
3. 重启 Claude Desktop 和 VSCode

**优点：**
- 📦 完整的独立包（74KB）
- 📚 包含所有文档和示例
- 🚀 即插即用

---

### 方式 3: 手动部署（给高级用户）✅

**使用工具脚本：**
```bash
# 清理临时文件
python tools/cleanup.py

# 部署配置
python tools/deploy_config.py

# 打包分发
python tools/package_framework.py
```

---

## 🚀 快速开始指南

### 对于开发者（本地使用）

```bash
# 1. 克隆或下载项目
cd C:\Users\YourName\Desktop\CONSOL

# 2. 运行一键安装
AI-Power-Pack-Installer.bat

# 3. 重启应用
# - Claude Desktop
# - VSCode

# 4. 验证安装
# 打开 Claude，问："你遵循什么开发标准？"
```

### 对于最终用户（接收分发包）

```bash
# 1. 解压收到的 ZIP 文件
AI_Power_Pack_v2.4_*.zip

# 2. 进入解压目录，运行
INSTALL.bat

# 3. 重启应用
# - Claude Desktop
# - VSCode

# 4. 开始使用！
```

---

## 📋 安装包对比

| 特性 | 本地安装器 | 分发 ZIP | 手动部署 |
|------|-----------|---------|---------|
| **易用性** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **适用场景** | 开发环境 | 团队分发 | 高级定制 |
| **文件大小** | 0.43 MB | 74 KB | N/A |
| **需要Python** | ✅ 是 | ✅ 是 | ✅ 是 |
| **包含示例** | ✅ 完整 | ✅ 完整 | ✅ 完整 |
| **自动配置** | ✅ 是 | ✅ 是 | ⚙️ 半自动 |

---

## 🎯 安装步骤详解

### 本地安装器详细步骤

**使用 `AI-Power-Pack-Installer.bat`：**

```
第1步: 检查 Python 安装
  ↓
第2步: 配置 Claude Desktop
  ├─ 检测安装位置
  ├─ 读取 CLAUDE.md
  ├─ 写入配置文件
  └─ 验证配置
  ↓
第3步: 配置 VSCode
  ├─ 检测安装位置
  ├─ 复制 copilot-instructions.md
  ├─ 更新 settings.json
  └─ 验证配置
  ↓
第4步: 安装 Python 依赖
  ├─ requests
  ├─ cryptography
  ├─ pyside6
  ├─ fastapi
  └─ 其他包...
  ↓
完成！重启应用即可使用
```

### PowerShell 安装器详细步骤

**使用 `AI-Power-Pack-Installer.ps1`：**

- ✅ 彩色输出界面
- ✅ 详细的进度显示
- ✅ 完整的错误处理
- ✅ 支持静默安装模式

---

## 💡 常见问题

### Q1: 需要管理员权限吗？
**A:** 建议使用，但不是必须。某些配置可能需要管理员权限。

### Q2: 支持哪些操作系统？
**A:** 
- Windows 10/11 ✅
- macOS（需要使用 Python 版本）✅
- Linux（需要使用 Python 版本）✅

### Q3: 如果 Python 未安装怎么办？
**A:** 安装器会检测并提示。请从 https://www.python.org/downloads/ 下载安装 Python 3.8+

### Q4: Claude 或 VSCode 未安装会怎样？
**A:** 安装器会自动跳过未安装的应用，不会报错。

### Q5: 可以重复安装吗？
**A:** 可以！重复运行会更新配置，不会造成冲突。

### Q6: 如何验证安装成功？
**A:** 
- **Claude**: 问 "你遵循什么开发标准？"
- **VSCode**: 生成代码并检查是否符合规范

---

## 📁 文件清单

### 一键安装器文件
```
CONSOL/
├── AI-Power-Pack-Installer.bat     # Windows 批处理安装器
├── AI-Power-Pack-Installer.ps1     # PowerShell 安装器（推荐）
├── config/                          # 配置文件
│   ├── CLAUDE.md
│   └── copilot-instructions.md
├── tools/                           # 工具脚本
└── dist/packages/                   # 分发包
    └── AI_Power_Pack_v2.4_*.zip
```

### 分发包内容
```
AI_Power_Pack_v2.4_*.zip
├── config/              # 配置文件
├── projects/            # 示例项目
├── showcase/            # 示例应用
├── tools/               # 工具脚本
├── docs/                # 文档
├── INSTALL.bat          # Windows 安装脚本
├── install.py           # Python 安装脚本
├── manifest.json        # 包清单
└── README.md            # 说明文档
```

---

## 🎁 推荐分发方式

### 给开发团队
1. 将整个项目推送到 Git 仓库
2. 团队成员克隆后运行 `AI-Power-Pack-Installer.bat`

### 给非技术用户
1. 发送 `dist/packages/AI_Power_Pack_v2.4_*.zip`
2. 附带简单说明：解压 → 运行 INSTALL.bat → 重启

### 企业内网分发
1. 将 ZIP 包上传到内网服务器
2. 提供下载链接和安装文档

---

## ✨ 安装器特性

### 批处理版本 (`.bat`)
- ✅ 简单直接
- ✅ 双击即可运行
- ✅ 兼容所有 Windows 版本
- ✅ 中英文提示

### PowerShell 版本 (`.ps1`)
- ✅ 彩色界面
- ✅ 更好的错误处理
- ✅ 支持静默模式
- ✅ 详细的进度显示
- ✅ 现代化体验

---

## 🚀 立即使用

### 本地开发者
```bash
# 双击运行
AI-Power-Pack-Installer.bat
```

### 分发给用户
```bash
# 发送这个文件
dist/packages/AI_Power_Pack_v2.4_20260107_161822.zip
```

---

## 📝 更新日志

### v2.4.0 (2026-01-07)
- ✨ 新增一键安装器（批处理版本）
- ✨ 新增一键安装器（PowerShell 版本）
- ✨ 自动化配置部署
- ✨ 自动安装 Python 依赖
- ✨ 完整的错误处理和用户提示

---

**🎉 现在您可以选择最适合的安装方式开始使用 AI Power Pack v2.4！**

- 本地开发：运行 `AI-Power-Pack-Installer.bat`
- 分发给用户：发送 `dist/packages/AI_Power_Pack_v2.4_*.zip`
- 高级定制：使用 `tools/` 中的脚本

💡 推荐：PowerShell 版本提供最佳体验！
