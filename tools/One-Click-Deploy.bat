@echo off
chcp 65001 >nul
:: AI Power Pack - One Click Deploy
:: 自动部署脚本

echo [AI Power Pack] Starting Autonomous Deployment...
echo [AI Power Pack] 正在启动自动部署...
echo.

:: Run the executable in Silent Mode
:: 在静默模式下运行可执行文件
"%~dp0AI-Power-Pack-Ultimate-v2.4.0.exe" -Silent

echo.
echo [SUCCESS] Deployment Complete!
echo [成功] 部署完成！
echo.
echo Press any key to exit...
pause >nul
