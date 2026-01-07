"""
框架打包工具 - 将项目打包成可分发的格式
Framework Packager - Package the project for distribution
"""
import os
import shutil
import zipfile
import json
from pathlib import Path
from datetime import datetime

class FrameworkPackager:
    def __init__(self):
        self.root = Path(__file__).parent.parent
        self.version = "2.4"
        self.package_name = f"AI_Power_Pack_v{self.version}"
        self.output_dir = self.root / 'dist' / 'packages'
        
    def create_package_structure(self) -> Path:
        """创建打包目录结构"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        package_dir = self.output_dir / f"{self.package_name}_{timestamp}"
        
        # 创建目录结构
        dirs = [
            package_dir / 'config',
            package_dir / 'projects',
            package_dir / 'tools',
            package_dir / 'docs',
            package_dir / 'examples',
            package_dir / 'mcp-servers'
        ]
        
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        return package_dir
    
    def copy_configs(self, package_dir: Path):
        """复制配置文件"""
        print("📋 复制配置文件...")
        config_src = self.root / 'config'
        config_dst = package_dir / 'config'
        
        for file in config_src.glob('*.md'):
            if not file.name.endswith('.backup'):
                shutil.copy2(file, config_dst / file.name)
                print(f"  ✓ {file.name}")
    
    def copy_projects(self, package_dir: Path):
        """复制项目文件"""
        print("📦 复制项目代码...")
        projects_src = self.root / 'projects'
        projects_dst = package_dir / 'projects'
        
        # 排除目录
        exclude_dirs = {'__pycache__', '.pytest_cache', 'node_modules', '.venv'}
        exclude_files = {'*.pyc', '*.pyo', '*.db'}
        
        for project in projects_src.iterdir():
            if project.is_dir() and project.name not in exclude_dirs:
                dst = projects_dst / project.name
                shutil.copytree(
                    project, 
                    dst, 
                    ignore=shutil.ignore_patterns(*exclude_files, *exclude_dirs)
                )
                print(f"  ✓ {project.name}")
    
    def copy_tools(self, package_dir: Path):
        """复制工具脚本"""
        print("🔧 复制工具脚本...")
        tools_src = self.root / 'tools'
        tools_dst = package_dir / 'tools'
        
        tool_files = [
            'cleanup.py',
            'deploy_config.py',
            'package_framework.py',
            'One-Click-Deploy.bat'
        ]
        
        for tool in tool_files:
            src = tools_src / tool
            if src.exists():
                shutil.copy2(src, tools_dst / tool)
                print(f"  ✓ {tool}")
    
    def copy_docs(self, package_dir: Path):
        """复制文档"""
        print("📚 复制文档...")
        docs_src = self.root / 'docs'
        docs_dst = package_dir / 'docs'
        
        for doc in docs_src.glob('*.md'):
            if not doc.name.endswith('.backup'):
                shutil.copy2(doc, docs_dst / doc.name)
                print(f"  ✓ {doc.name}")
        
        # 复制主 README
        readme_src = self.root / 'README.md'
        if readme_src.exists():
            shutil.copy2(readme_src, package_dir / 'README.md')
            print(f"  ✓ README.md")
    
    def copy_examples(self, package_dir: Path):
        """复制示例代码"""
        print("💡 复制示例代码...")
        examples_src = self.root / 'showcase'
        examples_dst = package_dir / 'examples'
        
        if examples_src.exists():
            for example in examples_src.iterdir():
                if example.is_dir() and not example.name.startswith('.'):
                    dst = examples_dst / example.name
                    shutil.copytree(
                        example,
                        dst,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '*.db')
                    )
                    print(f"  ✓ {example.name}")
    
    def copy_mcp_servers(self, package_dir: Path):
        """复制 MCP 服务器"""
        print("🔌 复制 MCP 服务器...")
        mcp_src = self.root / 'mcp-servers'
        mcp_dst = package_dir / 'mcp-servers'
        
        if mcp_src.exists():
            try:
                shutil.copytree(
                    mcp_src,
                    mcp_dst,
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc', 'node_modules'),
                    dirs_exist_ok=True
                )
                print(f"  ✓ MCP 服务器已复制")
            except Exception as e:
                print(f"  ⚠ MCP 服务器复制警告: {str(e)}")
        else:
            print(f"  - MCP 服务器目录不存在，跳过")
    
    def create_manifest(self, package_dir: Path):
        """创建清单文件"""
        print("📝 创建清单文件...")
        manifest = {
            'name': 'AI Power Pack',
            'version': self.version,
            'description': 'Professional AI development framework with Claude and VSCode integration',
            'author': 'CONSOL Team',
            'created': datetime.now().isoformat(),
            'components': {
                'config': 'Configuration files for Claude and VSCode',
                'projects': 'Sample projects and frameworks',
                'tools': 'Deployment and utility tools',
                'docs': 'Documentation',
                'examples': 'Example implementations',
                'mcp-servers': 'Model Context Protocol servers'
            },
            'installation': {
                'step1': 'Run: python tools/cleanup.py (optional)',
                'step2': 'Run: python tools/deploy_config.py',
                'step3': 'Restart Claude Desktop and VSCode',
                'step4': 'Start coding with AI Power Pack!'
            },
            'requirements': {
                'python': '>=3.8',
                'vscode': 'Latest version recommended',
                'claude': 'Claude Desktop recommended'
            }
        }
        
        manifest_file = package_dir / 'manifest.json'
        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        
        print(f"  ✓ manifest.json")
    
    def create_installation_script(self, package_dir: Path):
        """创建安装脚本"""
        print("📜 创建安装脚本...")
        
        # Windows 批处理脚本
        batch_script = """@echo off
