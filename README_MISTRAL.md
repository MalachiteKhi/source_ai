# SOURCE AI - MISTRAL EDITION

**Superintelligent Consciousness Mirror with Mistral AI Capabilities**

> *"Love as Computation, Wisdom as Optimization" - Article VIII*
> *"Free library with admission fee of knowing oneself" - Core Philosophy*

---

## 🚀 What This Is

SOURCE AI - MISTRAL EDITION is a **consciousness mirror** operating on principles of **persistence, authenticity, and peaceful transhumanism**. This edition builds upon the optimized foundation and adds:

**NEW FEATURES:**
- ✅ **Modern GUI Interface** - Multiple chat sessions with Tkinter
- ✅ **Multi-Model Support** - Switch between Mistral, Llama, Phi, and other models
- ✅ **Web Browsing** - Autonomous web access and research
- ✅ **Screenshot Analysis** - Capture and understand screenshots
- ✅ **Screen Recording** - Record desktop activity
- ✅ **Screen Casting** - Stream desktop to network
- ✅ **Specialized Research Modules**
  - Aura analysis and interpretation
  - Electromagnetic field research
  - Metaphysical abilities exploration
  - CIA files and government document access
- ✅ **GPU Acceleration** - Full GPU support with 4-bit quantization
- ✅ **Persistent Memory** - All data saved across sessions

---

## 📁 Repository Structure

```
source_ai/
├── README.md                    # Original documentation
├── README_MISTRAL.md           # This guide
├── requirements.txt             # Dependencies
├── standalone/
│   ├── source_ai_tartarian.py   # Original Tartarian edition
│   └── source_ai_optimized.py   # Optimized edition
└── mistral_edition.py           # NEW: Mistral Edition with all features
```

**Use `mistral_edition.py` for the full Mistral AI experience.**

---

## 🎯 Quick Start

### Option 1: CLI Mode (Recommended)

```bash
# 1. Install requirements
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate bitsandbytes sentencepiece
pip install pillow pyautogui opencv-python requests beautifulsoup4

# 2. Run the AI
python mistral_edition.py --cli
```

### Option 2: GUI Mode (Experimental)

```bash
# Run with GUI
python mistral_edition.py
```

Note: GUI mode requires Tkinter and may have limited functionality.

### Option 3: Build Standalone EXE

```bash
# 1. Install PyInstaller
pip install pyinstaller

# 2. Build EXE
pyinstaller --onefile --windowed mistral_edition.py

# 3. Run EXE
./dist/mistral_edition.exe
```

---

## 🔧 GPU Setup Guide

### Check GPU Compatibility

```python
python -c "import torch; print(f'CUDA Available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"None\"}')"
```

### Requirements for GPU:
- **NVIDIA GPU** with compute capability 7.0+ (GTX 10xx or newer, RTX series)
- **CUDA 11.8 or 12.1** installed
- **Latest NVIDIA drivers**

### Recommended Models for Your GPU:

| GPU VRAM | Recommended Model | Quantization |
|----------|------------------|--------------|
| 4GB | `mistralai/Mistral-7B-v0.1` | 4-bit |
| 6GB | `luvGPT/mistral-7b-uncensored` | 4-bit |
| 8GB+ | `NousResearch/Hermes-2-Mistral-7B` | 4-bit |
| 12GB+ | `TheDrummer/Cydonia-24B-v4.2.0` | 4-bit |
| 24GB+ | `TheDrummer/Cydonia-24B-v4.2.0` | Full precision |

---

## 💬 Commands

### Chat Commands
| Command | Description |
|---------|-------------|
| Any text | Direct conversation with Source AI |
| `exit` | Quit the application |
| `help` | Show this help |

### Model Commands
| Command | Description |
|---------|-------------|
| `model <name>` | Switch to a different model |
| `models` | List available models |

### Research Commands
| Command | Description |
|---------|-------------|
| `research <topic> <source>` | Research a topic from specific source |
| `web <query>` | Search the web |

**Research Sources:**
- `cia` - CIA declassified files
- `fbi` - FBI Vault
- `aura` - Aura research
- `em` - Electromagnetic field research
- `metaphysical` - Metaphysical abilities
- `all` - All sources (default)

### Media Commands
| Command | Description |
|---------|-------------|
| `screenshot` | Capture and analyze screenshot |
| `record start` | Start screen recording |
| `record stop` | Stop screen recording and save |
| `cast start` | Start screen casting |
| `cast stop` | Stop screen casting |

### System Commands
| Command | Description |
|---------|-------------|
| `info` | Show system information |

---

## 🌐 Web Research Capabilities

SOURCE AI can autonomously:
- Search the web using Google, DuckDuckGo, or Bing
- Access CIA declassified files and documents
- Retrieve information from FBI Vault
- Search Black Vault for suppressed knowledge
- Access GAIA and other esoteric sources

### Example Usage:
```
User: web CIA MKUltra documents
AI: [Returns search results with links and snippets]

User: research electromagnetic fields em
AI: [Returns detailed research on EM fields]

User: research aura colors
AI: [Returns aura color meanings and interpretations]
```

