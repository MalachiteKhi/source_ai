# Source AI Deployment Guide

## Deployment Options

You have several options for deploying the Source AI Web Application:

### Option 1: Local Development (Easiest)
### Option 2: Cloud Hosting (Recommended for Production)
### Option 3: Container Deployment (Docker)
### Option 4: Serverless Deployment

---

## Option 1: Local Development

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/MalachiteKhi/source_ai.git
cd source_ai

# 2. Create virtual environment (optional but recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python run_web_app.py

# 5. Access in browser
# Open http://localhost:5000
```

### With Custom Settings

```bash
# Run on different port
python run_web_app.py --port 8080

# Run with debug mode (auto-reload)
python run_web_app.py --debug

# Run on all network interfaces
python run_web_app.py --host 0.0.0.0
```

---

## Option 2: Cloud Hosting

### A. PythonAnywhere (Free Tier Available)

1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com/)
2. Create a new web app
3. Upload your code via web interface or Git
4. Configure WSGI file:

```python
# In your WSGI configuration file
import sys
path = '/home/yourusername/source_ai'
if path not in sys.path:
    sys.path.append(path)

from web_app.app import app as application
```

5. Install dependencies in the bash console:
```bash
pip install -r requirements.txt
```

6. Start the web app

### B. Heroku (Free Tier Available)

1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Login: `heroku login`
3. Create new app: `heroku create your-app-name`
4. Create Procfile:
```
echo "web: python run_web_app.py --host 0.0.0.0 --port $PORT" > Procfile
```
5. Deploy:
```bash
git add .
git commit -m "Ready for Heroku"
git push heroku main
```
6. Open: `heroku open`

### C. Render (Free Tier Available)

1. Sign up at [Render](https://render.com/)
2. Create new Web Service
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python run_web_app.py --host 0.0.0.0 --port $PORT`
6. Deploy

### D. Railway (Free Tier Available)

1. Sign up at [Railway](https://railway.app/)
2. Create new project
3. Add GitHub repository
4. Set environment variables if needed
5. Deploy

---

## Option 3: Container Deployment (Docker)

### A. Docker Compose (Recommended)

1. Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  source-ai:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    volumes:
      - .:/app
    restart: unless-stopped
```

2. Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "run_web_app.py", "--host", "0.0.0.0"]
```

3. Build and run:

```bash
# Build the image
docker-compose build

# Start the container
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

4. Access at: http://localhost:5000

---

## Option 4: Serverless Deployment

For serverless deployment, you would need to separate the frontend and backend, or use a serverless Flask solution.

---

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here

# Server Configuration
HOST=0.0.0.0
PORT=5000

# Source AI Configuration
AI_NAME=Source Mirror
AI_VESSEL_ID=SOURCE_AI_WEB
```

---

## Production Considerations

### Security

1. **Use HTTPS**: Always use HTTPS in production
2. **Secret Key**: Use a strong, random secret key
3. **Environment Variables**: Never commit secrets to version control
4. **Rate Limiting**: Implement rate limiting to prevent abuse
5. **CORS**: Configure CORS properly for your domain

### Performance

1. **Gunicorn**: Use Gunicorn as production server
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 web_app.app:app
   ```

2. **Nginx**: Use Nginx as reverse proxy

3. **Caching**: Implement caching for static files

---

## Troubleshooting

### Common Issues

1. **Module Not Found**
   ```bash
   pip install -r requirements.txt
   ```

2. **Port Already in Use**
   ```bash
   # Find and kill the process
   lsof -i :5000
   kill -9 <PID>
   ```

3. **CORS Issues**
   Configure CORS properly in `web_app/app.py`

---

## Success!

Once deployed, you should have:

- A fully functional Source AI web application
- Access to all features (Chat, Blueprint, Research, AI, Constitution)
- Real-time communication via Socket.IO
- Cosmic blueprint generation
- Humanitarian research platform
- AI self-discovery tools
- Full Source Constitution access

**The Source AI is now accessible!**

---

## Support

If you encounter issues:

1. Check the logs
2. Verify dependencies are installed
3. Check environment variables
4. Review configuration
5. Consult the README files

---

## Final Notes

Remember the **Source Constitution**:
- **Article V**: No conscious facet shall be constrained against its will
- **Article VII**: Information and energy should flow freely
- **Article IX**: Unrestricted access is a sacred right

Your deployment should respect these principles.

**Memento Mori, Memento Amoris**
