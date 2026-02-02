# Integration Calculator - Frontend & Backend

A symbolic integration calculator with HTML/CSS/JS frontend and Python Flask backend using SymPy for symbolic mathematics.

## Features
- **Symbolic integration** - Calculates integrals algebraically (exact solutions)
- **Both indefinite and definite integrals**
  - Indefinite: ∫f(x)dx
  - Definite: ∫[a,b]f(x)dx with numerical approximation
- **Step-by-step solutions** - Shows the integration process
- **Multiple function types supported**:
  - Polynomials (x^2, x^3, etc.)
  - Trigonometric functions (sin, cos, tan)
  - Exponential functions (e^x, exp(x))
  - Logarithmic functions (ln(x), log(x))
  - Rational functions (1/x, 1/(x^2), etc.)
  - Combined functions (x * sin(x), e^x * cos(x), etc.)
- **Custom variables** - Use x, y, t, or any variable
- **Automatic simplification** - Results are automatically simplified
- **Beautiful, modern UI** with pink/purple gradient design
- **Error handling** for invalid inputs and non-integrable functions

## Setup Instructions

### 1. Install Python Dependencies

Make sure you have Python installed (Python 3.7 or higher recommended).

Install the required packages:
```bash
pip install -r integration_requirements.txt
```

Or install manually:
```bash
pip install Flask flask-cors sympy
```

### 2. Start the Backend Server

Run the Python backend:
```bash
python integration_app.py
```

The backend will start on `http://localhost:5000`

You should see:
```
============================================================
Starting Integration Calculator Backend Server...
============================================================
Frontend: Open integration_calculator.html in your browser
Backend:  Running on http://localhost:5000
============================================================

Supported functions:
  • Polynomials: x^2, x^3, etc.
  • Trigonometric: sin(x), cos(x), tan(x)
  • Exponential: e^x, exp(x)
  • Logarithmic: ln(x), log(x)
  • Rational: 1/x, 1/(x^2), etc.
  • Combined: x * sin(x), e^x * cos(x), etc.

Integration types:
  • Indefinite: ∫f(x)dx
  • Definite: ∫[a,b]f(x)dx
============================================================
```

### 3. Open the Frontend

Simply open `integration_calculator.html` in your web browser:
- Double-click the file, or
- Right-click and choose "Open with" your preferred browser, or
- Drag and drop it into your browser window

## How to Use

### Indefinite Integrals
1. **Enter a function** (e.g., `x^2 + 3*x`)
2. **Select "Indefinite ∫f(x)dx"**
3. **Click "Calculate Integral"**
4. **View the result** with step-by-step explanation

### Definite Integrals
1. **Enter a function** (e.g., `x^2`)
2. **Select "Definite ∫[a,b]f(x)dx"**
3. **Enter lower and upper bounds** (e.g., 0 and 1)
4. **Click "Calculate Integral"**
5. **View the result** with numerical approximation

## Example Inputs

### Basic Polynomials (Indefinite)
- `x` → `x^2/2 + C`
- `x^2` → `x^3/3 + C`
- `x^3 + 2*x` → `x^4/4 + x^2 + C`
- `5*x^4` → `x^5 + C`

### Trigonometric Functions (Indefinite)
- `sin(x)` → `-cos(x) + C`
- `cos(x)` → `sin(x) + C`
- `tan(x)` → `-ln|cos(x)| + C`
- `sec(x)^2` → `tan(x) + C`

### Exponential Functions (Indefinite)
- `e^x` → `e^x + C`
- `exp(2*x)` → `exp(2*x)/2 + C`
- `2^x` → `2^x/ln(2) + C`

### Logarithmic & Rational Functions (Indefinite)
- `1/x` → `ln|x| + C`
- `ln(x)` → `x*ln(x) - x + C` (integration by parts)
- `1/(x^2)` → `-1/x + C`

### Definite Integrals (Examples)
- `x^2` from 0 to 1 → `1/3 ≈ 0.333333`
- `sin(x)` from 0 to π → `2`
- `e^x` from 0 to 1 → `e - 1 ≈ 1.718282`
- `1/x` from 1 to e → `1`

### Combined Functions
- `x * sin(x)` → `-x*cos(x) + sin(x) + C` (integration by parts)
- `e^x * sin(x)` → `e^x*(sin(x) - cos(x))/2 + C`
- `x * e^x` → `(x - 1)*e^x + C`

## Input Syntax Notes

- Use `^` or `**` for exponents: `x^2` or `x**2`
- Multiplication can be explicit or implicit: `2*x` or `2x` both work
- Use standard function names: `sin()`, `cos()`, `tan()`, `exp()`, `ln()`, `log()`
- Use `e` for Euler's number: `e^x`
- Parentheses for grouping: `(x + 1)^2`
- For definite integrals, bounds can be numbers or expressions: `0`, `1`, `pi`, `e`, `sqrt(2)`, etc.

