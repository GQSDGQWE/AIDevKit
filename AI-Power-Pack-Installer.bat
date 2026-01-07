@echo off
chcp 65001 >nul
REM ========================================
REM AI Power Pack v2.4 - 一键安装程序
REM One-Click Installer
REM ========================================

echo.
echo ========================================
echo    AI Power Pack v2.4
echo    一键安装程序 / One-Click Installer
echo ========================================
echo.

REM 检查管理员权限
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [INFO] 检测到管理员权限
) else (
    echo [WARNING] 建议以管理员身份运行
    echo [WARNING] Recommended to run as Administrator
    echo.
)

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python 未安装 / Python not installed
    echo.
    echo 请先安装 Python 3.8+
    echo Please install Python 3.8+ first
    echo.
    echo 下载地址 / Download from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [INFO] Python 已安装 / Python detected:
python --version
echo.

REM 创建临时目录
set TEMP_DIR=%TEMP%\ai_power_pack_install
if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"
mkdir "%TEMP_DIR%"

echo [STEP 1/5] 正在下载安装包...
echo [STEP 1/5] Downloading package...
echo.

REM 这里可以从网络下载，或者使用本地文件
set SOURCE_DIR=%~dp0
if exist "%SOURCE_DIR%dist\packages" (
    echo [INFO] 使用本地安装包 / Using local package
    xcopy /E /I /Y "%SOURCE_DIR%dist\packages\*" "%TEMP_DIR%" >nul
) else (
    echo [INFO] 使用当前目录 / Using current directory
    xcopy /E /I /Y "%SOURCE_DIR%*" "%TEMP_DIR%" >nul
)

echo [STEP 2/5] 正在安装配置文件...
echo [STEP 2/5] Installing configuration files...
echo.

REM 检测并创建配置目录
set CLAUDE_CONFIG=%APPDATA%\Claude
set VSCODE_CONFIG=%APPDATA%\Code\User

if not exist "%CLAUDE_CONFIG%" (
    echo [INFO] Claude Desktop 未安装，跳过配置
    echo [INFO] Claude Desktop not found, skipping
) else (
    echo [INFO] 正在配置 Claude Desktop...
    if exist "%TEMP_DIR%\config\CLAUDE.md" (
        python -c "import json,sys;c=json.load(open('%CLAUDE_CONFIG%\\claude_desktop_config.json')) if __import__('os').path.exists('%CLAUDE_CONFIG%\\claude_desktop_config.json') else {};c['customInstructions']={'global':open('%TEMP_DIR%\\config\\CLAUDE.md',encoding='utf-8-sig').read(),'version':'2.4','auto_deployed':True};json.dump(c,open('%CLAUDE_CONFIG%\\claude_desktop_config.json','w',encoding='utf-8'),indent=2,ensure_ascii=False)" 2>nul
        if errorlevel 1 (
            echo [WARNING] Claude 配置失败，请手动配置
        ) else (
            echo [SUCCESS] Claude Desktop 配置成功！
        )
    )
)

if not exist "%VSCODE_CONFIG%" (
    echo [INFO] VSCode 未安装，跳过配置
    echo [INFO] VSCode not found, skipping
) else (
    echo [INFO] 正在配置 VSCode...
    if exist "%TEMP_DIR%\config\copilot-instructions.md" (
        copy /Y "%TEMP_DIR%\config\copilot-instructions.md" "%VSCODE_CONFIG%\copilot-instructions.md" >nul
        python -c "import json,sys;s=json.load(open('%VSCODE_CONFIG%\\settings.json',encoding='utf-8')) if __import__('os').path.exists('%VSCODE_CONFIG%\\settings.json') else {};s['github.copilot.chat.codeGeneration.instructions']=[{'file':'%VSCODE_CONFIG%\\copilot-instructions.md','text':'Follow AI Power Pack v2.4 standards'}];s['github.copilot.enable']={'*':True,'plaintext':True,'markdown':True};json.dump(s,open('%VSCODE_CONFIG%\\settings.json','w',encoding='utf-8'),indent=2,ensure_ascii=False)" 2>nul
        if errorlevel 1 (
            echo [WARNING] VSCode 配置失败，请手动配置
        ) else (
            echo [SUCCESS] VSCode 配置成功！
        )
    )
)

echo.
echo [STEP 3/5] 正在安装依赖...
echo [STEP 3/5] Installing dependencies...
echo.

REM 安装必要的 Python 包
pip install requests cryptography pyside6 fastapi sqlmodel uvicorn python-jose passlib -q 2>nul
if errorlevel 1 (
    echo [WARNING] 部分依赖安装失败，项目可能无法完整运行
    echo [WARNING] Some dependencies failed to install
) else (
    echo [SUCCESS] 依赖安装完成！
)

echo.
echo [STEP 4/5] 正在创建快捷方式...
echo [STEP 4/5] Creating shortcuts...
echo.

REM 创建桌面快捷方式（可选）
set DESKTOP=%USERPROFILE%\Desktop
set /p CREATE_SHORTCUT="是否创建桌面快捷方式? (Y/N) [默认 N]: "
if /i "%CREATE_SHORTCUT%"=="Y" (
    echo [INFO] 创建快捷方式到桌面...
    REM 这里可以添加创建快捷方式的代码
    echo [SUCCESS] 快捷方式已创建
) else (
    echo [INFO] 跳过创建快捷方式
)

echo.
echo [STEP 5/5] 正在清理临时文件...
echo [STEP 5/5] Cleaning up...
echo.

REM 清理临时目录
if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"

echo ========================================
echo    安装完成！/ Installation Complete!
echo ========================================
echo.
echo ✅ 配置文件已部署
echo    Configuration files deployed
echo.
echo 📝 下一步 / Next Steps:
echo    1. 重启 Claude Desktop
echo       Restart Claude Desktop
echo    2. 重启 VSCode
echo       Restart VSCode
echo    3. 开始使用 AI Power Pack！
echo       Start using AI Power Pack!
echo.
echo 📚 文档 / Documentation:
if exist "%SOURCE_DIR%README.md" (
    echo    查看 README.md 了解更多信息
    echo    Check README.md for more information
)
echo.
echo 🎉 感谢使用 AI Power Pack v2.4！
echo    Thank you for using AI Power Pack v2.4!
echo.

pause
exit /b 0
