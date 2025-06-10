@echo off
setlocal enabledelayedexpansion

:: 设置命令行编码为UTF-8
chcp 65001 >nul
cls

:: 固定设置 - 根据您的需求修改这两个值
set REPO_URL=https://github.com/baimianxiao/PtilopsisOvoPlugin.git
set TARGET_DIR=%CD%/test

echo 正在准备拉取仓库...
echo 仓库URL: %REPO_URL%
echo 目标目录: %TARGET_DIR%
echo.

:: 获取当前脚本文件名（用于排除检查）
set "SCRIPT_NAME=%~nx0"

:: 检查目标目录是否就是脚本所在目录
cd /d "%TARGET_DIR%" 2>nul || (
    echo 错误：无法进入目录
    goto :pause_exit
)

:: 判断是否Git仓库
if exist ".git\" (
    echo 正在更新已有仓库...
    git pull
    if errorlevel 1 (
        echo 错误：拉取更新失败
        goto :pause_exit
    )
    echo 更新成功！
    goto :pause_exit
)

:: 检查目录是否为空（排除脚本本身）
set EMPTY_DIR=true
for /f "delims=" %%i in ('dir /b /a 2^>nul') do (
    if /i not "%%i"=="%SCRIPT_NAME%" (
        set EMPTY_DIR=false
        goto :check_empty
    )
)

:check_empty
if "!EMPTY_DIR!"=="true" (
    echo 正在克隆仓库...
    git clone "%REPO_URL%" .
    if errorlevel 1 (
        echo 错误：克隆仓库失败
        goto :pause_exit
    )
    echo 克隆成功！
    goto :pause_exit
)

:: 非空非Git目录处理
echo 错误：目标目录非空且不是Git仓库
echo 目录内容（排除脚本本身）:
dir /b | findstr /v /i "%SCRIPT_NAME%"
echo.
echo 请清理目录后再运行此脚本

:pause_exit
echo.
echo 操作完成，按回车键退出...
pause >nul
endlocal