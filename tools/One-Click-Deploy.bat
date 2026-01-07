@echo off
chcp 65001 >nul
REM ========================================
REM AI Power Pack v2.4 - One-Click Deploy
REM ========================================

echo.
echo ========================================
echo    AI Power Pack v2.4
echo    One-Click Deploy Tool
echo ========================================
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo [错误] Python 未安装或不在 PATH 中
    echo Please install Python 3.8 or higher
    echo 请安装 Python 3.8 或更高版本
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [INFO] Python detected: 
python --version
echo.

REM 显示菜单
:MENU
echo ========================================
echo Select an option:
echo 选择一个选项:
echo ========================================
echo 1. Full Deploy (Clean + Package + Configure)
echo    完整部署（清理 + 打包 + 配置）
echo.
echo 2. Clean Only (Remove temporary files)
echo    仅清理（删除临时文件）
echo.
echo 3. Package Only (Create distribution package)
echo    仅打包（创建分发包）
echo.
echo 4. Configure Only (Deploy to Claude/VSCode)
echo    仅配置（部署到 Claude/VSCode）
echo.
echo 5. Exit
echo    退出
echo ========================================
echo.

set /p choice="Enter your choice (1-5) 输入选择: "

if "%choice%"=="1" goto FULL_DEPLOY
if "%choice%"=="2" goto CLEAN_ONLY
if "%choice%"=="3" goto PACKAGE_ONLY
if "%choice%"=="4" goto CONFIGURE_ONLY
if "%choice%"=="5" goto EXIT
goto MENU

:FULL_DEPLOY
echo.
echo ========================================
echo Starting Full Deployment...
echo 开始完整部署...
echo ========================================
echo.

echo [STEP 1/3] Cleaning temporary files...
echo [步骤 1/3] 清理临时文件...
python tools\cleanup.py
if errorlevel 1 (
    echo [WARNING] Cleanup completed with warnings
    echo [警告] 清理完成但有警告
)
echo.

echo [STEP 2/3] Creating distribution package...
echo [步骤 2/3] 创建分发包...
python tools\package_framework.py
if errorlevel 1 (
    echo [ERROR] Package creation failed
    echo [错误] 创建包失败
    pause
    exit /b 1
)
echo.

echo [STEP 3/3] Deploying configurations...
echo [步骤 3/3] 部署配置...
python tools\deploy_config.py
if errorlevel 1 (
    echo [WARNING] Configuration deployment completed with warnings
    echo [警告] 配置部署完成但有警告
)
echo.

goto SUCCESS

:CLEAN_ONLY
echo.
echo ========================================
echo Cleaning temporary files...
echo 清理临时文件...
echo ========================================
echo.
python tools\cleanup.py
echo.
goto MENU

:PACKAGE_ONLY
echo.
echo ========================================
echo Creating distribution package...
echo 创建分发包...
echo ========================================
echo.
python tools\package_framework.py
echo.
goto MENU

:CONFIGURE_ONLY
echo.
echo ========================================
echo Deploying configurations...
echo 部署配置...
echo ========================================
echo.
python tools\deploy_config.py
echo.
goto MENU

:SUCCESS
echo.
echo ========================================
echo    Deployment Complete!
echo    部署完成！
echo ========================================
echo.
echo Next Steps 下一步:
echo   1. Restart Claude Desktop
echo      重启 Claude Desktop
echo   2. Restart VSCode
echo      重启 VSCode
echo   3. Check dist/packages for distribution files
echo      检查 dist/packages 目录中的分发文件
echo.
echo Thank you for using AI Power Pack v2.4!
echo 感谢使用 AI Power Pack v2.4！
echo.
pause
exit /b 0

:EXIT
echo.
echo Goodbye! 再见!
exit /b 0
