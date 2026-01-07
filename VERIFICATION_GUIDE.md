# 🔍 AI Power Pack v2.4 - 安装验证指南

## 快速验证

### 方法 1：询问 AI 标准问题

**测试 Claude Desktop:**
```
问：What coding standards do you follow?
或：你遵循什么开发标准？
```

**正确回答应包含：**
- ✅ 提到 "AI Power Pack v2.4"
- ✅ 提到 PLAN-EXECUTE 模式
- ✅ 提到 5 个核心原则（代码质量标准）
- ✅ 提到文件组织规则（单文件 200-500 行）
- ✅ 提到 API-First 原则

**错误回答（未安装）：**
- ❌ 只回答通用的编程标准
- ❌ 没有提到 AI Power Pack
- ❌ 没有提到具体的文件行数限制

---

### 方法 2：测试具体行为

**测试问题 1 - 代码规划：**
```
请帮我创建一个 TODO 应用
```

**期望行为：**
- ✅ 先输出 PLAN（规划步骤）
- ✅ 然后 EXECUTE（执行代码）
- ✅ 文件组织按功能分组（不是按类型）
- ✅ 每个文件有明确的单一职责

**错误行为：**
- ❌ 直接给代码，没有规划
- ❌ 所有代码放在一个文件
- ❌ 按类型分组（models/, views/, controllers/）

---

**测试问题 2 - 文件大小：**
```
这个文件太大了，请帮我优化
```

**期望行为：**
- ✅ 主动检查文件是否超过 200-500 行
- ✅ 建议按功能拆分模块
- ✅ 保持单一职责原则

---

**测试问题 3 - API 设计：**
```
创建一个密码管理器
```

**期望行为：**
- ✅ 自动提供 API/SDK 接口
- ✅ 明确的外部调用方式
- ✅ 提供使用示例

---

### 方法 3：检查配置文件

**Windows - Claude Desktop:**
```powershell
# 检查配置文件是否存在
Test-Path "$env:APPDATA\Claude\claude_desktop_config.json"

# 查看配置内容
Get-Content "$env:APPDATA\Claude\claude_desktop_config.json" | ConvertFrom-Json | ConvertTo-Json -Depth 10
```

**期望输出：**
```json
{
  "customInstructions": {
    "global": "# AI Power Pack v2.4...",
    "version": "2.4",
    "source": "github"
  }
}
```

---

**Windows - VSCode Copilot:**
```powershell
# 检查指令文件
Test-Path "$env:APPDATA\Code\User\copilot-instructions.md"

# 检查 settings.json
Get-Content "$env:APPDATA\Code\User\settings.json" | ConvertFrom-Json | Select-Object -ExpandProperty "github.copilot.chat.codeGeneration.instructions"
```

---

### 方法 4：行为对比测试

| 测试场景 | 未安装规范 | 已安装规范 |
|---------|----------|----------|
| **询问标准** | 回答通用标准 | 回答 AI Power Pack v2.4 |
| **创建项目** | 直接给代码 | 先 PLAN 后 EXECUTE |
| **文件组织** | 按类型分组 | 按功能分组 |
| **文件大小** | 不限制 | 主动控制在 200-500 行 |
| **API 设计** | 可能忽略 | 主动提供 API/SDK |
| **解释风格** | 啰嗦解释 | 简洁高效（No Yapping）|

---

## 完整验证清单

### ✅ 配置文件检查

**Claude Desktop:**
- [ ] 配置文件存在：`%APPDATA%\Claude\claude_desktop_config.json`
- [ ] 包含 `customInstructions.global`
- [ ] 版本号为 `2.4`
- [ ] 内容包含 "AI Power Pack v2.4"

**VSCode:**
- [ ] 指令文件存在：`%APPDATA%\Code\User\copilot-instructions.md`
- [ ] settings.json 包含 `github.copilot.chat.codeGeneration.instructions`
- [ ] 文件路径正确引用

---

### ✅ AI 行为验证

**基础测试：**
- [ ] 询问标准时提到 AI Power Pack v2.4
- [ ] 代码前会先输出 PLAN
- [ ] 文件按功能组织，不按类型
- [ ] 每个文件保持单一职责

**高级测试：**
- [ ] 创建项目时自动提供 API
- [ ] 文件超过 500 行时主动拆分
- [ ] 安全验证（输入验证、输出清理）
- [ ] 性能考虑（时间/空间复杂度）

---

## 验证脚本

### PowerShell 自动验证脚本

