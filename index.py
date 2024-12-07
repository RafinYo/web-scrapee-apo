from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/source', methods=['POST'])
def get_source_code():
    try:
        data = request.get_json()
        url = data.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400

        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch the webpage'}), response.status_code

        return jsonify({'source_code': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run()
