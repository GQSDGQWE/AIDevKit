# 🚀 AI Power Pack v2.4 - Professional AI Development Framework

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-v2.4.0-orange.svg)](CHANGELOG)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

> 基于 5 个经实战检验的开源框架，将 AI 助手提升为专业级开发工程师

## ⚡ 一键安装（推荐）

### Windows (PowerShell)
```powershell
iwr -useb https://raw.githubusercontent.com/GQSDGQWE/AIDevKit/main/install.ps1 | iex
```

### macOS / Linux (Bash)
```bash
curl -fsSL https://raw.githubusercontent.com/GQSDGQWE/AIDevKit/main/install.sh | bash
```

### 安装后操作
1. 重启 Claude Desktop
2. 重启 VSCode
3. 开始编码！🎉

📖 详细安装说明: [QUICK_INSTALL.md](QUICK_INSTALL.md)

---

## 📦 核心功能

### 🎯 自动化部署系统（v2.4 新增）

| 工具 | 功能 | 命令 |
|------|------|------|
| **一键部署** | 交互式完整部署流程 | `tools\One-Click-Deploy.bat` |
| **配置部署** | 自动配置 Claude/VSCode | `python tools/deploy_config.py` |
| **清理工具** | 清除临时文件和缓存 | `python tools/cleanup.py` |
| **框架打包** | 创建可分发的 ZIP 包 | `python tools/package_framework.py` |

### 🔧 智能特性

- ✅ **自动检测** - 识别 Claude Desktop 和 VSCode 安装位置
- ✅ **配置写入** - 将规则文件自动部署到系统配置
- ✅ **错误处理** - 完整的异常处理和超时控制
- ✅ **双语支持** - 中英文完整支持

### 📁 配置位置

部署后配置文件位置：

```
Claude Desktop:
  %APPDATA%\Claude\claude_desktop_config.json

VSCode:
  %APPDATA%\Code\User\settings.json
  %APPDATA%\Code\User\copilot-instructions.md
```

---

---

## 📚 项目结构

```
CONSOL/
├── config/              # 配置文件（AI 规则）
│   ├── CLAUDE.md       # Claude Desktop 全局指令
│   └── copilot-instructions.md  # GitHub Copilot 指令
│
├── projects/           # 示例项目
│   ├── cognis_vault/   # 密码保险库（API + GUI + SDK）
│   └── aether_engine/  # DevOps 引擎
│
├── showcase/           # 5 个完整示例应用
│   ├── 01_todo_pro/    # 待办事项管理
│   ├── 02_log_insight/ # 日志分析
│   ├── 03_crypto_pulse/# 加密货币追踪
│   ├── 04_container_auth/ # Docker 容器认证
│   └── 05_doc_flow/    # 文档流程管理
│
├── tools/              # 自动化工具
│   ├── cleanup.py      # 清理工具
│   ├── deploy_config.py# 配置部署
│   ├── package_framework.py # 框架打包
│   └── One-Click-Deploy.bat # 一键部署
│
├── docs/               # 文档
│   ├── DEPLOYMENT_GUIDE.md # 部署指南
│   ├── INITIAL.md      # 项目说明
│   ├── GIT_GUIDE.md    # Git 工作流程
│   └── SKILLS_DEPLOYMENT.md # 技能系统
│
└── mcp-servers/        # Model Context Protocol 服务器
```

---

## 🎯 配置规则说明

### CLAUDE.md - AI Power Pack v2.4 标准

**核心规则：**
- ✅ **PLAN-EXECUTE 模式** - 先规划后执行
- ✅ **文件大小控制** - 单文件建议不超过 500 行
- ✅ **模块化设计** - 单一职责原则
- ✅ **质量优先** - 代码质量 > 数量
- ✅ **需求驱动** - 必须满足实际需求

**适用于：**
- Claude Desktop 全局指令
- 项目上下文工程
- 团队开发规范

### copilot-instructions.md - GitHub Copilot 规则

**核心规则：**
- ✅ **持续执行** - 默认完成整个任务
- ✅ **意图分析** - 理解用户真实需求
- ✅ **错误处理** - 完整的异常处理
- ✅ **类型安全** - 明确的类型定义
- ✅ **Git 集成** - 自动生成提交消息

**适用于：**
- VSCode GitHub Copilot
- 代码生成和补全
- AI 辅助编程

---

## 🚀 使用示例

### 1. 部署配置

```bash
# 运行一键部署
tools\One-Click-Deploy.bat

# 选择选项
1. Full Deploy (Clean + Package + Configure)  # 完整部署
2. Clean Only                                  # 仅清理
3. Package Only                                # 仅打包
4. Configure Only                              # 仅配置
5. Exit                                        # 退出
```

### 2. 验证部署

**测试 Claude Desktop：**
```
问题: "你遵循什么开发标准？"
预期: 应该提到 AI Power Pack v2.4、PLAN-EXECUTE 模式、500行限制等
```

**测试 VSCode Copilot：**
```
生成任意代码
预期: 
- 有 PLAN 注释
- 代码结构清晰
- 完整错误处理
- 文件大小合理
```

### 3. 运行示例项目

