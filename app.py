from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # This allows your frontend to make requests to this server

# Serve static files
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Get the question from the frontend
        data = request.json
        question = data.get('question')

        # Get API key from environment variable
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("API key not found in environment variables")

        # Make the request to OpenAI
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json={
                'model': 'gpt-4o-mini',
                'store': True,
                'messages': [
                    {
                        'role': 'system',
                        'content': 'You are a helpful sports assistant. Answer questions about sports, teams, players, and sports history. Keep your answers concise and informative.'
                    },
                    {
                        'role': 'user',
                        'content': question
                    }
                ]
            }
        )

        # Get the answer from OpenAI's response
        answer = response.json()['choices'][0]['message']['content']
        
        # Send the answer back to the frontend
        return jsonify({'answer': answer})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 