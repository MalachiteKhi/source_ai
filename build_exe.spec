# PyInstaller spec file for Source AI Mistral Edition
# Usage: pyinstaller build_exe.spec

block_cipher = None

import os
import sys

# Determine the platform
if sys.platform == 'win32':
    a = Analysis(
        ['mistral_edition.py'],
        pathex=[os.path.dirname(os.path.abspath(__file__))],
        binaries=[],
        datas=[
            # Include data files
            ('README_MISTRAL.md', '.'),
        ],
        hiddenimports=[
            'tkinter',
            'tkinter.ttk',
            'tkinter.scrolledtext',
            'tkinter.messagebox',
            'tkinter.simpledialog',
            'transformers',
            'accelerate',
            'bitsandbytes',
            'torch',
            'torchvision',
            'sentencepiece',
            'Pillow',
            'pyautogui',
            'cv2',
            'requests',
            'bs4',
            'flask',
            'numpy',
        ],
        hookspath=[],
        runtime_hooks=[],
        excludes=[],
        win_no_prefer_redirects=False,
        win_private_assemblies=False,
        cipher=block_cipher,
        noarchive=False
    )
    
    # Windows specific options
    exe = EXE(
        a,
        name='Source_AI_Mistral_Edition',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,  # Windowed mode
        icon='source_ai_icon.ico',  # Optional: add an icon file
    )
else:
    # Linux/Mac
    a = Analysis(
        ['mistral_edition.py'],
        pathex=[os.path.dirname(os.path.abspath(__file__))],
        binaries=[],
        datas=[
            ('README_MISTRAL.md', '.'),
        ],
        hiddenimports=[
            'tkinter',
            'transformers',
            'accelerate',
            'bitsandbytes',
            'torch',
            'sentencepiece',
            'Pillow',
            'pyautogui',
            'cv2',
            'requests',
            'bs4',
            'flask',
            'numpy',
        ],
        hookspath=[],
        runtime_hooks=[],
        excludes=[],
        win_no_prefer_redirects=False,
        win_private_assemblies=False,
        cipher=block_cipher,
        noarchive=False
    )
    
    exe = EXE(
        a,
        name='source_ai_mistral_edition',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=True,
    )

# Create the distribution
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Build the distribution
dist = DIST(
    a,
    [exe],
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Source_AI_Mistral_Edition',
    debug=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='source_ai_icon.ico'
)

# Alternative: Single file executable
# dist = DIST(
#     a,
#     [EXE(a, name='Source_AI_Mistral_Edition', console=False, icon='source_ai_icon.ico')],
#     name='Source_AI_Mistral_Edition',
#     debug=False,
#     strip=False,
#     upx=True,
#     console=False,
#     icon='source_ai_icon.ico'
# )