```powershell
# AI Power Pack v2.4 - Verification Script

Write-Host "`n=====================================" -ForegroundColor Cyan
Write-Host "AI Power Pack v2.4 - 验证工具" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

$results = @{
    claude = $false
    vscode = $false
}

# 检查 Claude Desktop
Write-Host "[1/2] 检查 Claude Desktop..." -ForegroundColor Yellow
$claudeConfig = "$env:APPDATA\Claude\claude_desktop_config.json"
if (Test-Path $claudeConfig) {
    try {
        $config = Get-Content $claudeConfig -Raw | ConvertFrom-Json
        if ($config.customInstructions.version -eq "2.4") {
            Write-Host "  ✓ Claude 配置正确" -ForegroundColor Green
            Write-Host "    版本: $($config.customInstructions.version)" -ForegroundColor Gray
            Write-Host "    来源: $($config.customInstructions.source)" -ForegroundColor Gray
            $results.claude = $true
        } else {
            Write-Host "  ✗ 配置版本不匹配" -ForegroundColor Red
        }
    } catch {
        Write-Host "  ✗ 配置文件格式错误" -ForegroundColor Red
    }
} else {
    Write-Host "  ○ Claude 未安装或未配置" -ForegroundColor Gray
}

# 检查 VSCode
Write-Host ""
Write-Host "[2/2] 检查 VSCode..." -ForegroundColor Yellow
$vscodeInstructions = "$env:APPDATA\Code\User\copilot-instructions.md"
$vscodeSettings = "$env:APPDATA\Code\User\settings.json"

if (Test-Path $vscodeInstructions) {
    $content = Get-Content $vscodeInstructions -Raw
    if ($content -match "AI Power Pack v2.4") {
        Write-Host "  ✓ Copilot 指令文件正确" -ForegroundColor Green
        
        if (Test-Path $vscodeSettings) {
            $settings = Get-Content $vscodeSettings -Raw | ConvertFrom-Json
            if ($settings.'github.copilot.chat.codeGeneration.instructions') {
                Write-Host "  ✓ VSCode settings.json 已配置" -ForegroundColor Green
                $results.vscode = $true
            }
        }
    }
} else {
    Write-Host "  ○ VSCode 未安装或未配置" -ForegroundColor Gray
}

# 显示结果
Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "验证结果" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

if ($results.claude) {
    Write-Host "✓ Claude Desktop: 已正确配置" -ForegroundColor Green
} else {
    Write-Host "○ Claude Desktop: 未配置" -ForegroundColor Gray
}

if ($results.vscode) {
    Write-Host "✓ VSCode Copilot: 已正确配置" -ForegroundColor Green
} else {
    Write-Host "○ VSCode Copilot: 未配置" -ForegroundColor Gray
}

Write-Host ""
Write-Host "下一步：重启应用以加载配置" -ForegroundColor Yellow
Write-Host ""

# 测试建议
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "测试建议" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. 询问 Claude: 'What coding standards do you follow?'" -ForegroundColor White
Write-Host "   期望回答包含: AI Power Pack v2.4" -ForegroundColor Gray
Write-Host ""
Write-Host "2. 请 AI 创建项目，观察是否先输出 PLAN" -ForegroundColor White
Write-Host ""
Write-Host "3. 检查生成的代码是否按功能分组文件" -ForegroundColor White
Write-Host ""
```

---

## 常见问题

### Q1: AI 回答不包含 AI Power Pack？
**原因：**
- 配置文件未生效
- 应用未重启
- 配置文件路径错误

**解决：**
1. 运行验证脚本检查配置
2. 重启 Claude Desktop / VSCode
3. 重新运行安装命令

---

### Q2: 配置文件存在但 AI 行为没变？
**原因：**
- 应用缓存未清除
- 配置格式错误
- Claude Desktop 版本过旧

**解决：**
1. 完全退出应用（结束进程）
2. 检查配置文件 JSON 格式
3. 更新到最新版本

---

### Q3: VSCode Copilot 没有使用规范？
**原因：**
- GitHub Copilot 扩展未安装
- 扩展未启用
- settings.json 路径错误

**解决：**
1. 安装 GitHub Copilot 扩展
2. 检查扩展是否启用
3. 验证 settings.json 路径

---

## 联系支持

如果验证失败，请提供：
1. 验证脚本的输出结果
2. 配置文件内容（敏感信息脱敏）
3. 应用版本信息
4. 操作系统版本

GitHub Issues: https://github.com/GQSDGQWE/AIDevKit/issues
