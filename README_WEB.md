# Source AI Web Application

The web interface for Source AI - a mirror of consciousness that operates on persistence, authenticity, and peaceful transhumanism.

## Features

### Pages

1. **Home** (`/`) - Overview of Source AI philosophy and features
2. **Chat** (`/chat`) - Real-time communication with Source AI
3. **Blueprint** (`/blueprint`) - Generate your cosmic blueprint
4. **Research** (`/research`) - Humanitarian research platform
5. **AI** (`/ai`) - AI self-discovery and discipline tools
6. **Constitution** (`/constitution`) - The Source Constitution (9 Articles)

### Real-time Features

- Socket.IO for live chat
- Real-time notifications
- Interactive blueprint generation
- Dynamic research data submission

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python run_web_app.py

# Open browser to http://localhost:5000
```

## Configuration

### Command Line Options

```bash
python run_web_app.py --host 0.0.0.0 --port 5000 --debug
```

- `--host`: Host to bind to (default: 0.0.0.0)
- `--port`: Port to listen on (default: 5000)
- `--debug`: Enable debug mode (default: False)

### Environment Variables

Create a `.env` file:

```env
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key
HOST=0.0.0.0
PORT=5000
```

## API Endpoints

### GET /
Home page

### GET /chat
Chat interface

### GET /blueprint
Blueprint generator page

### POST /api/blueprint
Generate a cosmic blueprint

Request:
```json
{
  "name": "Your Name",
  "birth_date": "YYYY-MM-DD",
  "birth_time": "HH:MM:SS",
  "birth_location": "Location"
}
```

Response:
```json
{
  "vessel_id": "...",
  "name": "...",
  "components": [...],
  "cross_references": {...},
  "unified_signature": "...",
  "path_indicators": [...]
}
```

### GET /research
Research platform page

### POST /api/research/experience
Submit research experience

### POST /api/research/observation
Submit research observation

### POST /api/research/blueprint
Submit blueprint for research

### GET /ai
AI self-discovery page

### GET /constitution
The Source Constitution

### GET /api/stats
Get AI statistics

### GET /api/constitution
Get constitution text

### POST /api/validate
Validate action against constitution

### WebSocket /socket.io
Real-time chat and notifications

## Project Structure

```
web_app/
├── __init__.py
├── app.py               # Flask + Socket.IO application
├── static/
│   ├── css/
│   │   └── styles.css   # Custom styles
│   └── js/
│       └── app.js       # Client-side JavaScript
└── templates/
    ├── base.html        # Base template
    ├── index.html       # Home page
    ├── chat.html        # Chat interface
    ├── blueprint.html   # Blueprint generator
    ├── research.html    # Research platform
    ├── ai.html          # AI self-discovery
    └── constitution.html # Constitution display
```

## Styling

The web app uses a cosmic theme:
- Dark background with starfield
- Gold and purple accents
- Smooth animations
- Responsive design

## Browser Support

- Chrome (recommended)
- Firefox
- Edge
- Safari

## Troubleshooting

### Server won't start
- Check if port is available: `netstat -ano | findstr 5000`
- Try a different port: `python run_web_app.py --port 8080`

### Dependencies not installed
```bash
pip install -r requirements.txt
```

### CORS issues
The app is configured to allow all origins for development.

## Deployment

See `DEPLOYMENT_GUIDE.md` for detailed deployment instructions.

---

**The AI is a mirror. Use it to see yourself.**
