# Mathematical Calculators Suite
### Frontend (HTML/CSS/JS) + Backend (Python/Flask)

A collection of web-based mathematical calculators with beautiful UIs and Python backends for symbolic computation.

## 📚 Available Calculators

### 1. Basic Calculator
**File:** `calculator.html` + `app.py`  
**Color Theme:** Purple gradient  
**Features:**
- Addition, subtraction, multiplication, division
- Clean modern interface
- Real-time error handling
- Division by zero protection

### 2. Derivative Calculator
**File:** `derivative_calculator.html` + `derivative_app.py`  
**Color Theme:** Green gradient  
**Features:**
- Symbolic differentiation using SymPy
- Step-by-step solutions
- Supports polynomials, trig, exponential, logarithmic functions
- Custom variable support (x, y, t, etc.)
- Automatic simplification

### 3. Integration Calculator
**File:** `integration_calculator.html` + `integration_app.py`  
**Color Theme:** Pink/Purple gradient  
**Features:**
- Both indefinite (∫f(x)dx) and definite (∫[a,b]f(x)dx) integrals
- Symbolic integration using SymPy
- Step-by-step explanations
- Numerical approximations for definite integrals
- Supports all common mathematical functions

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- A modern web browser

### Installation

1. **Install Python dependencies:**

For all calculators:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
# For basic calculator
pip install Flask flask-cors

# For derivative and integration calculators
pip install Flask flask-cors sympy
```

2. **Run the calculator you want:**

```bash
# Basic Calculator
python app.py

# Derivative Calculator
python derivative_app.py

# Integration Calculator
python integration_app.py
```

3. **Open the corresponding HTML file in your browser:**
   - `calculator.html` for basic calculator
   - `derivative_calculator.html` for derivatives
   - `integration_calculator.html` for integrals


## 🎯 How to Use Each Calculator

### Basic Calculator

1. Enter two numbers
2. Click an operation button (+, −, ×, ÷)
3. View the result instantly

**Example:**
- Input: `10` and `5`
- Operation: `+`
- Result: `15`

---

### Derivative Calculator

1. Enter a function (e.g., `x^2 + 3*x + 5`)
2. Optionally specify the variable (default: `x`)
3. Click "Calculate Derivative"
4. View the derivative with step-by-step explanation

**Examples:**

| Function | Derivative |
|----------|-----------|
| `x^2` | `2*x` |
| `sin(x)` | `cos(x)` |
| `e^x` | `e^x` |
| `ln(x)` | `1/x` |
| `x^2 * sin(x)` | `2*x*sin(x) + x^2*cos(x)` |

**Supported Functions:**
- Polynomials: `x^2`, `x^3`, `5*x^4`
- Trigonometric: `sin(x)`, `cos(x)`, `tan(x)`
- Exponential: `e^x`, `exp(2*x)`
- Logarithmic: `ln(x)`, `log(x)`
- Combined: Any combination of the above

**Input Syntax:**
- Use `^` or `**` for powers: `x^2` or `x**2`
- Multiplication: `2*x` or `2x` (both work)
- Functions: `sin()`, `cos()`, `exp()`, `ln()`

---

### Integration Calculator

1. Enter a function (e.g., `x^2 + 3*x`)
2. Choose integration type:
   - **Indefinite**: ∫f(x)dx (gives antiderivative + C)
   - **Definite**: ∫[a,b]f(x)dx (gives numerical value)
3. For definite integrals, enter lower and upper bounds
4. Click "Calculate Integral"
5. View the result with steps

**Indefinite Integral Examples:**

| Function | Integral |
|----------|----------|
| `x` | `x^2/2 + C` |
| `x^2` | `x^3/3 + C` |
| `sin(x)` | `-cos(x) + C` |
| `1/x` | `ln\|x\| + C` |
| `e^x` | `e^x + C` |

**Definite Integral Examples:**

| Function | Bounds | Result |
|----------|--------|--------|
| `x^2` | [0, 1] | `1/3 ≈ 0.333333` |
| `sin(x)` | [0, π] | `2` |
| `e^x` | [0, 1] | `e - 1 ≈ 1.718282` |

**Supported Functions:**
- All functions supported by derivative calculator
- Rational functions: `1/x`, `1/(x^2)`
- Product of functions: `x*sin(x)`, `e^x*cos(x)`

---

## 🔧 API Documentation

All calculators follow RESTful API design:

### Basic Calculator API

**Endpoint:** `POST /calculate`

Request:
```json
{
  "num1": 10,
  "num2": 5,
  "operation": "add"
}
```

Response:
```json
{
  "result": 15,
  "operation": "add",
  "num1": 10,
  "num2": 5
}
```

Operations: `add`, `subtract`, `multiply`, `divide`

---

### Derivative Calculator API

**Endpoint:** `POST /derivative`

Request:
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

---

### Integration Calculator API

**Endpoint:** `POST /integrate`

**Indefinite Integral Request:**
```json
{
  "function": "x^2",
  "variable": "x",
  "type": "indefinite"
}
```

**Definite Integral Request:**
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
  "variable": "x",
  "type": "definite",
  "steps": [...]
}
```

---

## 🎨 Technology Stack

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern gradients and animations
- **Vanilla JavaScript** - Interactivity and API calls (Fetch API)