echo ========================================
echo AI Power Pack v2.4 - Installation
echo ========================================
echo.

echo Step 1: Cleaning temporary files...
python tools\\cleanup.py
echo.

echo Step 2: Deploying configurations...
python tools\\deploy_config.py
echo.

echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Please restart:
echo   1. Claude Desktop
echo   2. VSCode
echo.
echo Then enjoy coding with AI Power Pack!
echo.
pause
"""
        
        install_bat = package_dir / 'INSTALL.bat'
        with open(install_bat, 'w', encoding='utf-8') as f:
            f.write(batch_script)
        
        print(f"  ✓ INSTALL.bat")
        
        # Python 安装脚本
        python_script = """#!/usr/bin/env python3
import subprocess
import sys

def main():
    print("=" * 60)
    print("AI Power Pack v2.4 - Installation")
    print("=" * 60)
    print()
    
    print("Step 1: Cleaning temporary files...")
    subprocess.run([sys.executable, "tools/cleanup.py"])
    print()
    
    print("Step 2: Deploying configurations...")
    subprocess.run([sys.executable, "tools/deploy_config.py"])
    print()
    
    print("=" * 60)
    print("Installation Complete!")
    print("=" * 60)
    print()
    print("Please restart:")
    print("  1. Claude Desktop")
    print("  2. VSCode")
    print()
    print("Then enjoy coding with AI Power Pack!")

if __name__ == "__main__":
    main()
"""
        
        install_py = package_dir / 'install.py'
        with open(install_py, 'w', encoding='utf-8') as f:
            f.write(python_script)
        
        print(f"  ✓ install.py")
    
    def create_zip_archive(self, package_dir: Path) -> Path:
        """创建 ZIP 压缩包"""
        print("📦 创建 ZIP 压缩包...")
        zip_path = package_dir.parent / f"{package_dir.name}.zip"
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in package_dir.rglob('*'):
                if file.is_file():
                    arcname = file.relative_to(package_dir.parent)
                    zipf.write(file, arcname)
        
        print(f"  ✓ {zip_path.name}")
        return zip_path
    
    def package(self) -> Path:
        """执行完整打包流程"""
        print("=" * 60)
        print("🚀 AI Power Pack 框架打包工具")
        print("=" * 60)
        print()
        
        # 创建包目录
        package_dir = self.create_package_structure()
        print(f"📁 创建打包目录: {package_dir.name}\n")
        
        # 复制各个组件
        self.copy_configs(package_dir)
        self.copy_projects(package_dir)
        self.copy_tools(package_dir)
        self.copy_docs(package_dir)
        self.copy_examples(package_dir)
        self.copy_mcp_servers(package_dir)
        
        # 创建元数据
        self.create_manifest(package_dir)
        self.create_installation_script(package_dir)
        
        # 创建压缩包
        print()
        zip_path = self.create_zip_archive(package_dir)
        
        # 显示结果
        print("\n" + "=" * 60)
        print("✨ 打包完成!")
        print("=" * 60)
        print(f"\n📦 包路径: {package_dir}")
        print(f"📦 压缩包: {zip_path}")
        print(f"📊 包大小: {self._get_size(zip_path)}")
        print("\n💡 分发说明:")
        print("  1. 将 ZIP 文件分发给用户")
        print("  2. 用户解压后运行 INSTALL.bat 或 install.py")
        print("  3. 重启 Claude Desktop 和 VSCode")
        
        return zip_path
    
    def _get_size(self, path: Path) -> str:
        """获取文件大小（可读格式）"""
        size = path.stat().st_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

def main():
    packager = FrameworkPackager()
    packager.package()

if __name__ == "__main__":
    main()
