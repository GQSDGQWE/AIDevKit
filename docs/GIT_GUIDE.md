# Git Version Control Template / Git版本控制模板

## Quick Start / 快速开始

### Initialize Repository / 初始化仓库
```bash
# Initialize git
git init

# Add remote (GitHub/GitLab)
git remote add origin https://github.com/username/repo.git

# First commit
git add .
git commit -m "chore: initial commit"
git push -u origin main
```

### Daily Workflow / 日常工作流
```bash
# 1. Update local code
git pull origin develop

# 2. Create feature branch
git checkout -b feature/my-feature

# 3. Make changes and stage
git add src/feature.py

# 4. Commit with message
git commit -m "feat(feature): add new capability"

# 5. Push to remote
git push origin feature/my-feature

# 6. Create Pull Request on GitHub/GitLab
```

---

## Commit Message Convention / 提交信息规范

### Format
```
type(scope): subject

[optional body]

[optional footer]
```

### Types
| Type | Description | 说明 |
|------|-------------|------|
| `feat` | New feature | 新功能 |
| `fix` | Bug fix | 修复Bug |
| `docs` | Documentation only | 仅文档更改 |
| `style` | Code style (formatting, semicolons) | 代码格式 |
| `refactor` | Code restructuring | 重构代码 |
| `perf` | Performance improvement | 性能优化 |
| `test` | Add/update tests | 测试相关 |
| `build` | Build system, dependencies | 构建系统 |
| `ci` | CI/CD config | CI配置 |
| `chore` | Other changes | 其他杂项 |
| `revert` | Revert previous commit | 回滚提交 |

### Examples / 示例
```bash
# Feature
git commit -m "feat(auth): implement OAuth2 login flow"

# Bug Fix
git commit -m "fix(api): handle null response in user endpoint"

# Documentation
git commit -m "docs(readme): update installation instructions"

# Refactor
git commit -m "refactor(utils): simplify date formatting logic"

# Performance
git commit -m "perf(db): add index to users table"

# Multiple files
git commit -m "feat(cart): add item quantity controls

- Add increment/decrement buttons
- Update total calculation
- Add input validation"
```

---

## Branch Strategy / 分支策略

### Git Flow Model
```
main (protected)
├── develop (integration)
│   ├── feature/user-authentication
│   ├── feature/payment-gateway
│   ├── bugfix/login-redirect
│   └── refactor/api-layer
├── release/v1.2.0 (staging)
└── hotfix/critical-security-fix
```

### Branch Types / 分支类型
| Branch | Purpose | From | Merge To |
|--------|---------|------|----------|
| `main` | Production code | - | - |
| `develop` | Integration branch | main | main |
| `feature/*` | New features | develop | develop |
| `bugfix/*` | Bug fixes | develop | develop |
| `hotfix/*` | Urgent fixes | main | main + develop |
| `release/*` | Release preparation | develop | main + develop |

### Naming Convention / 命名规范
```bash
feature/短横线分隔的功能名
feature/user-profile-page
feature/oauth2-integration
feature/dark-mode

bugfix/短横线分隔的问题描述
bugfix/login-form-validation
bugfix/api-timeout-error

hotfix/紧急修复描述
hotfix/security-vulnerability
hotfix/payment-gateway-down

release/版本号
release/v1.2.0
release/v2.0.0-beta
```

---

## Best Practices / 最佳实践

### Commit Frequency / 提交频率
✅ **DO:**
- Commit early and often / 频繁提交
- One logical change per commit / 每次提交一个逻辑变更
- Commit working code / 提交可运行的代码
- Use meaningful messages / 使用有意义的提交信息

❌ **DON'T:**
- Commit broken code / 提交无法运行的代码
- Mix unrelated changes / 混合不相关的更改
- Use vague messages like "fix" or "update" / 使用模糊信息
- Commit generated files / 提交生成的文件

### Before Every Commit / 每次提交前
```bash
# 1. Review changes
git diff

# 2. Run tests
npm test  # or pytest, go test, etc.

# 3. Check linting
npm run lint

# 4. Stage files
git add <files>

# 5. Commit
git commit -m "type(scope): message"
```

### Pull Request Checklist / PR检查清单
- [ ] Branch is up-to-date with target branch
- [ ] All tests passing
- [ ] Code reviewed by at least 1 person
- [ ] No merge conflicts
- [ ] Documentation updated
- [ ] CHANGELOG updated (if applicable)

---

## .gitignore Template / 忽略文件模板

### Universal
```gitignore
# Environment variables
.env
.env.local
.env.*.local

# Logs
*.log
logs/
npm-debug.log*

# OS
.DS_Store
Thumbs.db
desktop.ini
```

### Node.js
```gitignore
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.npm
.yarn/cache
dist/
build/
```

### Python
```gitignore
__pycache__/
*.py[cod]
*$py.class
venv/
env/
.Python
*.egg-info/
dist/
build/
```

### IDE
```gitignore
# VS Code
.vscode/
*.code-workspace

# JetBrains
.idea/
*.iml

# Vim
*.swp
*.swo
*~
```

---

## Useful Commands / 实用命令

### Undoing Changes / 撤销更改
```bash
# Discard changes in working directory
git restore <file>

# Unstage file (keep changes)
git restore --staged <file>

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert commit (create new commit)
git revert <commit-hash>
```

### Branch Management / 分支管理
```bash
# List branches
git branch -a

# Switch branch
git checkout develop

# Create and switch
git checkout -b feature/new-feature

# Delete local branch
git branch -d feature/old-feature

# Delete remote branch
git push origin --delete feature/old-feature

# Rename branch
git branch -m old-name new-name
```

### Stashing / 暂存
```bash
# Save changes temporarily
git stash save "work in progress"

# List stashes
git stash list

# Apply latest stash
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Drop stash
git stash drop stash@{0}
```

### History & Logs / 历史记录
```bash
# View commit history
git log --oneline --graph --all

# View file history
git log --follow <file>

# Show commit details
git show <commit-hash>

# Search commits
git log --grep="bug fix"

# Find who changed a line
git blame <file>
```

---

## Collaboration / 协作

### Code Review / 代码审查
```bash
# Fetch latest changes
git fetch origin

# Review PR locally
git fetch origin pull/123/head:pr-123
git checkout pr-123

# Leave feedback as comments on GitHub/GitLab
# Approve or request changes
```

### Resolving Conflicts / 解决冲突
```bash
# Pull latest changes
git pull origin develop

# If conflicts occur:
# 1. Open conflicted files
# 2. Look for <<<<<<< ======= >>>>>>>
# 3. Manually resolve conflicts
# 4. Stage resolved files
git add <resolved-files>

# 5. Complete merge
git commit -m "merge: resolve conflicts with develop"
```

---

## Security / 安全

### Never Commit / 禁止提交
❌ API keys, passwords, tokens
❌ Private keys (.pem, .key)
❌ Database credentials
❌ OAuth secrets
❌ Personal data (emails, phone numbers)

### If Accidentally Committed / 如果不小心提交了
```bash
# Remove from history (last commit)
git rm --cached <file>
git commit --amend

# Remove from entire history (dangerous!)
git filter-branch --index-filter \
  "git rm -rf --cached --ignore-unmatch <file>" HEAD

# Force push (use with caution)
git push --force

# Better: Use tools like BFG Repo-Cleaner
```

---

## Resources / 资源

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Oh Shit, Git!](https://ohshitgit.com/)
