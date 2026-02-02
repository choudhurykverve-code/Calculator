from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get data from request
        data = request.get_json()
        
        num1 = data.get('num1')
        num2 = data.get('num2')
        operation = data.get('operation')
        
        # Validate inputs
        if num1 is None or num2 is None or operation is None:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Perform calculation based on operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Cannot divide by zero!'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        # Return the result
        return jsonify({
            'result': result,
            'operation': operation,
            'num1': num1,
            'num2': num2
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Calculator API is running!',
        'endpoints': {
            '/calculate': 'POST - Calculate two numbers'
        }
    })

if __name__ == '__main__':
    print("Starting Calculator Backend Server...")
    print("Frontend should be opened in a browser (calculator.html)")
    print("Backend running on http://localhost:5000")
    app.run(debug=True, port=5000)