```bash
# Cognis Vault - 密码保险库
cd projects/cognis_vault
python api/main.py          # 启动 API (端口 8888)
python gui/main_window.py  # 启动 GUI

# Aether Engine - DevOps 引擎
cd projects/aether_engine
python gui/dashboard.py    # 启动仪表板
```

---

## 🛠️ 常见问题

### Q: Python 未找到？
```bash
python --version
# 如果未安装，下载: https://www.python.org/downloads/
# 需要 Python 3.8 或更高版本
```

### Q: Claude 配置未生效？
1. 完全关闭 Claude Desktop（不是最小化）
2. 重新运行 `python tools/deploy_config.py`
3. 重新启动 Claude Desktop
4. 验证配置文件: `%APPDATA%\Claude\claude_desktop_config.json`

### Q: VSCode Copilot 没有使用规则？
1. 检查文件是否存在: `%APPDATA%\Code\User\copilot-instructions.md`
2. 检查 settings.json 是否包含 Copilot 配置
3. 重启 VSCode（完全退出）
4. 在代码编辑器中测试生成代码

### Q: 如何分发给团队？
```bash
# 1. 创建分发包
python tools/package_framework.py

# 2. 找到 ZIP 文件
# 位置: dist/packages/AI_Power_Pack_v2.4_*.zip

# 3. 发送给团队成员

# 4. 团队成员安装
# 解压 → 运行 INSTALL.bat → 重启应用
```

---

## 📖 详细文档

- **部署指南**: [docs/DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md)
- **项目说明**: [docs/INITIAL.md](docs/INITIAL.md)
- **Git 工作流**: [docs/GIT_GUIDE.md](docs/GIT_GUIDE.md)
- **技能系统**: [docs/SKILLS_DEPLOYMENT.md](docs/SKILLS_DEPLOYMENT.md)

---

## 🎉 更新日志

### v2.4.0 (2026-01-07)
- ✨ 新增自动化部署系统
- ✨ 自动检测并配置 Claude Desktop
- ✨ 自动检测并配置 VSCode
- ✨ 新增清理工具 (cleanup.py)
- ✨ 新增配置部署工具 (deploy_config.py)
- ✨ 新增框架打包工具 (package_framework.py)
- ✨ 新增一键部署脚本 (One-Click-Deploy.bat)
- 🐛 修复网络连接超时问题
- 📝 完整的部署文档和指南

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**AI Power Pack v2.4** - Professional AI Development Framework

Made with ❤️ by CONSOL Team | 2026
- Prevents AI from inventing APIs/patterns that don't exist / 防止 AI 编造不存在的 API
- Enforces project-specific coding standards / 强制执行项目特定编码标准
- PRP (Plan-Research-Produce) workflow / PRP（计划-研究-生成）工作流

**Key Files / 核心文件**:
- `CLAUDE.md`: Global project rules (tech stack, coding standards) / 全局项目规则
- `INITIAL.md`: Feature description template / 功能描述模板
- `.cursorrules`: AI behavior configuration / AI 行为配置

---

### 4. **OpenSkills** - [github.com/ErikBjare/openskills](https://github.com/ErikBjare/openskills)
**The Platform Lock-In Problem / 平台锁定问题**

**What It Does / 功能**:
- Brings Claude Code's "Skills" to Cursor, Windsurf, Aider / 将 Claude Code 的"技能"带到其他工具
- Enables AI to handle PDFs, Excel, Word, PowerPoint natively / 使 AI 能原生处理 PDF、Excel、Word、PPT
- Progressive Disclosure: Load instructions only when needed / 渐进式披露

**Example Skills / 技能示例**:
- `database-migration`: Generate Prisma migrations / 生成 Prisma 迁移
- `api-endpoint`: Create REST routes with validation / 创建带验证的 REST 路由
- `pdf-extract`: Parse PDF tables and text / 解析 PDF 表格和文本

---

### 5. **UI/UX Pro Max** - [github.com/Haoqi9/ui-ux-pro-max-skill](https://github.com/Haoqi9/ui-ux-pro-max-skill)
**The "Programmer Art" Problem / "程序员审美"问题**

**What It Does / 功能**:
- Prevents ugly/inconsistent UI generation / 防止生成丑陋/不一致的 UI
- Auto-enforces WCAG accessibility standards / 自动强制执行 WCAG 无障碍标准
- Stack-specific design rules (React/Vue/Svelte/Flutter) / 特定技术栈的设计规则

---

## 🚀 Quick Start / 快速开始 {#quick-start}

### Method 1: One-Click Deployment (Recommended) / 一键部署（推荐）

**Plan Mode Approach / Plan 模式方法**:
```
PLAN:
1. Extract distribution package to destination folder
2. Run silent installation with automated deployment
3. Verify all configuration files are created
4. Display success confirmation

EXECUTE:
```

```powershell
# Step 1: Extract the package
Expand-Archive AI-Power-Pack-v2.4-Ultimate-Dist.zip -DestinationPath C:\AI-Tools

# Step 2: Run silent installation
cd C:\AI-Tools
.\One-Click-Deploy.bat

# Or use the EXE directly with silent flag
.\AI-Power-Pack-Ultimate-v2.3.2.exe -Silent
```

### Method 2: Manual Installation / 手动安装