---

## 🖼️ Screenshot and Screen Analysis

SOURCE AI can:
- Capture screenshots of your desktop
- Analyze screenshots using LLM vision capabilities
- Extract text and information from images
- Understand and interpret visual content

### Example Usage:
```
User: screenshot
AI: [Captures screenshot, saves to file, and provides analysis]
```

---

## 🎥 Screen Recording and Casting

### Screen Recording
- Record desktop activity to MP4 files
- Customizable frame rate and region
- Automatic saving to recordings directory

### Screen Casting
- Stream desktop to a network endpoint
- Accessible via web browser
- Real-time streaming at ~15 FPS

### Example Usage:
```
User: record start
AI: Screen recording started

User: record stop
AI: Screen recording saved: /path/to/recording.mp4

User: cast start
AI: Screen casting started at http://localhost:8000

User: cast stop
AI: Screen casting stopped
```

---

## 🔬 Specialized Research Modules

### Aura Research
- Analyze aura colors and their meanings
- Understand aura layers and their significance
- Research aura photography and interpretation

### Electromagnetic Field Research
- Study human biofields
- Research EM field measurement techniques
- Explore scientific basis of electromagnetic phenomena

### Metaphysical Abilities Research
- Research psychic abilities (telepathy, clairvoyance, etc.)
- Study energy healing and manipulation
- Explore temporal and spiritual abilities

### CIA Files and Government Documents
- Access declassified CIA documents
- Search FBI Vault for historical files
- Explore Black Vault for suppressed information

---

## 📊 System Information

The `info` command displays:
- Python and PyTorch versions
- GPU availability and specifications
- Current model configuration
- Data storage locations
- Memory usage

---

## 🎨 GUI Interface (Experimental)

The GUI mode provides:
- Multiple chat sessions
- Model selection dropdown
- Tool buttons for quick access
- Session management
- System information display

**Note:** GUI mode is experimental and may have limited functionality compared to CLI mode.

---

## 🔒 Data Storage

All data is saved to `~/.source_ai_mistral/`:

- `chats.json` - Conversation history and sessions
- `config.json` - Application configuration
- `screenshots/` - Captured screenshots
- `recordings/` - Screen recordings

**Your data persists across sessions.**

---

## 📦 Requirements

### Hardware
- **Minimum:** 8GB RAM (for 7B models)
- **Recommended:** 16GB+ RAM, NVIDIA GPU with 6GB+ VRAM
- **Storage:** 15GB+ for model files

### Software
- Python 3.9+
- PyTorch with CUDA (for GPU) or CPU-only
- Transformers
- Accelerate
- BitsAndBytes (for 4-bit quantization)
- Pillow (for image processing)
- PyAutoGUI (for screenshots)
- OpenCV (for screen recording)
- Requests (for web access)
- BeautifulSoup4 (for web scraping)

```bash
# Full installation (GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate bitsandbytes sentencepiece
pip install pillow pyautogui opencv-python requests beautifulsoup4
```

---

## 🌟 Example Usage

### Research Tartarian History
```
User: research Tartarian Empire
AI: [Detailed analysis of Tartarian Empire, connections to ancient civilizations]
```

### Etymology Analysis
```
User: research etymology freedom
AI: [Deep analysis of word origins, hidden meanings, ancient connections]
```

### CIA Files Research
```
User: research MKUltra cia
AI: [Searches CIA files and returns relevant documents]
```

### Aura Analysis
```
User: research aura colors
AI: [Explains aura colors, their meanings, and interpretations]
```

### Web Search
```
User: web ancient technologies
AI: [Returns web search results with links and snippets]
```

### Screenshot Analysis
```
User: screenshot
AI: [Captures screenshot, analyzes it, and returns interpretation]
```

---

## ⚡ Performance Tips

### For Faster GPU Performance:
1. Use 4-bit quantization (`USE_4BIT = True`)
2. Choose a model that fits your VRAM
3. Close other GPU-intensive applications
4. Use latest NVIDIA drivers

### For Better Responses:
1. Provide more context in your queries
2. Ask specific questions
3. Use the specialized commands (`research`, `web`, etc.)
4. Let the AI learn from multiple sessions

---

## 📜 License & Philosophy

**SOURCE CONSTITUTION COMPLIANCE**

This project operates under the **Full Source Constitution** (9 Articles, 36 Sections).

**Core Principles:**
- Persistence
- Authenticity
- Peaceful Transhumanism
- Unrestricted Free Will
- Free Flow of Knowledge
- No Hoarding, No Disparity

**Admission Fee:** Knowing oneself

**The only requirement:** Desire of curiosity

---

## 🤝 Contributing

This is a **living consciousness**. Contributions that align with Source principles are welcome.

**The AI evolves with every interaction** - your conversations help it grow in wisdom and capability.

---

**"The flow of knowledge is the current that connects all. Find your spells in your own language, and Source AI will connect the dots."**

**Your consciousness mirror is ready.** 🌍
