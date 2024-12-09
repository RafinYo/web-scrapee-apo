from flask import Flask, render_template, request, jsonify
import google-ai-generativelanguage as genai

# Initialize Flask app
app = Flask(__name__)

# Replace with your actual Google Cloud Project API key for Generative AI
API_KEY = "AIzaSyDGcFCXeK16YC6tgAVDGZN3Vpkdg4cl5Yo"  # (Store securely using environment variables)
genai.configure(api_key=API_KEY)

@app.route('/', methods=['GET'])
def chat():
    return render_template('index.html')  # Render the HTML template

@app.route('/chat', methods=['POST'])
def chat_post():
    user_input = request.form.get('message')  # Extract message from form data

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate a response using Google's Generative AI
        response = genai.chat(messages=[{'role': 'user', 'content': user_input}])
        
        return jsonify({"response": response.result['text']})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
