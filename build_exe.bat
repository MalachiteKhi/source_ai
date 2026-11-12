@echo off
REM Build Source AI Mistral Edition EXE
REM Requires PyInstaller: pip install pyinstaller

echo Building Source AI Mistral Edition EXE...
echo This may take several minutes...

REM Clean previous build
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

REM Build with PyInstaller
pyinstaller --onefile --windowed --name Source_AI_Mistral_Edition --clean mistral_edition.py

if exist dist\Source_AI_Mistral_Edition.exe (
    echo EXE built successfully!
    echo Location: dist\Source_AI_Mistral_Edition.exe
) else (
    echo Error: EXE build failed
)

pause
