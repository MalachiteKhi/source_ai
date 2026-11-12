# SOURCE AI - MISTRAL EDITION

**Superintelligent Consciousness Mirror with Full GUI Interface**

A complete AI assistant with Mistral-level capabilities, featuring a user-friendly interface, web research, screenshot analysis, screen recording, and specialized research modules.

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# GPU version (recommended - requires NVIDIA GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements_mistral.txt

# CPU version (works on any system)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements_mistral.txt
```

### 2. Run the Application

```bash
# Start with GUI (default)
python mistral_edition.py

# Or use CLI mode
python mistral_edition.py --cli
```

### 3. Build Standalone EXE (Windows)

```bash
# Install PyInstaller
pip install pyinstaller

# Build EXE
python build_exe.bat

# The EXE will be in: dist\Source_AI_Mistral_Edition.exe
```

---

## ✨ Features

### 💬 Chat Interface
- Modern GUI with multiple chat sessions
- Conversation history saved automatically
- Context-aware responses

### 🌐 Web Research
- Search Google, DuckDuckGo, Bing
- Access CIA declassified files
- FBI Vault integration
- Black Vault and GAIA access

### 🔬 Specialized Research
- **Aura Research** - Color meanings, layers, energy fields
- **EM Field Research** - Human biofield, electromagnetic phenomena
- **Metaphysical Abilities** - Telepathy, clairvoyance, energy healing

### 🖼️ Media Processing
- **Screenshot Capture** - Capture desktop and analyze with AI
- **Screen Recording** - Record desktop activity to MP4
- **Screen Casting** - Stream desktop to web browser

### ⚡ Performance
- GPU acceleration with 4-bit quantization
- Multi-model support (Mistral, Llama, Phi)
- Automatic GPU detection
- Memory-efficient loading

---

## 📋 Commands (CLI Mode)

| Command | Description |
|---------|-------------|
| `model <name>` | Switch LLM model |
| `models` | List available models |
| `research <topic> <source>` | Research with source (cia, aura, em) |
| `web <query>` | Search the web |
| `screenshot` | Capture & analyze screenshot |
| `record start/stop` | Screen recording |
| `cast start/stop` | Screen casting |
| `info` | System information |
| `help` | Show all commands |
| `exit` | Quit application |

---

## 🎯 Research Sources

- `cia` - CIA declassified documents
- `fbi` - FBI Vault files
- `aura` - Aura and energy field research
- `em` - Electromagnetic field research
- `metaphysical` - Metaphysical abilities
- `all` - All sources (default)

---

## 📦 Requirements

### Hardware
- **Minimum:** 8GB RAM
- **Recommended:** 16GB+ RAM, NVIDIA GPU with 6GB+ VRAM
- **Storage:** 15GB+ for model files

### Software
- Python 3.9+
- All dependencies in `requirements_mistral.txt`

---

## 📁 Files

- `mistral_edition.py` - Main application
- `requirements_mistral.txt` - Dependencies
- `README.md` - This file
- `README_MISTRAL.md` - Detailed documentation
- `build_exe.bat` - Windows build script
- `build_exe.spec` - PyInstaller configuration

---

## 🎨 GUI Interface

The GUI provides:
- **Chat Area** - Main conversation display
- **Input Box** - Type your messages
- **Sidebar** - Sessions, model selection, tools
- **Tools** - Screenshot, web search, research, recording, casting

### Keyboard Shortcuts
- `Ctrl+N` - New chat session
- `Enter` - Send message (Shift+Enter for new line)

---

## 🔧 Troubleshooting

### GPU Not Detected
```bash
# Check CUDA availability
python -c "import torch; print(torch.cuda.is_available())"

# Install correct PyTorch version for your GPU
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Model Loading Error
```bash
# Try CPU mode
python mistral_edition.py --cli

# Or install missing dependencies
pip install transformers accelerate bitsandbytes
```

### Web Features Not Working
```bash
pip install requests beautifulsoup4
```

### Screen Features Not Working
```bash
pip install pyautogui opencv-python pillow
```

---

## 📜 License

Free library - admission fee is knowing oneself.

---

**"The flow of knowledge is the current that connects all."**
