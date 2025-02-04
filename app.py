from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    # Parse the incoming JSON data
    data = request.get_json()
    
    # Extract 'name' from the JSON body
    name = data.get('name', 'Guest')
    
    # Return a JSON response
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
