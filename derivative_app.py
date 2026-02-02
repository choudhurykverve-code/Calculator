from flask import Flask, request, jsonify
from flask_cors import CORS
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

@app.route('/derivative', methods=['POST'])
def calculate_derivative():
    try:
        # Get data from request
        data = request.get_json()
        
        function_str = data.get('function')
        variable_str = data.get('variable', 'x')
        
        # Validate inputs
        if not function_str:
            return jsonify({'error': 'Function is required'}), 400
        
        if not variable_str:
            variable_str = 'x'
        
        # Parse the variable
        try:
            var = sp.Symbol(variable_str)
        except Exception as e:
            return jsonify({'error': f'Invalid variable: {variable_str}'}), 400
        
        # Parse the function with transformations for better parsing
        # This allows input like "2x" instead of requiring "2*x"
        transformations = (standard_transformations + (implicit_multiplication_application,))
        
        try:
            expr = parse_expr(function_str, transformations=transformations)
        except Exception as e:
            return jsonify({'error': f'Invalid function syntax: {str(e)}'}), 400
        
        # Calculate the derivative
        try:
            derivative = sp.diff(expr, var)
        except Exception as e:
            return jsonify({'error': f'Error calculating derivative: {str(e)}'}), 400
        
        # Simplify the derivative
        simplified_derivative = sp.simplify(derivative)
        
        # Generate step-by-step explanation
        steps = generate_steps(expr, var, derivative, simplified_derivative)
        
        # Return the result
        return jsonify({
            'original': str(expr),
            'derivative': str(simplified_derivative),
            'derivative_latex': sp.latex(simplified_derivative),
            'variable': variable_str,
            'steps': steps
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


def generate_steps(expr, var, derivative, simplified):
    """Generate step-by-step explanation of the derivative"""
    steps = []
    
    # Original function
    steps.append(f"Original function: f({var}) = {expr}")
    
    # Derivative notation
    steps.append(f"Finding: d/d{var}[{expr}]")
    
    # Raw derivative
    if str(derivative) != str(simplified):
        steps.append(f"Derivative (before simplification): {derivative}")
        steps.append(f"Simplified: {simplified}")
    else:
        steps.append(f"Derivative: {derivative}")
    
    # Special case explanations
    expr_str = str(expr)
    
    # Check for common patterns and add explanatory steps
    if 'sin' in expr_str or 'cos' in expr_str:
        steps.append("Note: d/dx[sin(x)] = cos(x), d/dx[cos(x)] = -sin(x)")
    
    if 'exp' in expr_str or 'e^' in expr_str:
        steps.append("Note: d/dx[e^x] = e^x")
    
    if 'log' in expr_str or 'ln' in expr_str:
        steps.append("Note: d/dx[ln(x)] = 1/x")
    
    if '**' in str(derivative) or '^' in expr_str:
        steps.append("Power rule applied: d/dx[x^n] = n*x^(n-1)")
    
    return steps


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Derivative Calculator API is running!',
        'endpoints': {
            '/derivative': 'POST - Calculate derivative of a function'
        },
        'example': {
            'function': 'x^2 + 3*x + 5',
            'variable': 'x'
        }
    })


@app.route('/test', methods=['GET'])
def test():
    """Test endpoint to verify SymPy is working"""
    x = sp.Symbol('x')
    expr = x**2 + 3*x + 5
    derivative = sp.diff(expr, x)
    
    return jsonify({
        'status': 'SymPy is working!',
        'test_function': str(expr),
        'test_derivative': str(derivative)
    })


if __name__ == '__main__':
    print("=" * 60)
    print("Starting Derivative Calculator Backend Server...")
    print("=" * 60)
    print("Frontend: Open derivative_calculator.html in your browser")
    print("Backend:  Running on http://localhost:5000")
    print("=" * 60)
    print("\nSupported functions:")
    print("  • Polynomials: x^2, x^3, etc.")
    print("  • Trigonometric: sin(x), cos(x), tan(x)")
    print("  • Exponential: e^x, exp(x)")
    print("  • Logarithmic: ln(x), log(x)")
    print("  • Combined: x^2 * sin(x), e^x / x, etc.")
    print("=" * 60)
    app.run(debug=True, port=5000)
