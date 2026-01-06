using System;
using System.IO;
using System.Text;
using System.Diagnostics;
using System.Linq;

class Launcher {
    static string version = "2.4.0";
    
    static void Main(string[] args) {
        bool silentMode = args.Contains("-Silent") || args.Contains("-silent");
        bool verifyMode = args.Contains("-Verify") || args.Contains("-verify");
        
        if (verifyMode) {
            TestInstallation();
            return;
        }
        
        string psPath = FindPowerShell();
        if (psPath == null) {
            Console.WriteLine("ERROR: PowerShell not found on this system.");
            Console.WriteLine("Please install PowerShell to use this tool.");
            Console.ReadKey();
            return;
        }
        
        string script = GetEmbeddedScript(silentMode);
        string scriptPath = Path.Combine(Path.GetTempPath(), "deploy_" + Guid.NewGuid().ToString("N") + ".ps1");
        
        try {
            File.WriteAllText(scriptPath, script, new UTF8Encoding(true));
            
            ProcessStartInfo psi = new ProcessStartInfo {
                FileName = psPath,
                Arguments = string.Format("-NoProfile -ExecutionPolicy Bypass -File \"{0}\"", scriptPath),
                UseShellExecute = false,
                CreateNoWindow = silentMode,
                WorkingDirectory = AppDomain.CurrentDomain.BaseDirectory
            };
            
            using (Process proc = Process.Start(psi)) {
                proc.WaitForExit();
                if (proc.ExitCode != 0 && !silentMode) {
                    Console.WriteLine("\nDeployment completed with warnings. Press any key to exit...");
                    Console.ReadKey();
                }
            }
        }
        catch (Exception ex) {
            Console.WriteLine("ERROR: " + ex.Message);
            Console.ReadKey();
        }
        finally {
            try { File.Delete(scriptPath); } catch { }
        }
    }
    
