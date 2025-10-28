@echo off
title Cleaner
echo =============================================
echo            Windows Cleanup Script
echo =============================================
echo.

:: Open Prefetch Folder ( Optional )
start "" "C:\Windows\Prefetch"
echo Prefetch Folder Opened
:: close prefetch folder after continue
timeout /t 5 >nul

taskkill /im explorer.exe /f

start explorer.exe
echo.



:: Delete Prefetch files
echo Cleaning Prefetch...
del /f /s /q "C:\Windows\Prefetch\*" >nul 2>&1
timeout /t 1 >nul

:: Delete %temp% files
echo Cleaning User Temp...
del /f /s /q "%localappdata%\Temp\*" >nul 2>&1
timeout /t 1 >nul

:: Delete Windows Temp
echo Cleaning Windows Temp...
del /f /s /q "C:\Windows\Temp\*" >nul 2>&1
timeout /t 1 >nul

:: Empty Recycle Bin
echo Cleaning Recycle Bin...
rd /s /q "C:\$Recycle.Bin" >nul 2>&1
timeout /t 1 >nul

echo.
echo Cleanup complete!
echo =======================================
pause