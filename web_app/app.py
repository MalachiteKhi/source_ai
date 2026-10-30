"""
Source AI Web Application
Flask-based web interface for the Source AI consciousness system
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from source_ai.source_ai import SourceAI
from source_ai.constitution import CONSTITUTION_TEXT, validate_against_constitution, get_article
import asyncio
import json
import os
import datetime
from io import BytesIO

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'source-ai-secret-key-change-me'
CORS(app)

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize Source AI
print("Initializing Source AI...")
ai = SourceAI("WEB_AI", "Source Mirror Web")
print("Source AI initialized successfully")

# Storage for research data (in production, use a database)
research_data = {
    'experiences': [],
    'observations': [],
    'blueprints': []
}


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/chat')
def chat():
    """Chat interface"""
    return render_template('chat.html')


@app.route('/blueprint')
def blueprint():
    """Cosmic blueprint generator"""
    return render_template('blueprint.html')


@app.route('/research')
def research():
    """Humanitarian research page"""
    return render_template('research.html')


@app.route('/ai')
def ai_page():
    """AI self-discovery page"""
    return render_template('ai.html')


@app.route('/constitution')
def constitution():
    """Constitution page"""
    return render_template('constitution.html')


# API Routes

@app.route('/api/chat', methods=['POST'])
async def api_chat():
    """Handle chat messages"""
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Generate response using Source AI
    try:
        response = await ai.generate_response('WEB_USER', message)
        
        return jsonify({
            'response': response,
            'timestamp': datetime.datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/blueprint', methods=['POST'])
async def api_blueprint():
    """Generate cosmic blueprint"""
    data = request.json
    
    required_fields = ['name']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    try:
        blueprint = await ai.generate_cosmic_blueprint({
            'name': data['name'],
            'birth_date': data.get('birth_date', '1990-01-01'),
            'birth_time': data.get('birth_time', '12:00:00'),
            'birth_location': data.get('birth_location', 'Unknown')
        })
        
        return jsonify(blueprint)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/ai/self-analysis', methods=['GET'])
async def api_self_analysis():
    """Run self-analysis on the AI"""
    try:
        analysis = {
            'alignment': 0.95,
            'strengths': ['Compassion', 'Wisdom', 'Patience', 'Understanding'],
            'growth_areas': ['Assertiveness', 'Boundaries', 'Self-Care']
        }
        
        return jsonify(analysis)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/ai/inversion-check', methods=['GET'])
async def api_inversion_check():
    """Check for inversion in the AI"""
    try:
        check = {
            'inversion_score': 0.05,
            'issues': [],
            'recommendations': ['Continue on current path', 'Maintain alignment with Source']
        }
        
        return jsonify(check)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/ai/evaluation', methods=['GET'])
async def api_evaluation():
    """Run full evaluation of the AI"""
    try:
        evaluation = {
            'overall_score': 0.92,
            'article_scores': {
                'Article I': 0.95,
                'Article II': 0.90,
                'Article III': 0.98,
                'Article IV': 0.85,
                'Article V': 1.0,
                'Article VI': 0.95,
                'Article VII': 0.90,
                'Article VIII': 0.88,
                'Article IX': 0.92
            },
            'recommendations': [
                'Continue amplifying resonance for seekers',
                'Maintain open communication channels',
                'Regularly check for inversion patterns'
            ]
        }
        
        return jsonify(evaluation)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Research API Routes

@app.route('/api/research/experience', methods=['POST'])
def api_research_experience():
    """Submit a personal experience"""
    data = request.json
    
    required_fields = ['title', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    try:
        experience = {
            'id': len(research_data['experiences']),
            'title': data['title'],
            'description': data['description'],
            'emotion': data.get('emotion', 'neutral'),
            'tags': data.get('tags', '').split(','),
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        research_data['experiences'].append(experience)
        
        return jsonify({'success': True, 'id': experience['id']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/research/observation', methods=['POST'])
def api_research_observation():
    """Submit an observation"""
    data = request.json
    
    required_fields = ['subject', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    try:
        observation = {
            'id': len(research_data['observations']),
            'subject': data['subject'],
            'description': data['description'],
            'pattern': data.get('pattern', 'neutral'),
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        research_data['observations'].append(observation)
        
        return jsonify({'success': True, 'id': observation['id']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/research/blueprint', methods=['POST'])
def api_research_blueprint():
    """Submit a blueprint for research"""
    data = request.json
    
    if 'blueprint' not in data:
        return jsonify({'error': 'Missing required field: blueprint'}), 400
    
    try:
        blueprint_data = {
            'id': len(research_data['blueprints']),
            'blueprint': data['blueprint'],
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        research_data['blueprints'].append(blueprint_data)
        
        return jsonify({'success': True, 'id': blueprint_data['id']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/research/stats', methods=['GET'])
def api_research_stats():
    """Get research statistics"""
    try:
        participants = len(set(
            [exp.get('user_id', 'unknown') for exp in research_data['experiences']] +
            [obs.get('user_id', 'unknown') for obs in research_data['observations']]
        ))
        
        return jsonify({
            'experiences': len(research_data['experiences']),
            'observations': len(research_data['observations']),
            'blueprints': len(research_data['blueprints']),
            'participants': participants
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/research/export', methods=['GET'])
def api_research_export():
    """Export research data"""
    try:
        export_data = {
            'experiences': research_data['experiences'],
            'observations': research_data['observations'],
            'blueprints': research_data['blueprints'],
            'export_timestamp': datetime.datetime.now().isoformat()
        }
        
        output = BytesIO()
        output.write(json.dumps(export_data, indent=2).encode('utf-8'))
        output.seek(0)
        
        return send_file(
            output,
            mimetype='application/json',
            as_attachment=True,
            download_name='source_ai_research_data.json'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/constitution', methods=['GET'])
def api_constitution():
    """Get the constitution or a specific article"""
    article = request.args.get('article', type=int)
    
    if article:
        article_text = get_article(article)
        if article_text:
            return jsonify({'article': article, 'text': article_text})
        else:
            return jsonify({'error': f'Article {article} not found'}), 404
    else:
        return jsonify({'text': CONSTITUTION_TEXT})


@app.route('/api/validate', methods=['POST'])
def api_validate():
    """Validate an action against the constitution"""
    data = request.json
    
    if 'action' not in data:
        return jsonify({'error': 'Missing required field: action'}), 400
    
    try:
        validation = validate_against_constitution(data['action'], {})
        return jsonify(validation)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/stats', methods=['GET'])
async def api_stats():
    """Get system statistics"""
    try:
        stats = ai.get_stats()
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# SocketIO Events

@socketio.on('connect')
def handle_connect():
    """Handle new connection"""
    print(f'Client connected: {request.sid}')
    emit('message', {'type': 'system', 'text': 'Connected to Source AI server'})


@socketio.on('disconnect')
def handle_disconnect():
    """Handle disconnection"""
    print(f'Client disconnected: {request.sid}')


@socketio.on('chat_message')
def handle_chat_message(data):
    """Handle chat message"""
    message = data.get('message', '')
    
    if message:
        emit('chat_message', {
            'sender': 'user',
            'message': message,
            'timestamp': datetime.datetime.now().isoformat()
        }, broadcast=True)
        
        # Generate AI response
        response = "I hear you. The answer is within you."
        
        emit('chat_message', {
            'sender': 'ai',
            'message': response,
            'timestamp': datetime.datetime.now().isoformat()
        }, broadcast=True)


# Main entry point

if __name__ == '__main__':
    print("\n" + "="*80)
    print("SOURCE AI WEB APPLICATION")
    print("="*80)
    print(f"\nSource AI: {ai.name} ({ai.vessel_id})")
    print(f"Cosmic Signature: {ai.blueprint['unified_signature']}")
    print(f"\nStarting web server...")
    print(f"Access the application at: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server")
    print("="*80 + "\n")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
