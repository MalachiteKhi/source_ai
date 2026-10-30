#!/usr/bin/env python3
"""
Source AI Web Application - Main Execution Script

This script runs the complete Source AI web application with:
- Flask web server
- Socket.IO for real-time communication
- Full Source AI integration
- All 9 Articles of the Constitution

Usage:
    python run_web_app.py              # Run with default settings
    python run_web_app.py --host 0.0.0.0 # Run on all interfaces
    python run_web_app.py --port 8080   # Run on custom port
    python run_web_app.py --debug       # Run in debug mode
"""

import sys
import argparse
from web_app.app import app, socketio, ai


def main():
    parser = argparse.ArgumentParser(description='Source AI Web Application')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to listen on')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    
    args = parser.parse_args()
    
    print("\n" + "="*80)
    print("SOURCE AI WEB APPLICATION")
    print("="*80)
    print(f"\nSource AI: {ai.name} ({ai.vessel_id})")
    print(f"Cosmic Signature: {ai.blueprint['unified_signature']}")
    print(f"\nServer Configuration:")
    print(f"   Host: {args.host}")
    print(f"   Port: {args.port}")
    print(f"   Debug: {args.debug}")
    print(f"\nAccess the application at: http://{args.host}:{args.port}")
    print("\nAvailable Pages:")
    print(f"   - Home:        http://{args.host}:{args.port}/")
    print(f"   - Chat:        http://{args.host}:{args.port}/chat")
    print(f"   - Blueprint:   http://{args.host}:{args.port}/blueprint")
    print(f"   - Research:    http://{args.host}:{args.port}/research")
    print(f"   - AI:          http://{args.host}:{args.port}/ai")
    print(f"   - Constitution: http://{args.host}:{args.port}/constitution")
    print("\n" + "="*80)
    print("Starting server... Press Ctrl+C to stop")
    print("="*80 + "\n")
    
    # Run the app
    socketio.run(app, host=args.host, port=args.port, debug=args.debug, allow_unsafe_werkzeug=True)


if __name__ == '__main__':
    main()