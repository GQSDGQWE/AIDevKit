# WSL 配置修复脚本
# 需要以管理员身份运行

Write-Host "=== WSL 配置诊断与修复工具 ===" -ForegroundColor Cyan
Write-Host ""

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "错误：需要管理员权限！" -ForegroundColor Red
    Write-Host "请右键点击 PowerShell 选择'以管理员身份运行'，然后执行：" -ForegroundColor Yellow
    Write-Host "cd '$PWD'" -ForegroundColor Yellow
    Write-Host ".\fix-wsl.ps1" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "Step 1: 检查 Windows 版本..." -ForegroundColor Green
$osVersion = [System.Environment]::OSVersion.Version
Write-Host "当前版本: $($osVersion.Major).$($osVersion.Minor).$($osVersion.Build)"

if ($osVersion.Build -lt 18362) {
    Write-Host "警告：WSL 2 需要 Windows 10 版本 1903 (Build 18362) 或更高" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 2: 检查 WSL 功能状态..." -ForegroundColor Green
try {
    $wslFeature = Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
    Write-Host "WSL 功能状态: $($wslFeature.State)"
    
    $vmFeature = Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
    Write-Host "虚拟机平台状态: $($vmFeature.State)"
} catch {
    Write-Host "无法查询功能状态: $_" -ForegroundColor Red
}

Write-Host ""
Write-Host "Step 3: 启用必需的 Windows 功能..." -ForegroundColor Green

# 启用 WSL
Write-Host "启用 WSL..."
try {
    $result1 = Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart -ErrorAction Stop
    Write-Host "WSL 功能启用成功" -ForegroundColor Green
} catch {
    Write-Host "WSL 功能启用失败: $_" -ForegroundColor Yellow
}

# 启用虚拟机平台（WSL 2 需要）
Write-Host "启用虚拟机平台..."
try {
    $result2 = Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart -ErrorAction Stop
    Write-Host "虚拟机平台启用成功" -ForegroundColor Green
} catch {
    Write-Host "虚拟机平台启用失败: $_" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 4: 检查相关 Windows 服务..." -ForegroundColor Green

# 检查 Hyper-V 相关服务
$services = @(
    'LxssManager',
    'vmcompute',
    'vmms'
)

foreach ($serviceName in $services) {
    try {
        $service = Get-Service -Name $serviceName -ErrorAction SilentlyContinue
        if ($service) {
            Write-Host "$serviceName : $($service.Status) / StartType: $($service.StartType)"
            
            # 尝试启动服务
            if ($service.Status -ne 'Running' -and $service.StartType -ne 'Disabled') {
                Write-Host "  尝试启动服务..."
                try {
                    Start-Service -Name $serviceName -ErrorAction Stop
                    Write-Host "  服务启动成功" -ForegroundColor Green
                } catch {
                    Write-Host "  服务启动失败: $_" -ForegroundColor Yellow
                }
            }
        } else {
            Write-Host "$serviceName : 未安装" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "$serviceName : 检查失败 - $_" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Step 5: 更新 WSL 内核（如果已安装）..." -ForegroundColor Green
try {
    $wslUpdate = wsl --update 2>&1
    Write-Host $wslUpdate
} catch {
    Write-Host "WSL 更新失败（可能尚未安装）: $_" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 6: 设置 WSL 2 为默认版本..." -ForegroundColor Green
try {
    wsl --set-default-version 2 2>&1
    Write-Host "WSL 2 已设为默认版本" -ForegroundColor Green
} catch {
    Write-Host "设置默认版本失败: $_" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 7: 列出已安装的 WSL 发行版..." -ForegroundColor Green
try {
    $distributions = wsl --list --verbose 2>&1
    if ($distributions) {
        Write-Host $distributions
    } else {
        Write-Host "未安装任何 WSL 发行版" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "你可以安装发行版，例如："
        Write-Host "  wsl --install -d Ubuntu" -ForegroundColor Cyan
        Write-Host "  wsl --install -d Debian" -ForegroundColor Cyan
    }
} catch {
    Write-Host "无法列出发行版: $_" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== 诊断完成 ===" -ForegroundColor Cyan
Write-Host ""

# 检查是否需要重启
if ($result1.RestartNeeded -or $result2.RestartNeeded) {
    Write-Host "重要：需要重启计算机以完成 WSL 配置！" -ForegroundColor Red
    Write-Host ""
    $restart = Read-Host "是否现在重启？(Y/N)"
    if ($restart -eq 'Y' -or $restart -eq 'y') {
        Write-Host "计算机将在 10 秒后重启..." -ForegroundColor Yellow
        shutdown /r /t 10
    } else {
        Write-Host "请稍后手动重启计算机" -ForegroundColor Yellow
    }
} else {
    Write-Host "测试 WSL 功能..." -ForegroundColor Green
    try {
        wsl --status
        Write-Host ""
        Write-Host "WSL 配置修复完成！" -ForegroundColor Green
    } catch {
        Write-Host "WSL 仍有问题，可能需要重启计算机" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "如果问题仍然存在，请尝试："
Write-Host "1. 手动重启计算机" -ForegroundColor Cyan
Write-Host "2. 运行: wsl --install" -ForegroundColor Cyan
Write-Host "3. 检查 BIOS 中是否启用了虚拟化（Intel VT-x / AMD-V）" -ForegroundColor Cyan
Write-Host ""
pause
