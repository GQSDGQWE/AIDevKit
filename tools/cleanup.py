"""
清理临时文件和构建产物
Clean up temporary files and build artifacts
"""
import os
import shutil
import sys
from pathlib import Path

class ProjectCleaner:
    def __init__(self, root_dir: str = None):
        self.root = Path(root_dir) if root_dir else Path(__file__).parent.parent
        self.cleaned_items = []
        self.errors = []
    
    def clean_build_artifacts(self):
        """清理构建产物"""
        patterns = [
            'build',
            'dist',
            '*.spec',
            '__pycache__',
            '*.pyc',
            '*.pyo',
            '*.egg-info',
            '.pytest_cache',
            '.coverage',
            'htmlcov'
        ]
        
        print("🧹 清理构建产物...")
        for pattern in patterns:
            if '*' in pattern:
                # 处理通配符模式
                for item in self.root.rglob(pattern):
                    self._remove_item(item)
            else:
                # 处理目录名
                for item in self.root.rglob(pattern):
                    if item.is_dir():
                        self._remove_item(item)
    
    def clean_databases(self):
        """清理测试数据库"""
        print("🗄️ 清理测试数据库...")
        db_patterns = ['*.db', 'test_*.log']
        for pattern in db_patterns:
            for db_file in self.root.glob(pattern):
                if db_file.name not in ['production.db']:  # 保护生产数据库
                    self._remove_item(db_file)
    
    def clean_temp_files(self):
        """清理临时文件"""
        print("📄 清理临时文件...")
        temp_patterns = [
            '*.tmp',
            '*.temp',
            '*.log',
            '*.bak',
            '*.backup',
            '*~',
            '.DS_Store',
            'Thumbs.db'
        ]
        
        for pattern in temp_patterns:
            for temp_file in self.root.rglob(pattern):
                self._remove_item(temp_file)
    
    def clean_node_modules(self):
        """清理 node_modules（如果存在）"""
        print("📦 清理 node_modules...")
        for node_dir in self.root.rglob('node_modules'):
            if node_dir.is_dir():
                self._remove_item(node_dir)
    
    def clean_venv(self):
        """清理虚拟环境（可选）"""
        print("🐍 检查虚拟环境...")
        venv_names = ['venv', '.venv', 'env', '.env']
        for venv_name in venv_names:
            venv_path = self.root / venv_name
            if venv_path.exists() and venv_path.is_dir():
                response = input(f"发现虚拟环境: {venv_name}, 是否删除? (y/N): ")
                if response.lower() == 'y':
                    self._remove_item(venv_path)
    
    def _remove_item(self, item: Path):
        """安全删除文件或目录"""
        try:
            if item.exists():
                if item.is_file():
                    item.unlink()
                    self.cleaned_items.append(str(item))
                    print(f"  ✓ 删除文件: {item.relative_to(self.root)}")
                elif item.is_dir():
                    shutil.rmtree(item)
                    self.cleaned_items.append(str(item))
                    print(f"  ✓ 删除目录: {item.relative_to(self.root)}")
        except Exception as e:
            error_msg = f"无法删除 {item}: {str(e)}"
            self.errors.append(error_msg)
            print(f"  ✗ {error_msg}")
    
    def clean_all(self, include_venv: bool = False):
        """执行完整清理"""
        print("=" * 60)
        print("🚀 开始清理项目...")
        print("=" * 60)
        
        self.clean_build_artifacts()
        self.clean_databases()
        self.clean_temp_files()
        self.clean_node_modules()
        
        if include_venv:
            self.clean_venv()
        
        print("\n" + "=" * 60)
        print("✨ 清理完成!")
        print("=" * 60)
        print(f"📊 清理统计:")
        print(f"  - 成功删除: {len(self.cleaned_items)} 项")
        print(f"  - 错误: {len(self.errors)} 项")
        
        if self.errors:
            print("\n⚠️ 错误详情:")
            for error in self.errors:
                print(f"  - {error}")
        
        return len(self.errors) == 0

def main():
    import argparse
    parser = argparse.ArgumentParser(description="清理项目临时文件")
    parser.add_argument('--all', action='store_true', help='清理所有内容（包括虚拟环境）')
    parser.add_argument('--path', type=str, help='指定项目路径')
    args = parser.parse_args()
    
    cleaner = ProjectCleaner(args.path)
    success = cleaner.clean_all(include_venv=args.all)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
