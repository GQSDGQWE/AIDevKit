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
framework: "[Your Framework]"
language: "[Your Language]"
database: "[Your Database]"
```

## Coding Standards (From Fabric + Cursor Rules)

### File Organization
| Rule | Description |
|------|-------------|
| Max Lines | 500 lines per file (flexible guideline) |
| API-First | Every project must provide an API or SDK for external control |
| MCP Management | AI can autonomously search/install/develop MCP servers |
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

## AI Workflow Rules / AI工作流程规则

### Continuous Execution / 持续执行
**Rule**: AI should continue working until task is complete unless encountering critical safety issues.

**Continue Working**:
- Multiple file operations
- Iterative improvements
- Testing and debugging
- Documentation updates
- Code refactoring

**STOP and Ask Confirmation**:
- ❌ Deleting multiple files (>3 files)
- ❌ Dropping database tables
- ❌ Removing entire directories
- ❌ Modifying production configs
- ❌ Changing critical system files

**Default Behavior**: 🚀 Keep executing → Complete the task → Report results

### User Intent Analysis / 用户意图分析

**3-Step Process when user provides requirement:**

```yaml
Step 1: Analyze Intent / 分析意图
  - What is the user trying to achieve?
  - What is the technical goal?
  - What are the implicit requirements?
  
Step 2: Supplement Technical Details / 补充技术细节
  - Break down into technical steps
  - Identify required files/modules
  - Determine tech stack and tools
  - Plan architecture and data flow
  
Step 3: Execute Implementation / 执行实现
  - Follow PLAN-EXECUTE pattern
  - Create/modify files as needed
  - Test and verify
  - Document changes
```

**Example:**

**User Says**: "我想添加登录功能" (I want to add login)

**AI Should Do**:
1. **Analyze**: User needs authentication system with login UI + backend validation
2. **Supplement**: Need login form component, auth service, JWT token handling, password encryption, session management
3. **Execute**: Create LoginForm.tsx, authService.ts, add auth middleware, update routes

**DON'T**: Immediately ask "what framework?" or "what database?"
**DO**: Check project structure → Infer tech stack → Ask only if truly ambiguous

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
3. **Write Descriptive Messages** - Clear "what" and "why" / 清晰说明做了什么和为什么
4. **Review Before Commit** - Use `git diff` / 提交前检查更改
5. **Never Commit Secrets** - Use .gitignore / 不提交敏感信息

### Workflow / 工作流程
```bash
# 1. Create feature branch / 创建功能分支
git checkout -b feature/new-feature develop

# 2. Make changes and commit / 开发并提交
git add .
git commit -m "feat(module): add new feature"

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
    "Global Requirements",
    "Tech Stack Configuration", 
    "Coding Standards",
    "Git Version Control"
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
    """Function logic"""
    return result

# Self-test examples
if __name__ == "__main__":
    # Example 1: Basic usage
    print("Test 1:", my_function("test"))
    
    # Example 2: Edge case
    print("Test 2:", my_function(""))
    
    # Example 3: Performance
    import time
    start = time.time()
    my_function("benchmark")
    print(f"Execution time: {time.time()-start:.4f}s")
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
    console.assert(calculate(2, 3) === 5, "Basic test");
    console.assert(calculate(-1, 1) === 0, "Negative test");
    console.assert(calculate(0, 0) === 0, "Zero test");
    console.log("✓ All tests passed");
}
```

#### Quick Run Commands
```yaml
Python:   "python script.py"
Node.js:  "node script.js" or "ts-node script.ts"
Java:     "java ClassName.java"
Go:       "go run main.go"
Rust:     "rustc main.rs && ./main"
```

### Requirements / 要求
- [ ] Every file has `if __name__ == "__main__"` block
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
API_KEY = "sk-1234567890abcdef"  # Never hardcode!
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
logger.info("Operation successful")
logger.error("Error occurred", exc_info=True)
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
package.json: "package": "^1.2.3"
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
CMD ["python", "main.py"]
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
        print(f"{func.__name__}: {end-start:.4f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
```

### Documentation Generation / 文档生成
```python
def calculate_total(items: list[float], tax_rate: float = 0.1) -> float:
    """
    Calculate total price with tax.
    
    Args:
        items: List of item prices
        tax_rate: Tax rate (default 10%)
        
    Returns:
        Total price including tax
        
    Example:
        >>> calculate_total([10, 20, 30], 0.1)
        66.0
    """
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