**Plan Mode Approach / Plan 模式方法**:
```
PLAN:
1. Install Fabric Framework via curl or Homebrew
2. Download tech-stack-specific Cursor Rules
3. Set up Context Engineering file structure
4. Configure OpenSkills for document processing
5. Apply UI/UX Pro Max design system

EXECUTE:
```

```bash
# Step 1: Install Fabric
curl -fsSL https://raw.githubusercontent.com/danielmiessler/fabric/main/scripts/installer/install.sh | bash

# Step 2: Download Cursor Rules (browse at https://cursor.directory)
curl -o .cursorrules https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/YOUR_STACK/.cursorrules

# Step 3: Set Up Context Engineering
mkdir -p .context
touch CLAUDE.md INITIAL.md .cursorrules

# Step 4: Configure OpenSkills
curl -o openskills.json https://raw.githubusercontent.com/ErikBjare/openskills/main/skills.json

# Step 5: (Optional) Apply UI/UX design system rules
```

---

## 📖 Usage Examples / 使用示例 {#usage-examples}

### Fabric CLI Examples / Fabric CLI 示例

**Plan Mode Approach / Plan 模式方法**:
```
PLAN:
1. Extract YouTube video transcript and metadata
2. Process content through extract_wisdom pattern
3. Stream results to console and save to file

EXECUTE:
```

```bash
# Example 1: Summarize YouTube video
fabric -y "https://youtube.com/watch?v=dQw4w9WgXcQ" --pattern extract_wisdom --stream

# Example 2: Analyze website content
fabric -u https://news.ycombinator.com --pattern summarize -o summary.md

# Example 3: Code review
cat mycode.ts | fabric --pattern code_review --stream

# Example 4: Generate LaTeX academic paper
echo "AI ethics in healthcare" | fabric --pattern write_latex -o paper.tex

# Example 5: Create feature from user story
cat user_story.md | fabric --pattern create_coding_feature --model gpt-4
```

### Cursor Rules Example / Cursor Rules 示例

**Plan Mode Approach / Plan 模式方法**:
```
PLAN:
1. Initialize new project with Cursor IDE
2. Download appropriate .cursorrules for tech stack
3. Place file in project root directory
4. Configure AI to follow project-specific conventions

EXECUTE:
```

```bash
# Start a Next.js project with Cursor
cursor new-project my-app

# Download Next.js + TypeScript + Tailwind rules
cd my-app
curl -o .cursorrules https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/nextjs-typescript-tailwind-cursorrules-prompt-file/.cursorrules

# AI now follows Next.js best practices automatically
```

### Context Engineering Example / 上下文工程示例

**Plan Mode Approach / Plan 模式方法**:
```
PLAN:
1. Create CLAUDE.md with project context
2. Define tech stack, coding standards, and AI behavior rules
3. Set up INITIAL.md for feature description template
4. Configure .cursorrules for fine-grained control

EXECUTE:
```

```markdown
# CLAUDE.md example
You are working on a SaaS platform for project management.

## Tech Stack
- Next.js 14 (App Router)
- TypeScript 5.3+
- PostgreSQL + Prisma
- Socket.io for real-time updates

## Rules
- All API routes must check authentication
- Use RBAC for permission checks
- Rate limit: 100 req/min per user
- Log all failed auth attempts

## AI Behavior
- Research existing code patterns before implementing
- Write unit tests for all business logic
- Skip explanations for obvious changes ("No Yapping")
```

---

## 🎨 SCI Figure Prompts (JSON Config) / SCI 绘图配置 (JSON 结构) {#sci-figure-prompts}

以下是 **SCI 级别科研绘图的结构化视觉风格配置**，包含颜色、排版、构图和特效的 JSON 数据：

### JSON Configuration Schema / JSON 配置架构

