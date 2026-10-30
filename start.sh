#!/bin/bash
# Source AI Web Application Start Script

echo "=========================================="
echo "Source AI Web Application"
echo "=========================================="
echo ""
echo "Starting the web application..."
echo ""

# Install requirements
pip install -r requirements.txt -q

# Run the web application
python run_web_app.py
