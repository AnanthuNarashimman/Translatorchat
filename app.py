from flask import Flask, request, jsonify, send_from_directory
from googletrans import Translator
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  

translator = Translator()

# Serve the HTML file
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

# Serve the JavaScript file
@app.route('/chat.js')
def serve_js():
    return send_from_directory(os.getcwd(), 'chat.js')

# Serve the CSS file 
@app.route('/style.css')
def serve_css():
    return send_from_directory(os.getcwd(), 'style.css')

# Translation route
@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    srclang = data.get('source')
    trglang = data.get('target')

    if text:
        try:
            translated = translator.translate(text, src=srclang, dest=trglang)
            return jsonify({'translated_text': translated.text})
        except Exception as e:
            print(f"Error during translation: {str(e)}")
            return jsonify({'error': 'Translation failed'}), 500
    return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  
