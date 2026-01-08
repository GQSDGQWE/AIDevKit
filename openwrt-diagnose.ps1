# OpenWrt Web 界面诊断脚本
$password = "a1b2c3d4e5@bxm"
$router = "192.168.6.1"

Write-Host "=== OpenWrt 路由器诊断 ===" -ForegroundColor Cyan
Write-Host ""

# 创建 SSH 命令函数
function SSH-Command {
    param($cmd)
    $sshCmd = "C:\Windows\System32\OpenSSH\ssh.exe"
    Write-Host "执行: $cmd" -ForegroundColor Yellow
    echo $password | & $sshCmd -o StrictHostKeyChecking=no root@$router $cmd
    Write-Host ""
}

# 1. 检查 uhttpd 进程
Write-Host "1. 检查 uhttpd 进程..." -ForegroundColor Green
SSH-Command "ps | grep uhttpd | grep -v grep"

# 2. 检查服务状态
Write-Host "2. 检查 uhttpd 服务状态..." -ForegroundColor Green
SSH-Command "/etc/init.d/uhttpd status"

# 3. 尝试启动服务
Write-Host "3. 尝试启动 uhttpd 服务..." -ForegroundColor Green
SSH-Command "/etc/init.d/uhttpd start"

# 4. 再次检查进程
Write-Host "4. 再次检查 uhttpd 进程..." -ForegroundColor Green
SSH-Command "ps | grep uhttpd | grep -v grep"

# 5. 检查端口监听
Write-Host "5. 检查端口监听..." -ForegroundColor Green
SSH-Command "netstat -tuln | grep -E ':(80|443)'"

# 6. 查看日志
Write-Host "6. 查看 uhttpd 相关日志..." -ForegroundColor Green
SSH-Command "logread | grep uhttpd | tail -20"

Write-Host "=== 诊断完成 ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "请尝试在浏览器访问: http://192.168.6.1" -ForegroundColor Yellow