    static string FindPowerShell() {
        string[] paths = {
            Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.System), "WindowsPowerShell", "v1.0", "powershell.exe"),
            Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.SystemX86), "WindowsPowerShell", "v1.0", "powershell.exe"),
            "powershell.exe"
        };
        
        foreach (string path in paths) {
            if (File.Exists(path)) return path;
            try {
                ProcessStartInfo psi = new ProcessStartInfo {
                    FileName = path,
                    Arguments = "-Version",
                    UseShellExecute = false,
                    CreateNoWindow = true,
                    RedirectStandardOutput = true
                };
                using (Process proc = Process.Start(psi)) {
                    proc.WaitForExit();
                    if (proc.ExitCode == 0) return path;
                }
            } catch { }
        }
        return null;
    }
    
    static void TestInstallation() {
        Console.WriteLine("\n========================================");
        Console.WriteLine("  AI Power Pack v" + version + " - Installation Verification");
        Console.WriteLine("========================================\n");
        
        string[] requiredFiles = {
            "CLAUDE.md",
            "INITIAL.md",
            ".cursorrules",
            ".github\\copilot-instructions.md"
        };
        
        string[] requiredContent = {
            "PLAN-EXECUTE",
            "200 lines",
            "Context Management",
            "Code Self-Execution"
        };
        
        string[] frameworks = {
            "Fabric",
            "Cursor Rules",
            "Context Engineering",
            "OpenSkills",
            "UI/UX Pro Max"
        };
        
        int filesPass = 0;
        int contentPass = 0;
        int frameworksPass = 0;
        
        Console.WriteLine("Stage 1: Checking Required Files...");
        foreach (string file in requiredFiles) {
            bool exists = File.Exists(file);
            Console.WriteLine("  [{0}] {1}", exists ? "✓" : "✗", file);
            if (exists) filesPass++;
        }
        
        Console.WriteLine("\nStage 2: Validating Content Quality...");
        foreach (string pattern in requiredContent) {
            bool found = false;
            foreach (string file in requiredFiles.Where(f => File.Exists(f))) {
                if (File.ReadAllText(file).Contains(pattern)) {
                    found = true;
                    break;
                }
            }
            Console.WriteLine("  [{0}] {1}", found ? "✓" : "✗", pattern);
            if (found) contentPass++;
        }
        
        Console.WriteLine("\nStage 3: Verifying Framework Integration...");
        foreach (string framework in frameworks) {
            bool found = false;
            foreach (string file in requiredFiles.Where(f => File.Exists(f))) {
                if (File.ReadAllText(file).Contains(framework)) {
                    found = true;
                    break;
                }
            }
            Console.WriteLine("  [{0}] {1}", found ? "✓" : "✗", framework);
            if (found) frameworksPass++;
        }
        
        Console.WriteLine("\nStage 4: System Information");
        Console.WriteLine("  OS: " + Environment.OSVersion);
        Console.WriteLine("  .NET: " + Environment.Version);
        Console.WriteLine("  Directory: " + Environment.CurrentDirectory);
        
        Console.WriteLine("\n========================================");
        Console.WriteLine("Verification Summary:");
        Console.WriteLine("  Files: {0}/{1} passed", filesPass, requiredFiles.Length);
        Console.WriteLine("  Content: {0}/{1} passed", contentPass, requiredContent.Length);
        Console.WriteLine("  Frameworks: {0}/{1} integrated", frameworksPass, frameworks.Length);
        Console.WriteLine("========================================\n");
        
        if (filesPass == requiredFiles.Length && contentPass == requiredContent.Length && frameworksPass == frameworks.Length) {
            Console.WriteLine("Status: ALL CHECKS PASSED ✓");
        } else {
            Console.WriteLine("Status: SOME CHECKS FAILED ✗");
            Console.WriteLine("\nTroubleshooting:");
            Console.WriteLine("  1. Run the installer in the project root directory");
            Console.WriteLine("  2. Ensure all files were deployed correctly");
            Console.WriteLine("  3. Check file permissions");
        }
        
        Console.WriteLine("\nPress any key to exit...");
        Console.ReadKey();
    }
    
    static string GetEmbeddedScript(bool silent) {
        return @"
$ErrorActionPreference = 'Stop'
$WorkingDir = Get-Location

function Smart-Write($path, $content) {
    $dir = Split-Path $path -Parent
    if ($dir -and !(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    if (Test-Path $path) {
        $backup = $path + '.backup'
        Copy-Item $path $backup -Force
    }
    [System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($true))
}

$ClaudeMdContent = @'
# AI Power Pack v2.4 - Project Context

> Based on 5 Battle-Tested Frameworks:
> Fabric | Awesome Cursor Rules | Context Engineering | OpenSkills | UI/UX Pro Max

---

## Global Requirements (MUST FOLLOW)

### Code Quality Standards
1. **Organized & Clear Structure** - Code must be well-organized
2. **Modular Files** - Single file max 200 lines
3. **Quality Over Quantity** - Code quality > file count/size
4. **Requirement-Driven** - Code must fulfill requirements
5. **Production-Ready** - Write production-ready code first try

### AI Must Follow
- Plan before code (PLAN -> EXECUTE pattern)
- Modular architecture (single responsibility)
- Clear file organization (feature-based grouping)
- High code quality (readable, maintainable, testable)
- Requirement fulfillment (solve the actual problem)

---

## Tech Stack Configuration
```yaml
framework: ""[Your Framework]""
language: ""[Your Language]""
database: ""[Your Database]""
```

## Coding Standards (From Fabric + Cursor Rules)

### File Organization
| Rule | Description |
|------|-------------|
| Max Lines | 200 lines per file |
| Single Responsibility | One component/module per file |
| Feature Grouping | Group by feature, not file type |

### PLAN-EXECUTE Pattern
```typescript
// PLAN:
// 1. Validate input
// 2. Process data
// 3. Return result

// EXECUTE:
function process(input) {
    // Step 1: Validate
    // Step 2: Process
    // Step 3: Return
}
```

## AI Behavior Rules (From Context Engineering)
1. **Research First** - Analyze existing patterns before coding
2. **Security** - Validate all inputs, sanitize outputs
3. **Performance** - Consider time/space complexity
4. **No Yapping** - Skip unnecessary explanations

## Git Version Control / Git版本控制

### Commit Guidelines / 提交规范
**Commit Message Format:**
```
type(scope): subject

Body (optional)
Footer (optional)
```

**Types / 类型:**
- `feat`: New feature / 新功能
- `fix`: Bug fix / 修复
- `docs`: Documentation / 文档
- `style`: Formatting / 格式化
- `refactor`: Code restructuring / 重构
- `test`: Tests / 测试
- `chore`: Build/tooling / 构建工具

**Examples / 示例:**
```bash
feat(auth): add OAuth2 login
fix(api): resolve null pointer in user service
docs(readme): update installation guide
refactor(utils): simplify validation logic
```

### Branch Strategy / 分支策略
```
main (production)     - 生产环境
├─ develop           - 开发主分支
   ├─ feature/xxx    - 功能分支
   ├─ bugfix/xxx     - 修复分支
   └─ hotfix/xxx     - 紧急修复
```

**Branch Naming / 分支命名:**
- `feature/user-authentication`
- `bugfix/login-error`
- `hotfix/security-patch`
- `refactor/database-layer`

### Best Practices / 最佳实践
1. **Commit Often** - Small, focused commits / 频繁提交，小而专注
2. **Atomic Commits** - One logical change per commit / 每次提交一个逻辑变更
3. **Write Descriptive Messages** - Clear ""what"" and ""why"" / 清晰说明做了什么和为什么
4. **Review Before Commit** - Use `git diff` / 提交前检查更改
5. **Never Commit Secrets** - Use .gitignore / 不提交敏感信息

### Workflow / 工作流程
```bash
# 1. Create feature branch / 创建功能分支
git checkout -b feature/new-feature develop

# 2. Make changes and commit / 开发并提交
git add .
git commit -m ""feat(module): add new feature""

# 3. Keep updated / 保持更新
git pull origin develop

# 4. Push and create PR / 推送并创建PR
git push origin feature/new-feature

# 5. After merge, delete branch / 合并后删除分支
git branch -d feature/new-feature
```

### .gitignore Template / 忽略文件模板
```gitignore
# Dependencies
node_modules/
venv/
__pycache__/
*.pyc

# Environment
.env
.env.local
*.log

# Build
dist/
build/
*.exe
*.dll

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

## Context Management for Large Models / 大模型上下文管理

### For Claude (200K) & Gemini (2M)
**Strategy: Prompt Caching + Periodic Summarization**

#### When to Summarize / 何时总结
- Every 50 messages or 100K tokens
- Before switching topics
- When context becomes cluttered

#### What to Keep / 保留内容
```yaml
Always Keep:
  - Project structure & tech stack
  - Global requirements (200 lines, PLAN-EXECUTE)
  - Current task context
  - Recent 10 messages

Compress:
  - Historical decisions → bullet points
  - Old conversations → key outcomes
  - Code snippets → references only
```

#### Summarization Template
```markdown
## Context Summary [Date]
**Project**: [Name]
**Stack**: [Tech]
**Completed**: 
  - Task 1: [outcome]
  - Task 2: [outcome]
**Current Focus**: [what's being worked on]
**Next Steps**: [what's next]
```

#### Claude-Specific: Prompt Caching
```python
# Mark static content for caching
CACHE_SECTIONS = [
    ""Global Requirements"",
    ""Tech Stack Configuration"", 
    ""Coding Standards"",
    ""Git Version Control""
]
```

### Best Practices / 最佳实践
1. **Start Fresh Wisely** - When >150K tokens, summarize and start new chat
2. **Reference Files** - Link to files instead of pasting full content
3. **Compress History** - Keep decisions, drop verbose discussions
4. **Use Artifacts** - For long code, use Claude Artifacts / Gemini Code Execution

---

## Code Self-Execution / 代码自运行增强

### Playground-Style Code / Playground风格代码
**Every code file MUST be immediately runnable**

#### Template Structure
```python
# PLAN:
# 1. Define function
# 2. Add tests
# 3. Add main execution

# EXECUTE:
def my_function(param):
    """"""Function logic""""""
    return result

# Self-test examples
if __name__ == ""__main__"":
    # Example 1: Basic usage
    print(""Test 1:"", my_function(""test""))
    
    # Example 2: Edge case
    print(""Test 2:"", my_function(""""))
    
    # Example 3: Performance
    import time
    start = time.time()
    my_function(""benchmark"")
    print(f""Execution time: {time.time()-start:.4f}s"")
```

#### Auto-Generate Test Cases
```typescript
// PLAN:
// 1. Function implementation
// 2. Unit tests
// 3. Integration test

// EXECUTE:
export function calculate(a: number, b: number): number {
    return a + b;
}

// Auto-tests (run with: node script.ts)
if (require.main === module) {
    console.assert(calculate(2, 3) === 5, ""Basic test"");
    console.assert(calculate(-1, 1) === 0, ""Negative test"");
    console.assert(calculate(0, 0) === 0, ""Zero test"");
    console.log(""✓ All tests passed"");
}
```

#### Quick Run Commands
```yaml
Python:   ""python script.py""
Node.js:  ""node script.js"" or ""ts-node script.ts""
Java:     ""java ClassName.java""
Go:       ""go run main.go""
Rust:     ""rustc main.rs && ./main""
```

### Requirements / 要求
- [ ] Every file has `if __name__ == ""__main__""` block
- [ ] Include 3+ test examples per function
- [ ] Add execution time measurement for performance-critical code
- [ ] Print clear output showing test results

---

## Additional Best Practices / 补充最佳实践

### API Key Management / API密钥管理
```python
# ✓ CORRECT
import os
API_KEY = os.getenv('API_KEY')

# ✗ WRONG
API_KEY = ""sk-1234567890abcdef""  # Never hardcode!
```

**Rules:**
- Always use environment variables
- Add `.env` to `.gitignore`
- Provide `.env.example` template
- Use secrets management in production (AWS Secrets, Azure Key Vault)

### Logging Standards / 日志规范
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info(""Operation successful"")
logger.error(""Error occurred"", exc_info=True)
```

**Log Levels:**
- `DEBUG`: Detailed diagnostic info
- `INFO`: General informational messages
- `WARNING`: Warning messages
- `ERROR`: Error messages
- `CRITICAL`: Critical issues

### Dependency Management / 依赖管理
```bash
# Python
pip freeze > requirements.txt
pip install -r requirements.txt

# Node.js
npm install
npm ci  # for CI/CD

# Lock versions
requirements.txt: package==1.2.3
package.json: ""package"": ""^1.2.3""
```

### Docker Best Practices / Docker最佳实践
```dockerfile
# Multi-stage build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .
CMD [""python"", ""main.py""]
```

### CI/CD Pipeline / 持续集成
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: pytest
      - name: Lint
        run: flake8 .
```

### Performance Monitoring / 性能监控
```python
import time
import functools

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f""{func.__name__}: {end-start:.4f}s"")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
```

### Documentation Generation / 文档生成
```python
def calculate_total(items: list[float], tax_rate: float = 0.1) -> float:
    """"""
    Calculate total price with tax.
    
    Args:
        items: List of item prices
        tax_rate: Tax rate (default 10%)
        
    Returns:
        Total price including tax
        
    Example:
        >>> calculate_total([10, 20, 30], 0.1)
        66.0
    """"""
    subtotal = sum(items)
    return subtotal * (1 + tax_rate)
```

**Tools:**
- Python: Sphinx, MkDocs
- JavaScript: JSDoc, TypeDoc
- Auto-generate: `sphinx-apidoc`, `typedoc`

---

## Project-Specific Rules
> Add your custom rules below:
- [ ] Rule 1: ...
- [ ] Rule 2: ...
'@

$InitialMdContent = @'
# Feature Description Template

## Feature Name
[Name of the feature]

## Problem Statement
[What problem does this solve?]

## User Story
As a [user type], I want to [action], so that [benefit].

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Technical Design
### API Changes
```
POST /api/feature
Request: { ... }
Response: { ... }
```

### File Structure
```
feature-name/
  components/
  hooks/
  services/
  types/
  index.ts
```
'@

$CursorRulesContent = @'
# Cursor AI Rules - AI Power Pack v2.4

## CRITICAL RULES (MUST FOLLOW)

### Global Quality Requirements
1. CODE MUST BE ORGANIZED AND CLEAR
2. SINGLE FILE < 200 LINES
3. QUALITY > QUANTITY
4. MUST FULFILL REQUIREMENTS
5. PRODUCTION-READY ON FIRST TRY

## Core Principles (From Fabric + Cursor Rules)
- Write production-ready code on first try
- Follow project conventions in CLAUDE.md
- Prefer composition over inheritance
- Keep functions pure when possible

## PLAN-EXECUTE Pattern (MANDATORY)
```
// PLAN:
// 1. [Step 1]
// 2. [Step 2]
// 3. [Step 3]

// EXECUTE:
function implement() { ... }
```

## File Size Limits
| File Type | Max Lines |
|-----------|-----------|
| Component | 200 |
| Hook | 100 |
| Service | 150 |
| Utility | 100 |

## Security Rules (From OpenSkills)
- Validate all user inputs
- Use parameterized queries
- Never log sensitive data
- Handle errors gracefully

## UI/UX Standards (From UI/UX Pro Max)
- Consistent design language
- Mobile-first responsive
- Clear user feedback
- Accessible (WCAG 2.1)

## Git Version Control Rules / Git版本控制规则

### Commit Messages / 提交信息
```
MUST follow format:
type(scope): subject

Examples:
feat(auth): implement JWT authentication
fix(api): handle null user response
docs(readme): add setup instructions
refactor(utils): simplify date formatting
```

### Before Every Commit / 每次提交前
- [ ] Run tests / 运行测试
- [ ] Check linting / 检查代码规范
- [ ] Review changes / 检查更改
- [ ] Update docs if needed / 必要时更新文档

### Branch Rules / 分支规则
- Feature branches from `develop`
- Hotfix branches from `main`
- Delete branch after merge
- Keep branches short-lived (< 3 days)

## Context Management Rules / 上下文管理规则

### When Context > 100K Tokens
1. Summarize completed tasks
2. Extract key decisions to bullet points
3. Keep only recent 10-20 messages
4. Reference files instead of full content

### Claude/Gemini Optimization
- Use Prompt Caching for static rules
- Compress historical conversations
- Start fresh chat when >150K tokens
- Keep project structure always visible

## Code Self-Execution / 代码自运行

### MUST Include in Every File
```python
if __name__ == ""__main__"":
    # Test 1: Basic
    print(""Test 1:"", function(""input""))
    
    # Test 2: Edge case
    print(""Test 2:"", function(""""))
    
    # Test 3: Performance
    import time
    start = time.time()
    function(""benchmark"")
    print(f""Time: {time.time()-start:.4f}s"")
```

### Auto-Test Requirements
- [ ] 3+ test cases per function
- [ ] Clear output showing results
- [ ] Performance measurement for key functions
- [ ] Can run with single command

## Additional Standards / 补充标准

### API Keys
```python
# ✓ Use environment variables
import os
KEY = os.getenv('API_KEY')

# ✗ Never hardcode
KEY = ""sk-123456""  # FORBIDDEN!
```

### Logging
```python
import logging
logger = logging.getLogger(__name__)
logger.info(""Message"")  # Not print()
```

### Dependencies
- Python: Include requirements.txt
- Node.js: Include package.json
- Lock all versions

### Documentation
- Docstrings for all functions
- Type hints (Python 3.10+)
- Example usage in docstring

## Never Commit / 绝不提交
- Secrets, API keys, passwords
- node_modules, venv, __pycache__
- Build artifacts (dist/, build/)
- IDE config (.vscode/, .idea/)
- Personal configs (.env.local)
'@

$CopilotInstructionsContent = @'
# GitHub Copilot Instructions - AI Power Pack v2.4

## GLOBAL REQUIREMENTS (CRITICAL)
1. Code MUST be organized and clear
2. Single file MUST NOT exceed 200 lines
3. Quality > Quantity
4. Code MUST fulfill requirements
5. Every file MUST have high code quality

## Code Generation Rules

### ALWAYS DO
1. Use PLAN-EXECUTE pattern for complex logic
2. Split large files into smaller modules
3. Follow project conventions in CLAUDE.md
4. Write self-documenting code
5. Handle all error cases

### NEVER DO
- Generate files > 200 lines
- Skip error handling
- Use `any` type in TypeScript
- Leave TODO without issue reference

## Quality Checklist
- [ ] All files <= 200 lines
- [ ] PLAN comments present
- [ ] Types are explicit
- [ ] Errors handled
- [ ] Requirements fulfilled

## Git Integration / Git集成

### Generate Commit Messages
When asked to generate commit message:
```
Analyze changes → Determine type → Write clear subject

Format: type(scope): subject

Examples:
- feat(ui): add dark mode toggle
- fix(auth): resolve token expiration bug
- refactor(db): optimize query performance
```

### Pre-Commit Checklist
Before suggesting commit:
1. Check all files < 200 lines
2. Verify no secrets in code
3. Ensure tests pass
4. Confirm proper .gitignore

### Branch Suggestions
When creating feature:
- Suggest: `feature/descriptive-name`
- For bugs: `bugfix/issue-description`
- For urgent: `hotfix/critical-fix`

### .gitignore Generation
Always include in new projects:
```gitignore
# Language-specific
node_modules/, venv/, __pycache__/

# Environment & Secrets
.env, .env.local, *.key, *.pem

# Build & Artifacts
dist/, build/, *.exe, *.dll

# IDE & OS
.vscode/, .idea/, .DS_Store, Thumbs.db
```

## Context Management / 上下文管理

### For Claude (200K) & Gemini (2M)
When conversation exceeds 100K tokens:
1. **Summarize**: Compress completed work to key outcomes
2. **Extract**: Pull out important decisions/patterns
3. **Trim**: Keep recent 10-20 messages only
4. **Reference**: Link files instead of pasting content

### Summarization Format
```markdown
## Summary [Date]
**Completed**: 
- Feature X: [result]
- Bug Y: [fixed]
**Current**: [active work]
**Next**: [pending tasks]
```

## Code Self-Execution / 代码自运行

### Every File Must Be Runnable
When generating code, ALWAYS include:

```python
if __name__ == ""__main__"":
    # Test 1: Basic usage
    result = my_function(""test"")
    print(f""Test 1: {result}"")
    
    # Test 2: Edge case
    result = my_function("""")
    print(f""Test 2: {result}"")
    
    # Test 3: Performance
    import time
    start = time.time()
    my_function(""benchmark"")
    print(f""Execution: {time.time()-start:.4f}s"")
```

### TypeScript/JavaScript
```typescript
if (require.main === module) {
    console.assert(myFunction(2, 3) === 5);
    console.log(""✓ Tests passed"");
}
```

## Additional Best Practices / 补充最佳实践

### API Key Security
```python
# ✓ CORRECT
import os
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError(""API_KEY not set"")

# ✗ NEVER
API_KEY = ""hardcoded-key""  # FORBIDDEN!
```

### Logging Over Print
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(""Use this"")  # Not print()
```

### Dependency Files
ALWAYS generate:
- Python: `requirements.txt`
- Node.js: `package.json` with versions
- Docker: `Dockerfile` for containerization

### Documentation
Every function needs:
```python
def calculate(x: int, y: int) -> int:
    """"""
    Calculate sum of two numbers.
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        Sum of x and y
        
    Example:
        >>> calculate(2, 3)
        5
    """"""
    return x + y
```
'@

try {
    Smart-Write 'CLAUDE.md' $ClaudeMdContent
    Smart-Write 'INITIAL.md' $InitialMdContent
    Smart-Write '.cursorrules' $CursorRulesContent
    Smart-Write '.github\copilot-instructions.md' $CopilotInstructionsContent
    
    if (!" + (silent ? "1" : "0") + @") {
        Write-Host ""`n========================================"" -ForegroundColor Green
        Write-Host ""  AI Power Pack v2.4.0 - Enhanced Edition"" -ForegroundColor Green
        Write-Host ""========================================`n"" -ForegroundColor Green
        Write-Host ""Files Created:"" -ForegroundColor Cyan
        Write-Host ""  ✓ CLAUDE.md (Enhanced)"" -ForegroundColor White
        Write-Host ""  ✓ INITIAL.md"" -ForegroundColor White
        Write-Host ""  ✓ .cursorrules (Enhanced)"" -ForegroundColor White
        Write-Host ""  ✓ .github\copilot-instructions.md (Enhanced)"" -ForegroundColor White
        Write-Host ""`n🆕 New Features:"" -ForegroundColor Yellow
        Write-Host ""  ✓ Context Management (Claude 200K / Gemini 2M)"" -ForegroundColor White
        Write-Host ""  ✓ Code Self-Execution (Playground-style)"" -ForegroundColor White
        Write-Host ""  ✓ API Key Security"" -ForegroundColor White
        Write-Host ""  ✓ Logging Standards"" -ForegroundColor White
        Write-Host ""  ✓ Docker Best Practices"" -ForegroundColor White
        Write-Host ""  ✓ CI/CD Pipeline Templates"" -ForegroundColor White
        Write-Host ""  ✓ Performance Monitoring"" -ForegroundColor White
        Write-Host ""  ✓ Auto Documentation"" -ForegroundColor White
        Write-Host ""`nFrameworks Integrated:"" -ForegroundColor Cyan
        Write-Host ""  • Fabric (37.8k⭐) - AI Patterns"" -ForegroundColor White
        Write-Host ""  • Awesome Cursor Rules (36.7k⭐) - Best Practices"" -ForegroundColor White
        Write-Host ""  • Context Engineering - Project Structure"" -ForegroundColor White
        Write-Host ""  • OpenSkills - Security Standards"" -ForegroundColor White
        Write-Host ""  • UI/UX Pro Max - Design Principles"" -ForegroundColor White
        Write-Host ""`nOptimized for:"" -ForegroundColor Magenta
        Write-Host ""  🤖 Claude Sonnet 4.5 (200K context)"" -ForegroundColor White
        Write-Host ""  🤖 Gemini 2.0 Flash (2M context)"" -ForegroundColor White
        Write-Host ""`nNext Steps:"" -ForegroundColor Yellow
        Write-Host ""  1. Initialize Git: git init"" -ForegroundColor White
        Write-Host ""  2. Write playground-style code (self-runnable)"" -ForegroundColor White
        Write-Host ""  3. Use context summarization every 50 messages"" -ForegroundColor White
        Write-Host ""  4. Read GIT_GUIDE.md for Git workflow"" -ForegroundColor White
        Write-Host ""`nPress any key to continue..."" -ForegroundColor Gray
        $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
    }
    exit 0
} catch {
    Write-Host ""`nERROR: $($_.Exception.Message)"" -ForegroundColor Red
    Write-Host ""`nTroubleshooting:"" -ForegroundColor Yellow
    Write-Host ""  1. Run as Administrator"" -ForegroundColor White
    Write-Host ""  2. Check disk space"" -ForegroundColor White
    Write-Host ""  3. Verify write permissions"" -ForegroundColor White
    Write-Host ""`nPress any key to exit..."" -ForegroundColor Gray
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
    exit 1
}
";
    }
}