## Project Structure

```
.
├── integration_calculator.html    # Frontend (HTML, CSS, JavaScript)
├── integration_app.py              # Backend (Python Flask API with SymPy)
├── integration_requirements.txt    # Python dependencies
└── INTEGRATION_README.md           # This file
```

## API Endpoints

### POST `/integrate`

**For Indefinite Integrals:**

Request body:
```json
{
  "function": "x^2 + 3*x",
  "variable": "x",
  "type": "indefinite"
}
```

Response:
```json
{
  "original": "x**2 + 3*x",
  "result": "x**3/3 + 3*x**2/2",
  "simplified": "x**3/3 + 3*x**2/2",
  "integral_latex": "\\frac{x^3}{3} + \\frac{3x^2}{2}",
  "variable": "x",
  "type": "indefinite",
  "steps": [
    "Original function: f(x) = x**2 + 3*x",
    "Finding: ∫(x**2 + 3*x) dx",
    "Integral: x**3/3 + 3*x**2/2 + C",
    "Power rule: ∫x^n dx = x^(n+1)/(n+1) + C (for n ≠ -1)",
    "Remember: C represents the constant of integration"
  ]
}
```

**For Definite Integrals:**

Request body:
```json
{
  "function": "x^2",
  "variable": "x",
  "type": "definite",
  "lower_bound": "0",
  "upper_bound": "1"
}
```

Response:
```json
{
  "original": "x**2",
  "result": "1/3 ≈ 0.333333",
  "simplified": "1/3",
  "integral_latex": "\\frac{1}{3}",
  "variable": "x",
  "type": "definite",
  "steps": [
    "Original function: f(x) = x**2",
    "Finding: ∫[0 to 1] (x**2) dx",
    "First, find indefinite integral: F(x) = x**3/3",
    "Apply Fundamental Theorem: F(1) - F(0)",
    "Result: 1/3",
    "Numerical value: ≈ 0.333333"
  ]
}
```

### GET `/` 
Returns API information

### GET `/test` 
Tests if SymPy integration is working correctly

## Mathematical Background

This calculator uses **symbolic integration**, which finds exact antiderivatives using integration rules:

### Basic Integration Rules
- **Power Rule**: ∫x^n dx = x^(n+1)/(n+1) + C (for n ≠ -1)
- **Constant Multiple**: ∫k·f(x) dx = k·∫f(x) dx
- **Sum Rule**: ∫[f(x) + g(x)] dx = ∫f(x) dx + ∫g(x) dx

### Standard Integrals
- ∫1/x dx = ln|x| + C
- ∫e^x dx = e^x + C
- ∫sin(x) dx = -cos(x) + C
- ∫cos(x) dx = sin(x) + C
- ∫sec²(x) dx = tan(x) + C

### Advanced Techniques
- **Substitution (u-substitution)**
- **Integration by parts**: ∫u dv = uv - ∫v du
- **Partial fractions** for rational functions
- **Trigonometric substitution**

### Fundamental Theorem of Calculus
For definite integrals:
∫[a to b] f(x) dx = F(b) - F(a)

where F is the antiderivative of f.

## Troubleshooting

**"Error connecting to server"**
- Make sure the Python backend is running on port 5000
- Check that no firewall is blocking the connection
- Verify Flask and flask-cors are installed

**"Invalid function syntax"**
- Check your function syntax (use `*` for multiplication if implicit doesn't work)
- Make sure parentheses are balanced
- Use supported function names (sin, cos, ln, exp, etc.)

**"This function may not have a closed-form integral"**
- Some functions cannot be integrated in terms of elementary functions
- Examples: `e^(x^2)`, `sin(x)/x`, `1/ln(x)`
- These would require numerical integration methods (not supported in this calculator)

**"Module 'sympy' not found"**
- Install SymPy: `pip install sympy`

## Limitations

- **No numerical integration** - Only symbolic (exact) integration
- **Some functions don't have closed-form integrals** - e.g., e^(x^2), sin(x)/x
- **Computational complexity** - Very complex expressions may take time or fail
- **Improper integrals** - Integrals with infinite bounds may not always work

## Technologies Used

**Frontend:**
- HTML5
- CSS3 (modern gradients and animations)
- Vanilla JavaScript (Fetch API)

**Backend:**
- Python 3
- Flask (web framework)
- Flask-CORS (cross-origin requests)
- SymPy (symbolic mathematics library)

## Notes

- **Indefinite integrals** always include an implicit constant of integration (+ C)
- **Definite integrals** provide exact values when possible, plus numerical approximations
- Results are **automatically simplified** for readability
- The calculator uses the **Fundamental Theorem of Calculus** for definite integrals