```json
{
  "sci_figure_styles": {
    "version": "2.4.0",
    "description": "Scientific illustration visual style configuration for Midjourney/Stable Diffusion/DALL-E",
    "categories": [
      {
        "category": "biological_structures",
        "name": "Biological Structures / 生物结构",
        "styles": [
          {
            "type": "protein_visualization",
            "name": "Protein Folding & Structure / 蛋白质折叠与结构",
            "visual_style": {
              "color_palette": {
                "primary": ["#FF4444", "#FFAA00", "#44FF44"],
                "secondary": ["#4444FF", "#FF44FF", "#00FFFF"],
                "background": "#FFFFFF",
                "accent": "#FFD700",
                "description": "Red for alpha-helix, yellow for beta-sheet, green for loops, blue for beta-sheets"
              },
              "composition": {
                "layout": "centered_3d_ribbon_diagram",
                "perspective": "45_degree_isometric",
                "focal_point": "active_site_pocket",
                "depth_of_field": "shallow_focus_on_binding_site"
              },
              "typography": {
                "font_family": "Arial, Helvetica, sans-serif",
                "title_size": "18pt",
                "label_size": "12pt",
                "caption_size": "10pt",
                "color": "#333333",
                "style": "clean_scientific_sans_serif"
              },
              "effects": {
                "rendering": "ray_tracing",
                "lighting": "studio_three_point_lighting",
                "shadows": "soft_ambient_occlusion",
                "transparency": "molecular_surface_overlay_30%",
                "glow": "active_site_subtle_glow",
                "resolution": "8K_ultra_high_definition"
              },
              "prompt_template": "/imagine prompt: detailed 3d visualization of {{protein_name}} protein structure, ribbon diagram with {{color_coded}} secondary structures (red alpha-helix, yellow beta-sheet, green loops), molecular surface overlay at 30% transparency, {{binding_site}} highlighted with subtle golden glow, studio lighting with soft shadows, ray tracing, clean white background, scale bar {{size}}nm, scientific accuracy, 8k resolution --v 6.0 --ar 16:9 --quality 2"
            }
          },
          {
            "type": "cell_membrane",
            "name": "Cell Membrane & Receptors / 细胞膜与受体",
            "visual_style": {
              "color_palette": {
                "lipid_heads": "#FFB6C1",
                "lipid_tails": "#FFA500",
                "proteins": "#4169E1",
                "ligands": "#32CD32",
                "background": "#F5F5F5",
                "description": "Pink for phospholipid heads, orange for tails, royal blue for proteins, lime green for ligands"
              },
              "composition": {
                "layout": "cross_section_cutaway",
                "perspective": "side_view_with_depth",
                "focal_point": "receptor_ligand_binding",
                "layers": ["extracellular", "membrane", "intracellular"]
              },
              "typography": {
                "font_family": "Calibri, Arial, sans-serif",
                "annotation_style": "leader_lines_with_labels",
                "label_placement": "non_overlapping_smart_positioning"
              },
              "effects": {
                "rendering": "medical_textbook_illustration",
                "shading": "gradient_depth_perception",
                "highlights": "hydrophilic_hydrophobic_contrast",
                "transparency": "partial_membrane_transparency_50%",
                "resolution": "4K_print_ready"
              },
              "prompt_template": "/imagine prompt: cross-section of cell membrane lipid bilayer, phospholipid molecules with pink hydrophilic heads and orange hydrophobic tails, embedded {{receptor_type}} protein in royal blue, {{ligand}} binding in lime green, cutaway view showing both sides, gradient shading for depth, clean medical textbook illustration style, clear labels with leader lines, professional color palette, white background, 4k resolution --v 6.0 --ar 3:2"
            }
          }
        ]
      },
      {
        "category": "nanoparticle_systems",
        "name": "Nanoparticle Systems / 纳米粒子系统",
        "styles": [
          {
            "type": "drug_delivery_lnp",
            "name": "Lipid Nanoparticle for Drug Delivery / 脂质纳米粒子药物递送",
            "visual_style": {
              "color_palette": {
                "lipid_core": "#FFE4B5",
                "pegylation": "#87CEEB",
                "payload": "#FF6347",
                "targeting_ligand": "#9370DB",
                "background": "#2C3E50",
                "description": "Moccasin for lipid core, sky blue for PEG shell, tomato red for mRNA/drug, medium purple for targeting molecules"
              },
              "composition": {
                "layout": "cutaway_sphere_with_inset_zoom",
                "perspective": "3d_exploded_view",
                "scale_indicator": "100nm_scale_bar",
                "inset_position": "bottom_right_corner"
              },
              "typography": {
                "font_family": "Roboto, Helvetica, sans-serif",
                "size_annotation": "bold_with_unit_nm",
                "component_labels": "color_coded_to_match_visual"
              },
              "effects": {
                "rendering": "scientific_3d_glossy",
                "lighting": "dramatic_rim_lighting_on_dark_background",
                "transparency": "outer_shell_translucent_70%",
                "glow": "inner_core_soft_luminescence",
                "depth_cues": "size_gradient_for_depth",
                "resolution": "publication_quality_300dpi"
              },
              "prompt_template": "/imagine prompt: cutaway view of lipid nanoparticle (LNP) for {{payload_type}} delivery, spherical structure with moccasin-colored lipid core containing tomato-red {{drug_name}}, sky-blue PEGylated outer shell at 70% transparency, medium-purple targeting ligands on surface, dramatic rim lighting on dark blue-gray background, scale bar showing {{size}}nm, inset zoom showing molecular detail, glossy scientific rendering, Nature Nanotechnology journal style, publication quality 300dpi --v 6.0 --ar 16:9 --quality 2"
            }
          },
          {
            "type": "quantum_dots",
            "name": "Quantum Dots / 量子点",
            "visual_style": {
              "color_palette": {
                "core": ["#FF0000", "#00FF00", "#0000FF"],
                "shell": "#C0C0C0",
                "emission": ["#FF1493", "#00FFFF", "#FFD700"],
                "background": "#000000",
                "description": "RGB cores emit different colors, silver shells, emission halos in deep pink/cyan/gold on black"
              },
              "composition": {
                "layout": "array_pattern_with_emission_visualization",
                "arrangement": "hexagonal_close_packed",
                "size_distribution": "gaussian_with_size_tuning"
              },
              "typography": {
                "font_family": "Futura, Avant Garde, sans-serif",
                "wavelength_labels": "nm_values_in_white",
                "size_annotations": "diameter_in_nanometers"
              },
              "effects": {
                "rendering": "photoluminescence_glow",
                "lighting": "uv_excitation_visualization",
                "glow_intensity": "high_saturation_emission",
                "bloom": "color_specific_light_scatter",
                "resolution": "ultra_sharp_4K"
              },
              "prompt_template": "/imagine prompt: array of quantum dots in hexagonal pattern, varying sizes from {{min_size}}nm to {{max_size}}nm, cores in red/green/blue emitting bright photoluminescence halos (deep pink {{wavelength1}}nm / cyan {{wavelength2}}nm / gold {{wavelength3}}nm), silver shells, UV excitation visualization, high saturation glow effects, dramatic bloom, black background for contrast, size scale annotations, advanced materials science illustration, 4k ultra sharp --v 6.0 --ar 1:1 --quality 2"
            }
          }
        ]
      },
      {
        "category": "lab_equipment",
        "name": "Laboratory Equipment / 实验室设备",
        "styles": [
          {
            "type": "modern_lab_setup",
            "name": "Modern Molecular Biology Lab / 现代分子生物学实验室",
            "visual_style": {
              "color_palette": {
                "equipment": "#E8E8E8",
                "accents": "#0080FF",
                "lighting": "#FFFFFF",
                "background": "#F0F0F0",
                "floor": "#808080",
                "description": "Light gray equipment, blue LED accents, bright clinical white lighting, light gray background"
              },
              "composition": {
                "layout": "wide_angle_workstation_view",
                "perspective": "slightly_elevated_eye_level",
                "depth_of_field": "foreground_sharp_background_slight_blur",
                "elements": ["pcr_cycler", "gel_electrophoresis", "centrifuge", "pipettes"]
              },
              "typography": {
                "equipment_labels": "minimal_overlay_annotations",
                "font_style": "modern_technical_sans_serif",
                "placement": "non_intrusive_corner_labels"
              },
              "effects": {
                "rendering": "photorealistic_architecture_viz",
                "lighting": "bright_clinical_overhead_led",
                "reflections": "subtle_on_equipment_surfaces",
                "depth_of_field": "f2.8_shallow_focus",
                "camera": "Canon_EOS_R5_35mm_equivalent",
                "resolution": "8K_photorealistic"
              },
              "prompt_template": "/imagine prompt: modern molecular biology laboratory workstation, {{equipment_list}}, light gray equipment with blue LED indicators, bright clinical overhead lighting, slightly elevated eye-level perspective, shallow depth of field (foreground equipment in sharp focus, background slightly blurred), subtle reflections on surfaces, clean organized workspace, photorealistic architectural visualization style, shot on Canon EOS R5 with 35mm lens at f/2.8, 8k ultra detailed --v 6.0 --ar 16:9 --quality 2"
            }
          }
        ]
      },
      {
        "category": "data_visualization",
        "name": "Data Visualization / 数据可视化",
        "styles": [
          {
            "type": "multi_omics_network",
            "name": "Multi-Omics Integration Network / 多组学整合网络",
            "visual_style": {
              "color_palette": {
                "genes": "#FF4444",
                "proteins": "#44FF44",
                "metabolites": "#4444FF",
                "connections": "#CCCCCC",
                "background": "#1A1A2E",
                "clusters": ["#FF6B9D", "#C44569", "#FFC048", "#00D9FF"],
                "description": "Red nodes for genes, green for proteins, blue for metabolites, gray connections, dark blue-black background"
              },
              "composition": {
                "layout": "circular_chord_diagram",
                "network_algorithm": "force_directed_layout",
                "clustering": "hierarchical_by_pathway",
                "node_size": "proportional_to_degree_centrality"
              },
              "typography": {
                "node_labels": "gene_protein_metabolite_names",
                "font_size": "adaptive_based_on_importance",
                "label_color": "#FFFFFF",
                "pathway_annotations": "curved_along_arc"
              },
              "effects": {
                "rendering": "network_graph_cybernetic_style",
                "edge_style": "bezier_curves_with_transparency",
                "edge_weight": "line_thickness_by_correlation",
                "glow": "node_subtle_outer_glow",
                "animation": "static_with_implied_flow_direction",
                "resolution": "vector_quality_publication_ready"
              },
              "prompt_template": "/imagine prompt: circular chord diagram showing {{dataset_name}} multi-omics network, gene nodes in red, protein nodes in green, metabolite nodes in blue, bezier curve connections in semi-transparent gray (thickness represents correlation strength), nodes sized by degree centrality, hierarchical clustering by biological pathway (clusters colored pink/crimson/gold/cyan), subtle outer glow on all nodes, cybernetic blue-black background, high contrast, pathway labels curved along arcs, publication-ready vector quality, Nature Methods journal style --v 6.0 --ar 16:9 --quality 2"
            }
          },
          {
            "type": "time_series_heatmap",
            "name": "Gene Expression Heatmap / 基因表达热图",
            "visual_style": {
              "color_palette": {
                "low_expression": "#0000FF",
                "mid_expression": "#000000",
                "high_expression": "#FF0000",
                "gradient": "blue_black_red_diverging",
                "dendrograms": "#808080",
                "background": "#FFFFFF",
                "description": "Blue for low expression, black for baseline, red for high expression, gray dendrograms"
              },
              "composition": {
                "layout": "matrix_with_hierarchical_clustering",
                "row_clustering": "genes_by_expression_pattern",
                "column_clustering": "samples_by_timepoint",
                "dendrogram_position": "top_and_left"
              },
              "typography": {
                "row_labels": "gene_names_right_aligned",
                "column_labels": "timepoint_or_condition_45deg_angle",
                "font_family": "Arial_or_Helvetica",
                "font_size": "8pt_for_labels",
                "color": "#000000"
              },
              "effects": {
                "rendering": "clean_matrix_scientific_style",
                "borders": "thin_gray_cell_borders",
                "color_scale": "diverging_blue_black_red",
                "legend": "vertical_colorbar_with_values",
                "aspect_ratio": "rectangular_optimal_for_data",
                "resolution": "600dpi_vector_or_high_res_raster"
              },
              "prompt_template": "/imagine prompt: gene expression heatmap showing {{experiment_name}} time-series data, hierarchical clustering dendrograms on top and left (gray), matrix of cells colored by expression level (blue for low, black for baseline, red for high), gene names right-aligned in 8pt Arial, timepoint labels at 45-degree angle at top, thin gray cell borders, vertical colorbar legend on right showing scale, clean minimalist design, Nature Methods / Cell journal style, 600dpi publication quality --v 6.0 --ar 3:2 --quality 2"
            }
          },
          {
            "type": "volcano_plot",
            "name": "Volcano Plot for Differential Expression / 火山图差异表达",
            "visual_style": {
              "color_palette": {
                "upregulated": "#FF0000",
                "downregulated": "#0000FF",
                "non_significant": "#CCCCCC",
                "threshold_lines": "#000000",
                "background": "#FFFFFF",
                "description": "Red for upregulated, blue for downregulated, gray for non-significant"
              },
              "composition": {
                "layout": "scatter_plot_with_threshold_lines",
                "x_axis": "log2_fold_change",
                "y_axis": "negative_log10_p_value",
                "thresholds": "vertical_and_horizontal_dashed_lines"
              },
              "typography": {
                "axis_labels": "log2(Fold Change) and -log10(p-value)",
                "gene_annotations": "top_genes_with_leader_lines",
                "font_family": "Arial",
                "font_size": "12pt_axes_10pt_labels"
              },
              "effects": {
                "rendering": "clean_scatter_plot_style",
                "point_transparency": "60%_for_overlapping_points",
                "point_size": "small_uniform_2-3px",
                "threshold_style": "black_dashed_lines",
                "resolution": "vector_pdf_or_600dpi_png"
              },
              "prompt_template": "/imagine prompt: volcano plot for {{comparison_name}} differential gene expression, scatter plot with log2(Fold Change) on x-axis and -log10(p-value) on y-axis, upregulated genes in red (right side), downregulated genes in blue (left side), non-significant genes in light gray, black dashed lines indicating significance thresholds (vertical at fold-change ±1, horizontal at p<0.05), top {{N}} genes annotated with names and leader lines, small uniform point size with 60% transparency, clean minimalist scientific style, white background, publication-ready vector quality --v 6.0 --ar 4:3 --quality 2"
            }
          }
        ]
      },
      {
        "category": "biochemical_pathways",
        "name": "Biochemical Pathways / 生化通路",
        "styles": [
          {
            "type": "metabolic_pathway",
            "name": "Metabolic Pathway Diagram / 代谢通路图",
            "visual_style": {
              "color_palette": {
                "substrates": "#FFD700",
                "products": "#FF6347",
                "enzymes": "#4169E1",
                "cofactors": "#32CD32",
                "arrows": "#000000",
                "background": "#FFFFFF",
                "description": "Gold for substrates, tomato for products, royal blue for enzymes, lime green for cofactors"
              },
              "composition": {
                "layout": "directed_graph_left_to_right",
                "flow_direction": "substrate_to_product",
                "enzyme_position": "above_reaction_arrows",
                "branching": "clear_pathway_divergence"
              },
              "typography": {
                "molecule_names": "chemical_nomenclature",
                "enzyme_names": "EC_numbers_and_gene_names",
                "font_family": "Arial_or_Helvetica",
                "font_size": "10pt_molecules_8pt_enzymes"
              },
              "effects": {
                "rendering": "clean_vector_biochemistry_style",
                "arrows": "solid_black_with_chevron_heads",
                "reaction_reversibility": "double_arrows_for_reversible",
                "emphasis": "bold_borders_for_rate_limiting_steps",
                "resolution": "vector_svg_or_600dpi"
              },
              "prompt_template": "/imagine prompt: {{pathway_name}} metabolic pathway diagram, substrates in gold rounded rectangles, products in tomato-red rounded rectangles, enzyme names in royal blue above reaction arrows (with EC numbers), cofactors in lime green circles, solid black arrows showing reaction direction (double arrows for reversible reactions), left-to-right flow, clear branching points, rate-limiting steps with bold borders, clean biochemistry textbook style, white background, vector quality illustration --v 6.0 --ar 16:9"
            }
          }
        ]
      }
    ],
    "global_settings": {
      "image_aspect_ratios": {
        "standard": "16:9",
        "portrait": "3:4",
        "square": "1:1",
        "wide": "21:9"
      },
      "quality_presets": {
        "draft": "--quality 0.5",
        "standard": "--quality 1",
        "high": "--quality 2"
      },
      "model_versions": {
        "midjourney": "v6.0",
        "stable_diffusion": "SDXL 1.0",
        "dall_e": "dall-e-3"
      },
      "output_formats": {
        "print": "300dpi TIFF or PDF",
        "web": "72-150dpi PNG or JPEG",
        "vector": "SVG or AI"
      }
    }
  }
}
```

