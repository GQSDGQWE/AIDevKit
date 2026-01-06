# Project 2: Log Analyzer CLI Tool / 日志分析CLI工具

## 📋 项目目标
创建一个命令行工具用于分析服务器日志，验证AI Power Pack框架的CLI开发和数据处理能力。

## 🎯 测试的框架功能
- ✅ 200行代码限制
- ✅ PLAN-EXECUTE模式
- ✅ 模块化设计
- ✅ 代码自运行（单元测试）
- ✅ 性能基准测试
- ✅ 错误学习机制
- ✅ 持续执行工作流

## 🏗️ 技术栈
- **Language**: Python 3.11
- **CLI Framework**: argparse
- **Data Processing**: pandas (optional)
- **Testing**: Built-in unittest
- **Output**: Markdown reports

## 📁 项目结构
```
log_analyzer/
├── README.md          # 项目说明
├── parser.py          # 日志解析器 (<200 lines)
├── analyzer.py        # 数据分析器 (<200 lines)
├── reporter.py        # 报告生成器 (<200 lines)
├── main.py            # CLI入口 (<150 lines)
├── sample_logs.txt    # 示例日志文件
└── requirements.txt   # 依赖列表
```

## 🚀 迭代计划

### Iteration 1: 日志解析
- [x] 读取日志文件
- [x] 解析常见日志格式（Apache, Nginx, custom）
- [x] 提取关键信息（时间戳、IP、状态码、URL）
- [x] 单元测试

### Iteration 2: 数据分析
- [ ] 统计分析（请求数、错误率）
- [ ] 时间序列分析（每小时请求量）
- [ ] IP分析（top访问者）
- [ ] 错误分析（404/500统计）

### Iteration 3: 报告生成
- [ ] Markdown报告生成
- [ ] 可视化数据（ASCII图表）
- [ ] 导出CSV
- [ ] 性能优化

## 📊 成功指标
- ✅ 所有文件 < 200行
- ✅ 所有函数有PLAN注释
- ✅ 测试覆盖率 > 80%
- ✅ 处理速度: > 10,000 lines/sec
- ✅ 内存占用: < 100MB

## 🔧 运行方法
```bash
# 安装依赖
pip install -r requirements.txt

# 运行测试
python parser.py
python analyzer.py
python reporter.py

# 分析日志
python main.py --file sample_logs.txt --output report.md

# 查看报告
cat report.md
```

## 📝 示例日志格式
```
2026-01-07 10:23:45 - INFO - 192.168.1.100 - GET /api/users - 200 - 45ms
2026-01-07 10:24:12 - ERROR - 192.168.1.101 - POST /api/login - 401 - 12ms
2026-01-07 10:25:03 - WARN - 192.168.1.102 - GET /api/data - 404 - 8ms
```

---
**开始时间**: 2026-01-07  
**预计完成**: Iteration 1 (30分钟)
