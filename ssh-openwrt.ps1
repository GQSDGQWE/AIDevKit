# OpenWrt SSH 便捷脚本
# 从 1.md 读取账户密码
$credentials = Get-Content "1.md" | Where-Object { $_ -match '\S' }
$router = $credentials[0] -replace 'root@', ''
$password = $credentials[1]

# SSH 命令函数
function Invoke-OpenWrtSSH {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Command,
        [switch]$ShowPassword
    )
    
    if ($ShowPassword) {
        Write-Host "路由器: root@$router" -ForegroundColor Cyan
        Write-Host "密码: $password" -ForegroundColor Yellow
    }
    
    Write-Host "执行命令: $Command" -ForegroundColor Green
    $result = echo $password | & "C:\Windows\System32\OpenSSH\ssh.exe" -o StrictHostKeyChecking=no root@$router $Command 2>&1
    
    # 过滤掉密码提示
    $result | Where-Object { $_ -notmatch "password:" }
    
    return $LASTEXITCODE
}

# 检查参数
if ($args.Count -eq 0) {
    Write-Host "=== OpenWrt SSH 工具 ===" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "用法: .\ssh-openwrt.ps1 <命令>" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "示例:" -ForegroundColor Green
    Write-Host "  .\ssh-openwrt.ps1 'ps | grep uhttpd'"
    Write-Host "  .\ssh-openwrt.ps1 '/etc/init.d/uhttpd status'"
    Write-Host "  .\ssh-openwrt.ps1 'logread | tail -20'"
    Write-Host ""
    Write-Host "快捷命令:" -ForegroundColor Green
    Write-Host "  .\ssh-openwrt.ps1 status    # 检查 uhttpd 状态"
    Write-Host "  .\ssh-openwrt.ps1 restart   # 重启 uhttpd"
    Write-Host "  .\ssh-openwrt.ps1 log       # 查看日志"
    Write-Host "  .\ssh-openwrt.ps1 check     # 完整诊断"
    exit
}

$cmd = $args[0]

# 快捷命令
switch ($cmd) {
    "status" {
        Write-Host "=== 检查 uhttpd 状态 ===" -ForegroundColor Cyan
        Invoke-OpenWrtSSH "/etc/init.d/uhttpd status"
        Invoke-OpenWrtSSH "ps | grep uhttpd | grep -v grep"
        Invoke-OpenWrtSSH "netstat -tuln | grep -E ':(80|443)'"
    }
    "restart" {
        Write-Host "=== 重启 uhttpd ===" -ForegroundColor Cyan
        Invoke-OpenWrtSSH "/etc/init.d/uhttpd restart"
        Start-Sleep -Seconds 2
        Invoke-OpenWrtSSH "ps | grep uhttpd | grep -v grep"
    }
    "log" {
        Write-Host "=== uhttpd 日志 ===" -ForegroundColor Cyan
        Invoke-OpenWrtSSH "logread | grep uhttpd | tail -20"
    }
    "check" {
        Write-Host "=== 完整诊断 ===" -ForegroundColor Cyan
        Write-Host "`n1. 服务状态:" -ForegroundColor Yellow
        Invoke-OpenWrtSSH "/etc/init.d/uhttpd status"
        
        Write-Host "`n2. 进程检查:" -ForegroundColor Yellow
        Invoke-OpenWrtSSH "ps | grep uhttpd | grep -v grep"
        
        Write-Host "`n3. 端口监听:" -ForegroundColor Yellow
        Invoke-OpenWrtSSH "netstat -tuln | grep -E ':(80|443)'"
        
        Write-Host "`n4. 最近日志:" -ForegroundColor Yellow
        Invoke-OpenWrtSSH "logread | grep uhttpd | tail -10"
        
        Write-Host "`n5. 配置检查:" -ForegroundColor Yellow
        Invoke-OpenWrtSSH "uci show uhttpd.main"
    }
    default {
        Invoke-OpenWrtSSH $cmd
    }
}
