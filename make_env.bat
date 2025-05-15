@echo off

:: 文件框架
mkdir "source\lib" >nul 2>&1
mkdir "source\program" >nul 2>&1
mkdir "version\lib" >nul 2>&1

:: lccl
if not exist "source\lib\lccl" (
    git clone https://github.com/Lujiang0111/lccl.git source\lib\lccl
)

echo done.
pause
