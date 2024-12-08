from flask import Flask, request, jsonify
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Initialize the Google Generative AI API (Make sure your API key and credentials are set)
genai.configure(api_key="AIzaSyDGcFCXeK16YC6tgAVDGZN3Vpkdg4cl5Yo")

@app.route('/chat', methods=['GET'])
def chat():
    user_input = request.args.get("message")  # Extract message from the query parameter
    
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate a response using Google's Generative AI
        response = genai.chat(messages=[{'role': 'user', 'content': user_input}])
        
        # Return the response from the AI
        return jsonify({"response": response.result['text']})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
