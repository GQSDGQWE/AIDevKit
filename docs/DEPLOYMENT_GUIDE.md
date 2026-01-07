# AI Power Pack v2.4 - 部署指南

## 🚀 快速开始

### 使用一键部署脚本（推荐）

```bash
# Windows
tools\One-Click-Deploy.bat

# 或使用 Python（跨平台）
python tools/deploy_config.py
```

## 📦 工具说明

### 1. cleanup.py - 清理工具
清除项目中的临时文件和构建产物。

**用法：**
```bash
# 基本清理
python tools/cleanup.py

# 完整清理（包括虚拟环境）
python tools/cleanup.py --all

# 指定项目路径
python tools/cleanup.py --path /path/to/project
```

**清理内容：**
- `build/` - 构建产物
- `dist/` - 分发文件
- `__pycache__/` - Python 缓存
- `*.pyc, *.pyo` - 字节码文件
- `*.db` - 测试数据库
- `*.log` - 日志文件
- `*.tmp, *.temp` - 临时文件

### 2. deploy_config.py - 配置部署工具
自动检测并配置 Claude Desktop 和 VSCode。

**用法：**
```bash
python tools/deploy_config.py
```

**功能：**
- ✅ 自动检测 Claude Desktop 安装位置
- ✅ 自动检测 VSCode 安装位置
- ✅ 将规则文件写入相应配置目录
- ✅ 配置 GitHub Copilot 指令
- ✅ 生成配置报告

**配置位置：**
- **Claude Desktop**: `%APPDATA%\Claude\claude_desktop_config.json`
- **VSCode**: `%APPDATA%\Code\User\settings.json`

### 3. package_framework.py - 框架打包工具
将项目打包成可分发的格式。

**用法：**
```bash
python tools/package_framework.py
```

**输出：**
- 目录包：`dist/packages/AI_Power_Pack_v2.4_YYYYMMDD_HHMMSS/`
- ZIP 压缩包：`dist/packages/AI_Power_Pack_v2.4_YYYYMMDD_HHMMSS.zip`

**包含内容：**
```
AI_Power_Pack_v2.4/
├── config/              # 配置文件
│   ├── CLAUDE.md
│   └── copilot-instructions.md
├── projects/            # 项目代码
├── tools/               # 工具脚本
├── docs/                # 文档
├── examples/            # 示例代码
├── mcp-servers/         # MCP 服务器
├── manifest.json        # 清单文件
├── INSTALL.bat          # Windows 安装脚本
├── install.py           # Python 安装脚本
└── README.md            # 说明文档
```

### 4. One-Click-Deploy.bat - 一键部署
交互式部署脚本，提供菜单选择。

**选项：**
1. **完整部署** - 清理 + 打包 + 配置
2. **仅清理** - 删除临时文件
3. **仅打包** - 创建分发包
4. **仅配置** - 部署到 Claude/VSCode

## 🔄 完整部署流程

### 步骤 1: 清理临时内容
```bash
python tools/cleanup.py
```

### 步骤 2: 打包框架
```bash
python tools/package_framework.py
```

### 步骤 3: 部署配置
```bash
python tools/deploy_config.py
```

### 步骤 4: 重启应用
- 重启 Claude Desktop
- 重启 VSCode

## 📋 配置文件说明

### CLAUDE.md
Claude Desktop 的自定义指令文件。

**内容：**
- 全局要求
- 代码质量标准
- PLAN-EXECUTE 模式
- 技术栈配置
- 最佳实践

### copilot-instructions.md
VSCode GitHub Copilot 的指令文件。

**内容：**
- 代码生成规则
- AI 工作流程
- 质量检查清单
- Git 集成指南

## 🔍 验证部署

### 检查 Claude Desktop
1. 打开 Claude Desktop
2. 发送测试消息：`你遵循什么开发标准？`
3. 应该看到 AI Power Pack v2.4 的标准响应

### 检查 VSCode Copilot
1. 打开 VSCode
2. 打开任意代码文件
3. 请求 Copilot 生成代码
4. 应该看到符合 AI Power Pack 标准的代码

### 检查配置文件
```bash
# Windows
dir %APPDATA%\Claude\claude_desktop_config.json
dir %APPDATA%\Code\User\settings.json
dir %APPDATA%\Code\User\copilot-instructions.md
```

## 🛠️ 故障排除

### Python 未找到
```bash
# 检查 Python 安装
python --version

# 如果未安装，下载：
# https://www.python.org/downloads/
```

### Claude Desktop 未检测到
- 确认已安装 Claude Desktop
- 检查安装路径：`%APPDATA%\Claude`
- 手动创建配置文件

### VSCode 未检测到
- 确认已安装 VSCode
- 检查安装路径：`%APPDATA%\Code`
- 重新安装 VSCode

### 配置未生效
1. 完全关闭 Claude Desktop / VSCode
2. 重新运行部署脚本
3. 重启应用
4. 检查配置文件是否存在

## 📚 更多资源

- [项目 README](../README.md)
- [开发指南](../docs/INITIAL.md)
- [Git 指南](../docs/GIT_GUIDE.md)
- [技能部署](../docs/SKILLS_DEPLOYMENT.md)

## 🤝 支持

如有问题，请查看文档或提交 Issue。

---
**AI Power Pack v2.4** - Professional AI Development Framework