### Usage Example with JSON Config / JSON 配置使用示例

**Plan Mode Approach / Plan 模式方法**:
```
PLAN:
1. Load JSON configuration for desired figure type
2. Extract visual_style parameters (colors, composition, effects)
3. Replace template variables with specific content
4. Generate prompt for AI image generator
5. Validate output against style specifications

EXECUTE:
```

```python
import json

# Load configuration
with open('sci_figure_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Select a style
protein_style = config['sci_figure_styles']['categories'][0]['styles'][0]

# Extract template
template = protein_style['visual_style']['prompt_template']

# Fill in variables
prompt = template.replace('{{protein_name}}', 'EGFR kinase domain')
prompt = prompt.replace('{{color_coded}}', 'rainbow')
prompt = prompt.replace('{{binding_site}}', 'ATP-binding pocket')
prompt = prompt.replace('{{size}}', '5')

# Output final prompt
print(prompt)
```

**Generated Prompt Output / 生成的提示词输出**:
```
/imagine prompt: detailed 3d visualization of EGFR kinase domain protein structure, ribbon diagram with rainbow secondary structures (red alpha-helix, yellow beta-sheet, green loops), molecular surface overlay at 30% transparency, ATP-binding pocket highlighted with subtle golden glow, studio lighting with soft shadows, ray tracing, clean white background, scale bar 5nm, scientific accuracy, 8k resolution --v 6.0 --ar 16:9 --quality 2
```

