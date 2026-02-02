from flask import Flask, request, jsonify
from flask_cors import CORS
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

@app.route('/integrate', methods=['POST'])
def calculate_integral():
    try:
        # Get data from request
        data = request.get_json()
        
        function_str = data.get('function')
        variable_str = data.get('variable', 'x')
        integration_type = data.get('type', 'indefinite')
        lower_bound_str = data.get('lower_bound')
        upper_bound_str = data.get('upper_bound')
        
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
        transformations = (standard_transformations + (implicit_multiplication_application,))
        
        try:
            expr = parse_expr(function_str, transformations=transformations)
        except Exception as e:
            return jsonify({'error': f'Invalid function syntax: {str(e)}'}), 400
        
        # Calculate the integral based on type
        try:
            if integration_type == 'definite':
                # Parse bounds
                if not lower_bound_str or not upper_bound_str:
                    return jsonify({'error': 'Both lower and upper bounds are required for definite integration'}), 400
                
                try:
                    lower_bound = parse_expr(lower_bound_str, transformations=transformations)
                    upper_bound = parse_expr(upper_bound_str, transformations=transformations)
                except Exception as e:
                    return jsonify({'error': f'Invalid bounds: {str(e)}'}), 400
                
                # Calculate definite integral
                integral = sp.integrate(expr, (var, lower_bound, upper_bound))
                steps = generate_definite_steps(expr, var, lower_bound, upper_bound, integral)
                result_str = str(integral)
                
                # Try to get numerical value if possible
                try:
                    numerical_value = float(integral.evalf())
                    if not sp.oo in [lower_bound, upper_bound]:  # Don't show numerical if bounds are infinity
                        result_str = f"{integral} ≈ {numerical_value:.6f}"
                except:
                    pass
                
            else:
                # Calculate indefinite integral
                integral = sp.integrate(expr, var)
                steps = generate_indefinite_steps(expr, var, integral)
                result_str = str(integral)
                
        except Exception as e:
            return jsonify({'error': f'Error calculating integral: {str(e)}. This function may not have a closed-form integral.'}), 400
        
        # Simplify the integral
        simplified_integral = sp.simplify(integral)
        
        # Return the result
        return jsonify({
            'original': str(expr),
            'result': result_str,
            'simplified': str(simplified_integral),
            'integral_latex': sp.latex(simplified_integral),
            'variable': variable_str,
            'type': integration_type,
            'steps': steps
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


def generate_indefinite_steps(expr, var, integral):
    """Generate step-by-step explanation for indefinite integral"""
    steps = []
    
    # Original function
    steps.append(f"Original function: f({var}) = {expr}")
    
    # Integral notation
    steps.append(f"Finding: ∫({expr}) d{var}")
    
    # Result
    steps.append(f"Integral: {integral} + C")
    
    # Special case explanations
    expr_str = str(expr)
    
    # Check for common patterns and add explanatory steps
    if '**' in str(expr) or '^' in expr_str:
        steps.append("Power rule: ∫x^n dx = x^(n+1)/(n+1) + C (for n ≠ -1)")
    
    if '1/x' in expr_str or 'x**(-1)' in str(expr):
        steps.append("Special case: ∫(1/x) dx = ln|x| + C")
    
    if 'sin' in expr_str:
        steps.append("Note: ∫sin(x) dx = -cos(x) + C")
    
    if 'cos' in expr_str:
        steps.append("Note: ∫cos(x) dx = sin(x) + C")
    
    if 'exp' in expr_str or 'e**' in str(expr):
        steps.append("Note: ∫e^x dx = e^x + C")
    
    steps.append("Remember: C represents the constant of integration")
    
    return steps


def generate_definite_steps(expr, var, lower, upper, integral):
    """Generate step-by-step explanation for definite integral"""
    steps = []
    
    # Original function
    steps.append(f"Original function: f({var}) = {expr}")
    
    # Integral notation with bounds
    steps.append(f"Finding: ∫[{lower} to {upper}] ({expr}) d{var}")
    
    # Indefinite integral first
    indefinite = sp.integrate(expr, var)
    steps.append(f"First, find indefinite integral: F({var}) = {indefinite}")
    
    # Apply fundamental theorem
    steps.append(f"Apply Fundamental Theorem: F({upper}) - F({lower})")
    
    # Result
    steps.append(f"Result: {integral}")
    
    # Try to show numerical approximation
    try:
        numerical = float(integral.evalf())
        if abs(numerical) < 1e10:  # Only show if reasonable number
            steps.append(f"Numerical value: ≈ {numerical:.6f}")
    except:
        pass
    
    return steps


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Integration Calculator API is running!',
        'endpoints': {
            '/integrate': 'POST - Calculate integral of a function'
        },
        'example_indefinite': {
            'function': 'x^2 + 3*x',
            'variable': 'x',
            'type': 'indefinite'
        },
        'example_definite': {
            'function': 'x^2',
            'variable': 'x',
            'type': 'definite',
            'lower_bound': '0',
            'upper_bound': '1'
        }
    })


@app.route('/test', methods=['GET'])
def test():
    """Test endpoint to verify SymPy integration is working"""
    x = sp.Symbol('x')
    expr = x**2 + 3*x
    integral = sp.integrate(expr, x)
    definite_integral = sp.integrate(x**2, (x, 0, 1))
    
    return jsonify({
        'status': 'SymPy integration is working!',
        'test_function': str(expr),
        'test_indefinite_integral': str(integral),
        'test_definite_integral': str(definite_integral)
    })


if __name__ == '__main__':
    print("=" * 60)
    print("Starting Integration Calculator Backend Server...")
    print("=" * 60)
    print("Frontend: Open integration_calculator.html in your browser")
    print("Backend:  Running on http://localhost:5000")
    print("=" * 60)
    print("\nSupported functions:")
    print("  • Polynomials: x^2, x^3, etc.")
    print("  • Trigonometric: sin(x), cos(x), tan(x)")
    print("  • Exponential: e^x, exp(x)")
    print("  • Logarithmic: ln(x), log(x)")
    print("  • Rational: 1/x, 1/(x^2), etc.")
    print("  • Combined: x * sin(x), e^x * cos(x), etc.")
    print("\nIntegration types:")
    print("  • Indefinite: ∫f(x)dx")
    print("  • Definite: ∫[a,b]f(x)dx")
    print("=" * 60)
    app.run(debug=True, port=5000)