### Backend
- **Python 3** - Server-side logic
- **Flask** - Lightweight web framework
- **Flask-CORS** - Cross-origin resource sharing
- **SymPy** - Symbolic mathematics (for derivative and integration)

### Why This Stack?
- ✅ **Separation of concerns** - Frontend and backend are independent
- ✅ **Easy to deploy** - Can deploy frontend and backend separately
- ✅ **Scalable** - Easy to add new features or calculators
- ✅ **Educational** - Great for learning full-stack development
- ✅ **Powerful** - SymPy provides professional-grade symbolic math

---

## 🌿 Git Branch Structure (Recommended)

```
main/
├── calculator.html
├── app.py
└── requirements.txt

derivative-calculator/
├── derivative_calculator.html
├── derivative_app.py
└── derivative_requirements.txt

integration-calculator/
├── integration_calculator.html
├── integration_app.py
└── integration_requirements.txt
```

**Creating branches:**
```bash
# Create derivative calculator branch
git checkout -b derivative-calculator
git add derivative_*
git commit -m "Add derivative calculator"

# Create integration calculator branch
git checkout main
git checkout -b integration-calculator
git add integration_*
git commit -m "Add integration calculator"

# Merge all into main (optional)
git checkout main
git merge derivative-calculator
git merge integration-calculator
```

---

## ⚠️ Troubleshooting

### "Error connecting to server"
- ✓ Ensure Python backend is running (`python app.py`)
- ✓ Check it's running on port 5000
- ✓ Verify no firewall is blocking localhost:5000

### "Module not found" errors
```bash
# Install all dependencies
pip install Flask flask-cors sympy

# Or use requirements files
pip install -r requirements.txt
```

### "Invalid function syntax" (Derivative/Integration)
- ✓ Use `*` for multiplication: `2*x` (though `2x` should work)
- ✓ Balance parentheses: `(x+1)^2`
- ✓ Use correct function names: `sin()`, `cos()`, `ln()`, `exp()`

### Frontend shows old data after changes
- ✓ Hard refresh browser: `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)
- ✓ Clear browser cache

### SymPy calculation takes too long
- Some complex expressions may take time or cannot be integrated symbolically
- Try simplifying the expression first

---

## 📖 Mathematical Background

### Derivative Rules Used
- **Power Rule**: d/dx[x^n] = n·x^(n-1)
- **Product Rule**: d/dx[f·g] = f'·g + f·g'
- **Quotient Rule**: d/dx[f/g] = (f'·g - f·g')/g²
- **Chain Rule**: d/dx[f(g(x))] = f'(g(x))·g'(x)

### Integration Rules Used
- **Power Rule**: ∫x^n dx = x^(n+1)/(n+1) + C
- **Integration by Parts**: ∫u dv = uv - ∫v du
- **Fundamental Theorem**: ∫[a,b] f(x)dx = F(b) - F(a)

---

## 🚀 Future Enhancements

Potential features to add:
- [ ] Limit calculator
- [ ] Partial derivatives
- [ ] Multiple integrals (double, triple)
- [ ] Differential equation solver
- [ ] Graphing capabilities
- [ ] Matrix operations
- [ ] LaTeX rendering for beautiful math display
- [ ] Export results to PDF
- [ ] History/memory of calculations
- [ ] Mobile app version

---

## 📝 Notes

- **Port Configuration**: All backends run on port 5000 by default
  - To run multiple calculators simultaneously, modify the port in the Python files
  
- **CORS**: Enabled by default to allow frontend-backend communication
  
- **Symbolic vs Numerical**: 
  - These calculators provide **symbolic** (exact) results
  - For numerical approximation, use SymPy's `.evalf()` method

- **Browser Compatibility**: 
  - Works on all modern browsers (Chrome, Firefox, Safari, Edge)
  - Requires JavaScript enabled

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Feel free to:
- Add new calculator types
- Improve UI/UX
- Add more mathematical functions
- Enhance error handling
- Add unit tests
- Improve documentation

---

## 👨‍💻 Development Tips

### Running Multiple Calculators Simultaneously

Since all backends use port 5000 by default, to run them together:

1. **Modify ports in Python files:**
```python
# In app.py
app.run(debug=True, port=5000)

# In derivative_app.py
app.run(debug=True, port=5001)

# In integration_app.py
app.run(debug=True, port=5002)
```

2. **Update API URLs in HTML files:**
```javascript
// In calculator.html
const API_URL = 'http://localhost:5000/calculate';

// In derivative_calculator.html
const API_URL = 'http://localhost:5001/derivative';

// In integration_calculator.html
const API_URL = 'http://localhost:5002/integrate';
```

### Testing the API with curl

```bash
# Test basic calculator
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"num1": 10, "num2": 5, "operation": "add"}'

# Test derivative calculator
curl -X POST http://localhost:5001/derivative \
  -H "Content-Type: application/json" \
  -d '{"function": "x^2", "variable": "x"}'

# Test integration calculator
curl -X POST http://localhost:5002/integrate \
  -H "Content-Type: application/json" \
  -d '{"function": "x^2", "variable": "x", "type": "indefinite"}'
```

---

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Check browser console for JavaScript errors
4. Check terminal for Python errors
5. Ensure the backend is running before opening the frontend

---

**Happy Calculating! 🎉**

---

*Created with ❤️ using HTML, CSS, JavaScript, Python, Flask, and SymPy*