---

## 🎓 Learning Path / 学习路径 {#learning-path}

**Plan Mode Approach / Plan 模式方法**:
```
PLAN:
Week 1: Master Fabric CLI for content summarization
Week 2: Implement Cursor Rules in main project
Week 3: Deploy Context Engineering system
Week 4: Explore OpenSkills for document processing
Week 5: Fine-tune UI/UX Pro Max design system

EXECUTE: Follow the detailed weekly schedule below
```

### Week 1: Fabric CLI Mastery / Fabric CLI 精通
- Install Fabric framework / 安装 Fabric 框架
- Try 5-10 patterns with your content / 尝试 5-10 个模式
- Set up API keys for your preferred LLM / 设置首选 LLM 的 API 密钥
- Practice YouTube transcript extraction / 练习 YouTube 转录提取

### Week 2: Cursor Rules Implementation / Cursor Rules 实施
- Browse cursor.directory for your tech stack / 浏览 cursor.directory
- Download and test 2-3 different `.cursorrules` / 下载并测试 2-3 个不同的规则
- Customize rules for your project / 为项目定制规则
- Share with team for feedback / 与团队分享以获取反馈

### Week 3: Context Engineering Deployment / 上下文工程部署
- Create `CLAUDE.md` with project details / 创建包含项目详情的 CLAUDE.md
- Write `INITIAL.md` feature template / 编写 INITIAL.md 功能模板
- Test PRP workflow on a real feature / 在真实功能上测试 PRP 工作流
- Measure reduction in AI hallucinations / 测量 AI 幻觉的减少

