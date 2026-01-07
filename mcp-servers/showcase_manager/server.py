"""
Showcase Manager MCP Server
自主开发的 MCP 插件，用于管理 Showcase 项目。

PLAN:
1. 实现 MCP Tool: list_showcases (列出所有案例状态)
2. 实现 MCP Tool: launch_showcase (启动案例 GUI)
3. 符合 API-First 规则，本身提供标准接口。

EXECUTE:
"""

import os
import json
import subprocess
from mcp.server.fastmcp import FastMCP

# 初始化 MCP
mcp = FastMCP("ShowcaseManager")

SHOWCASE_ROOT = r"C:\Users\Buxiaomaomaozi\Desktop\CONSOL\showcase"

@mcp.tool()
def list_showcases() -> str:
    """列出目录下所有的 Showcase 案例及其路径"""
    if not os.path.exists(SHOWCASE_ROOT):
        return "Error: Showcase directory not found."
    
    dirs = [d for d in os.listdir(SHOWCASE_ROOT) if os.path.isdir(os.path.join(SHOWCASE_ROOT, d))]
    return json.dumps({"showcases": dirs, "root": SHOWCASE_ROOT}, indent=2)

@mcp.tool()
def launch_showcase(name: str) -> str:
    """启动指定案例的 GUI 界面"""
    target = os.path.join(SHOWCASE_ROOT, name, "gui.py")
    if not os.path.exists(target):
        # 兼容性检查: 部分案例可能是 monitor_gui 或 viewer_gui
        alt_names = ["gui.py", "monitor_gui.py", "viewer_gui.py"]
        found = False
        for alt in alt_names:
            target = os.path.join(SHOWCASE_ROOT, name, alt)
            if os.path.exists(target):
                found = True
                break
        if not found:
            return f"Error: GUI script not found in {name}"

    # 异步启动 (不阻塞 MCP 环境)
    subprocess.Popen([r"C:\ProgramData\anaconda3\Scripts\conda.exe", "run", "-p", r"C:\Users\Buxiaomaomaozi\.conda\envs\mathcupc", "python", target])
    return f"Success: Launched {name} GUI."

if __name__ == "__main__":
    mcp.run()
