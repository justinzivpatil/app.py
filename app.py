from flask import Flask, request, jsonify
from urllib.parse import quote as url_quote

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json(silent=True)  # Prevents crashing on bad JSON
    print(f"Received data: {data}")  # Debugging

    if not data:
        return jsonify({'error': 'Invalid or missing JSON'}), 400

    name = data.get('name', 'Guest')
    return jsonify({'message': f'Hello, {name}!'}), 200  # Explicit status

if __name__ == '__main__':
    app.run(debug=True)