### Week 4: OpenSkills Exploration / OpenSkills 探索
- Set up skills configuration / 设置技能配置
- Test PDF/Excel extraction capabilities / 测试 PDF/Excel 提取能力
- Create 1-2 custom skills for your workflow / 为工作流创建 1-2 个自定义技能
- Integrate with existing tools / 与现有工具集成

### Week 5: UI/UX Pro Max Fine-Tuning / UI/UX Pro Max 微调
- Review design system rules / 审查设计系统规则
- Apply to component library / 应用于组件库
- Test accessibility compliance / 测试无障碍合规性
- Document design decisions / 记录设计决策

---

## 📜 Release Notes / 发布说明 {#release-notes}

### v2.4.0 (2026-01-05) - Current Release

**🎉 Major Features / 主要功能**:
- ✅ **Real GitHub Project Integration**: Added official links to all 5 frameworks with live statistics / 添加了所有 5 个框架的官方链接和实时统计
- ✅ **JSON-Structured SCI Prompts**: Complete visual style configuration for scientific illustrations / 完整的科研绘图视觉风格 JSON 配置
- ✅ **Plan Mode Documentation**: All usage examples now follow Plan-Execute pattern / 所有使用示例现在遵循 Plan-Execute 模式
- ✅ **Unified Documentation**: Merged README and Release Notes into single comprehensive guide / 合并 README 和发布说明为单一综合指南

