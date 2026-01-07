"""
自动检测并配置 Claude Desktop 和 VSCode 的规则文件
Auto-detect and configure rules for Claude Desktop and VSCode
"""
import os
import json
import shutil
from pathlib import Path
from typing import Dict, Optional, List

class ConfigDeployer:
    def __init__(self):
        self.home = Path.home()
        self.project_root = Path(__file__).parent.parent
        self.results = {
            'claude': {'detected': False, 'configured': False, 'path': None},
            'vscode': {'detected': False, 'configured': False, 'path': None}
        }
    
    def detect_claude(self) -> Optional[Path]:
        """检测 Claude Desktop 配置目录"""
        possible_paths = [
            self.home / 'AppData' / 'Roaming' / 'Claude',
            self.home / '.config' / 'Claude',
            Path('C:/Users') / os.getenv('USERNAME', '') / 'AppData' / 'Roaming' / 'Claude'
        ]
        
        for path in possible_paths:
            if path.exists():
                print(f"✓ 找到 Claude Desktop 配置: {path}")
                return path
        
        print("○ 未检测到 Claude Desktop（跳过配置）")
        return None
    
    def detect_vscode(self) -> Optional[Path]:
        """检测 VSCode 配置目录"""
        possible_paths = [
            self.home / 'AppData' / 'Roaming' / 'Code' / 'User',
            self.home / '.config' / 'Code' / 'User',
            self.home / 'Library' / 'Application Support' / 'Code' / 'User'
        ]
        
        for path in possible_paths:
            if path.exists():
                print(f"✓ 找到 VSCode 配置: {path}")
                return path
        
        print("○ 未检测到 VSCode（跳过配置）")
        return None
    
    def configure_claude(self, claude_path: Path) -> bool:
        """配置 Claude Desktop 的自定义指令"""
        try:
            config_file = claude_path / 'claude_desktop_config.json'
            source_file = self.project_root / 'config' / 'CLAUDE.md'
            
            if not source_file.exists():
                print(f"✗ 源文件不存在: {source_file}")
                return False
            
            # 读取现有配置（如果存在）
            if config_file.exists():
                with open(config_file, 'r', encoding='utf-8-sig') as f:
                    try:
                        config = json.load(f)
                        print("  → 找到现有配置，将更新")
                    except json.JSONDecodeError:
                        config = {}
                        print("  → 现有配置格式错误，创建新配置")
            else:
                config = {}
                print("  → 创建新配置")
            
            # 读取规则文件内容（处理 BOM）
            with open(source_file, 'r', encoding='utf-8-sig') as f:
                rules_content = f.read()
            
            # 更新配置
            if 'customInstructions' not in config:
                config['customInstructions'] = {}
            
            config['customInstructions']['global'] = rules_content
            config['customInstructions']['source'] = str(source_file)
            config['customInstructions']['version'] = '2.4'
            config['customInstructions']['auto_deployed'] = True
            
            # 写入配置（不带 BOM）
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Claude 配置成功写入: {config_file}")
            return True
            
        except Exception as e:
            print(f"✗ 配置 Claude 失败: {str(e)}")
            return False
    
    def configure_vscode(self, vscode_path: Path) -> bool:
        """配置 VSCode 的 Copilot 指令"""
        try:
            # VSCode 设置文件
            settings_file = vscode_path / 'settings.json'
            source_file = self.project_root / 'config' / 'copilot-instructions.md'
            
            if not source_file.exists():
                print(f"✗ 源文件不存在: {source_file}")
                return False
            
            # 读取现有设置
            if settings_file.exists():
                with open(settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                print("  → 找到现有设置，将更新")
            else:
                settings = {}
                print("  → 创建新设置")
            
            # 复制指令文件到 VSCode 配置目录
            copilot_instructions_dest = vscode_path / 'copilot-instructions.md'
            shutil.copy2(source_file, copilot_instructions_dest)
            print(f"  → 复制指令文件到: {copilot_instructions_dest}")
            
            # 更新设置
            settings['github.copilot.chat.codeGeneration.instructions'] = [
                {
                    "file": str(copilot_instructions_dest),
                    "text": "Follow AI Power Pack v2.4 standards"
                }
            ]
            
            # 启用其他 Copilot 设置
            settings.update({
                'github.copilot.enable': {
                    '*': True,
                    'plaintext': True,
                    'markdown': True,
                    'scminput': False
                },
                'github.copilot.advanced': {
                    'debug.overrideEngine': 'claude-sonnet-4.5',
                    'inlineSuggestCount': 3
                }
            })
            
            # 写入设置
            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
            
            print(f"✓ VSCode 配置成功写入: {settings_file}")
            return True
            
        except Exception as e:
            print(f"✗ 配置 VSCode 失败: {str(e)}")
            return False
    
    def deploy_all(self) -> Dict:
        """执行完整部署"""
        print("=" * 60)
        print("🚀 AI Power Pack 配置部署工具 v2.4")
        print("=" * 60)
        
        # 检测 Claude Desktop
        print("\n📦 检测 Claude Desktop...")
        claude_path = self.detect_claude()
        if claude_path:
            self.results['claude']['detected'] = True
            self.results['claude']['path'] = str(claude_path)
            print("  → 开始配置 Claude...")
            self.results['claude']['configured'] = self.configure_claude(claude_path)
        
        # 检测 VSCode
        print("\n📦 检测 VSCode...")
        vscode_path = self.detect_vscode()
        if vscode_path:
            self.results['vscode']['detected'] = True
            self.results['vscode']['path'] = str(vscode_path)
            print("  → 开始配置 VSCode...")
            self.results['vscode']['configured'] = self.configure_vscode(vscode_path)
        
        # 显示结果
        print("\n" + "=" * 60)
        print("✨ 配置部署完成!")
        print("=" * 60)
        self._print_summary()
        
        return self.results
    
    def _print_summary(self):
        """打印部署摘要"""
        print("\n📊 部署摘要:")
        
        # Claude Desktop
        claude = self.results['claude']
        print(f"\n  Claude Desktop:")
        print(f"    检测状态: {'✓ 已安装' if claude['detected'] else '○ 未检测到'}")
        if claude['detected']:
            print(f"    配置路径: {claude['path']}")
            print(f"    配置状态: {'✓ 成功' if claude['configured'] else '✗ 失败'}")
        
        # VSCode
        vscode = self.results['vscode']
        print(f"\n  VSCode:")
        print(f"    检测状态: {'✓ 已安装' if vscode['detected'] else '○ 未检测到'}")
        if vscode['detected']:
            print(f"    配置路径: {vscode['path']}")
            print(f"    配置状态: {'✓ 成功' if vscode['configured'] else '✗ 失败'}")
        
        # 建议
        print("\n💡 下一步:")
        if claude['configured']:
            print("  1. 重启 Claude Desktop 以加载新配置")
        if vscode['configured']:
            print("  2. 重启 VSCode 以加载新的 Copilot 指令")
        
        if not claude['detected'] and not vscode['detected']:
            print("  ⚠️  未检测到 Claude Desktop 或 VSCode")
            print("  → 安装后可重新运行此工具进行配置")

def main():
    deployer = ConfigDeployer()
    results = deployer.deploy_all()
    
    # 返回状态码
    any_configured = any(r['configured'] for r in results.values())
    return 0 if any_configured else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
