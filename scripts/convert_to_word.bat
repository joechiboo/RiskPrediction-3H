@echo off
chcp 65001 > nul
echo ================================================
echo 論文前置頁面 Word 轉換工具
echo ================================================
echo.

echo 檢查 Python 環境...
python --version
if errorlevel 1 (
    echo [錯誤] Python 未安裝或不在 PATH 中
    pause
    exit /b 1
)

echo.
echo 檢查 python-docx 套件...
python -c "import docx; print('python-docx 版本:', docx.__version__)" 2>nul
if errorlevel 1 (
    echo python-docx 未安裝，正在安裝...
    pip install python-docx
    if errorlevel 1 (
        echo [錯誤] 安裝失敗
        echo 請手動執行：pip install python-docx
        pause
        exit /b 1
    )
    echo python-docx 安裝完成！
)

echo.
echo 開始轉換...
echo.
python "%~dp0convert_to_word.py"
if errorlevel 1 (
    echo [錯誤] 轉換過程發生錯誤
    pause
    exit /b 1
)

echo.
echo ================================================
echo 轉換完成！
echo 檔案位置：docs\00_thesis\word\
echo ================================================
pause
