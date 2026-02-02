# Derivative Calculator - Frontend & Backend

A symbolic derivative calculator with HTML/CSS/JS frontend and Python Flask backend using SymPy for symbolic mathematics.

## Features
- **Symbolic differentiation** - Calculates derivatives algebraically, not numerically
- **Step-by-step solutions** - Shows the derivation process
- **Multiple function types supported**:
  - Polynomials (x^2, x^3, etc.)
  - Trigonometric functions (sin, cos, tan)
  - Exponential functions (e^x, exp(x))
  - Logarithmic functions (ln(x), log(x))
  - Combined functions (x^2 * sin(x), e^x / x, etc.)
- **Custom variables** - Use x, y, t, or any variable
- **Automatic simplification** - Results are automatically simplified
- **Beautiful, modern UI** with gradient design
- **Error handling** for invalid inputs

## Setup Instructions

### 1. Install Python Dependencies

Make sure you have Python installed (Python 3.7 or higher recommended).

Install the required packages:
```bash
pip install -r derivative_requirements.txt
```

Or install manually:
```bash
pip install Flask flask-cors sympy
```

### 2. Start the Backend Server

Run the Python backend:
```bash
python derivative_app.py
```

The backend will start on `http://localhost:5000`

You should see:
```
============================================================
Starting Derivative Calculator Backend Server...
============================================================
Frontend: Open derivative_calculator.html in your browser
Backend:  Running on http://localhost:5000
============================================================

Supported functions:
  • Polynomials: x^2, x^3, etc.
  • Trigonometric: sin(x), cos(x), tan(x)
  • Exponential: e^x, exp(x)
  • Logarithmic: ln(x), log(x)
  • Combined: x^2 * sin(x), e^x / x, etc.
============================================================
```

### 3. Open the Frontend

Simply open `derivative_calculator.html` in your web browser:
- Double-click the file, or
- Right-click and choose "Open with" your preferred browser, or
- Drag and drop it into your browser window

## How to Use

1. **Enter a function** in the function input field (e.g., `x^2 + 3*x + 5`)
2. **Optionally specify a variable** (default is `x`, but you can use `y`, `t`, etc.)
3. **Click "Calculate Derivative"**
4. **View the result** with step-by-step explanation

## Example Inputs

### Basic Polynomials
- `x^2` → `2*x`
- `x^3 + 2*x^2 - 5*x + 1` → `3*x^2 + 4*x - 5`
- `5*x^4` → `20*x^3`

### Trigonometric Functions
- `sin(x)` → `cos(x)`
- `cos(x)` → `-sin(x)`
- `tan(x)` → `sec(x)^2` or `1/cos(x)^2`
- `sin(x) + cos(x)` → `cos(x) - sin(x)`

### Exponential Functions
- `e^x` → `e^x`
- `exp(2*x)` → `2*exp(2*x)`
- `x * e^x` → `(x + 1)*e^x` (product rule)

### Logarithmic Functions
- `ln(x)` → `1/x`
- `log(x)` → `1/(x*ln(10))`
- `x * ln(x)` → `ln(x) + 1`

### Combined Functions
- `x^2 * sin(x)` → `2*x*sin(x) + x^2*cos(x)`
- `e^x / x` → `(x*e^x - e^x)/x^2`
- `sin(x^2)` → `2*x*cos(x^2)` (chain rule)

## Input Syntax Notes

- Use `^` or `**` for exponents: `x^2` or `x**2`
- Multiplication can be explicit or implicit: `2*x` or `2x` both work
- Use standard function names: `sin()`, `cos()`, `tan()`, `exp()`, `ln()`, `log()`
- Use `e` for Euler's number: `e^x`
- Parentheses for grouping: `(x + 1)^2`

## Project Structure

```
.
├── derivative_calculator.html    # Frontend (HTML, CSS, JavaScript)
├── derivative_app.py             # Backend (Python Flask API with SymPy)
├── derivative_requirements.txt   # Python dependencies
└── DERIVATIVE_README.md          # This file
```

## API Endpoint

**POST** `/derivative`

Request body:
```json
{
  "function": "x^2 + 3*x + 5",
  "variable": "x"
}
```

Response:
```json
{
  "original": "x**2 + 3*x + 5",
  "derivative": "2*x + 3",
  "derivative_latex": "2x + 3",
  "variable": "x",
  "steps": [
    "Original function: f(x) = x**2 + 3*x + 5",
    "Finding: d/dx[x**2 + 3*x + 5]",
    "Derivative: 2*x + 3",
    "Power rule applied: d/dx[x^n] = n*x^(n-1)"
  ]
}
```

**GET** `/` - API information

**GET** `/test` - Test if SymPy is working correctly

## Troubleshooting

**"Error connecting to server"**
- Make sure the Python backend is running on port 5000
- Check that no firewall is blocking the connection
- Verify Flask and flask-cors are installed

**"Invalid function syntax"**
- Check your function syntax (use `*` for multiplication if implicit doesn't work)
- Make sure parentheses are balanced
- Use supported function names (sin, cos, ln, exp, etc.)

**"Module 'sympy' not found"**
- Install SymPy: `pip install sympy`

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

## Mathematical Background

This calculator uses **symbolic differentiation**, which means it applies calculus rules algebraically rather than computing numerical approximations. It uses the following derivative rules:

- **Power Rule**: d/dx[x^n] = n*x^(n-1)
- **Product Rule**: d/dx[f*g] = f'*g + f*g'
- **Quotient Rule**: d/dx[f/g] = (f'*g - f*g')/g^2
- **Chain Rule**: d/dx[f(g(x))] = f'(g(x))*g'(x)
- **Sum Rule**: d/dx[f + g] = f' + g'

Plus derivatives of standard functions (sin, cos, exp, ln, etc.)