**Referenced Projects / 参考项目**:
1. **Fabric**: [github.com/danielmiessler/fabric](https://github.com/danielmiessler/fabric) (37.8k⭐, 326 releases, MIT)
2. **Awesome Cursor Rules**: [github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) (36.7k⭐, 68 contributors, CC0)
3. **Context Engineering**: [github.com/Haoqi9/context-engineering-intro-zh](https://github.com/Haoqi9/context-engineering-intro-zh) (Community)
4. **OpenSkills**: [github.com/ErikBjare/openskills](https://github.com/ErikBjare/openskills) (Active)
5. **UI/UX Pro Max**: [github.com/Haoqi9/ui-ux-pro-max-skill](https://github.com/Haoqi9/ui-ux-pro-max-skill) (Active)

### v2.3.2 (2026-01-05)
- **[Fix]** PowerShell path resolution for cross-PC compatibility / PowerShell 路径解析修复
- **[Fix]** UTF-8 encoding for Chinese text display / UTF-8 编码修复中文显示

### v2.3.0 (2026-01-05)
- **[New]** Silent Mode for automation (`-Silent` flag) / 自动化静默模式
- **[New]** Smart overwrite protection with .bak files / 智能覆盖保护

### v2.0.0
- **[Initial]** Integrated 5 frameworks into single executable / 集成 5 个框架到单一可执行文件

---

## 🌐 Community Resources / 社区资源 {#community-resources}

### Official Documentation / 官方文档
- **Fabric Docs**: https://github.com/danielmiessler/fabric/blob/main/README.md
- **Fabric REST API**: https://github.com/danielmiessler/fabric/blob/main/docs/rest-api.md
- **Cursor Directory**: https://cursor.directory (browse all .cursorrules)

### Video Tutorials / 视频教程
- **Network Chuck**: https://www.youtube.com/watch?v=UbDyjIIGaxQ
- **David Bombal**: https://www.youtube.com/watch?v=vF-MQmVxnCs
- **Daniel Miessler's Intro**: https://www.youtube.com/watch?v=wPEyyigh10g

### Support Channels / 支持渠道
- **Fabric Issues**: https://github.com/danielmiessler/fabric/issues
- **Fabric Discussions**: https://github.com/danielmiessler/fabric/discussions
- **Cursor Rules Contributions**: https://github.com/PatrickJS/awesome-cursorrules
- **Context Engineering (Chinese Community)**: GitHub discussions

---

## 📊 Project Statistics / 项目统计

- **Total GitHub Stars**: 74.5k+ (Fabric 37.8k + Cursor Rules 36.7k)
- **Total Contributors**: 276+ (Fabric 208 + Cursor Rules 68)
- **Total Releases**: 326 (Fabric framework)
- **Supported Tech Stacks**: 150+ combinations
- **AI Patterns Available**: 600+ (Fabric 300+ + Cursor Rules 300+)
- **SCI Figure Styles**: 10+ structured JSON configurations

---

## ⚠️ System Requirements / 系统要求

- **OS**: Windows 10/11, macOS 10.15+, Linux (Ubuntu 20.04+)
- **PowerShell**: 5.1+ (Windows) or PowerShell Core 7+ (cross-platform)
- **.NET Framework**: 4.0+ (Windows only, for EXE version)
- **Python**: 3.8+ (recommended for Fabric CLI extensions)
- **Internet**: Required for initial setup and pattern downloads / 初始设置和模式下载需要网络

---

## 🐛 Known Issues & Troubleshooting / 已知问题与故障排除

### Issue 1: Fabric Installation Fails
**Solution**: Check internet connection and firewall settings. Try manual binary download.
**解决方案**: 检查网络连接和防火墙设置。尝试手动下载二进制文件。

### Issue 2: PowerShell Encoding Issues
**Solution**: Run `chcp 65001` before executing scripts to set UTF-8 encoding.
**解决方案**: 执行脚本前运行 `chcp 65001` 设置 UTF-8 编码。

### Issue 3: .cursorrules Not Loading
**Solution**: Ensure file is in project root directory and Cursor AI is restarted.
**解决方案**: 确保文件在项目根目录且重启 Cursor AI。

---

## 📄 License / 许可证

- **This Integration Tool**: MIT License
- **Fabric**: MIT License ([github.com/danielmiessler/fabric](https://github.com/danielmiessler/fabric))
- **Awesome Cursor Rules**: CC0 - Public Domain ([github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules))
- **Other Components**: Respective project licenses

---

## 🙏 Credits / 致谢

This tool stands on the shoulders of giants:
本工具站在巨人的肩膀上：

- **Daniel Miessler** - Creator of Fabric framework
- **PatrickJS** - Maintainer of Awesome Cursor Rules
- **Haoqi9** - Context Engineering & UI/UX Pro Max
- **ErikBjare** - OpenSkills cross-platform system
- **1000+ Contributors** - Community-driven patterns and rules

Special thanks to the open source community for making AI augmentation accessible to everyone.
特别感谢开源社区让 AI 增强对所有人都触手可及。

---

**Built with ❤️ by the Open Source Community**
**由开源社区用 ❤️ 构建**

_Standing on the shoulders of giants: Daniel Miessler, PatrickJS, and 1000+ contributors._
_站在巨人的肩膀上：Daniel Miessler、PatrickJS 和 1000+ 贡献者。_

---

_Last Updated / 最后更新: 2026-01-05_  
_Version / 版本: 2.4.0_  
_Package Size / 包大小: 11.73 KB_
