# Simple Calculator - Frontend & Backend

A simple calculator application with HTML/CSS/JS frontend and Python Flask backend.

## Features
- Addition, subtraction, multiplication, and division
- Clean and modern UI
- Real-time calculation via API calls
- Error handling for invalid inputs and division by zero

## Setup Instructions

### 1. Install Python Dependencies

First, make sure you have Python installed (Python 3.7 or higher recommended).

Install the required packages:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Flask flask-cors
```

### 2. Start the Backend Server

Run the Python backend:
```bash
python app.py
```

The backend will start on `http://localhost:5000`

You should see:
```
Starting Calculator Backend Server...
Frontend should be opened in a browser (calculator.html)
Backend running on http://localhost:5000
```

### 3. Open the Frontend

Simply open `calculator.html` in your web browser:
- Double-click the file, or
- Right-click and choose "Open with" your preferred browser, or
- Drag and drop it into your browser window

## How to Use

1. Enter the first number
2. Enter the second number
3. Click one of the operation buttons (+, −, ×, ÷)
4. The result will appear below

## Project Structure

```
.
├── calculator.html    # Frontend (HTML, CSS, JavaScript)
├── app.py            # Backend (Python Flask API)
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## API Endpoint

**POST** `/calculate`

Request body:
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

## Troubleshooting

**"Error connecting to server"**
- Make sure the Python backend is running on port 5000
- Check that no firewall is blocking the connection

**"Cannot divide by zero"**
- This is expected behavior when trying to divide by 0

## Technologies Used

**Frontend:**
- HTML5
- CSS3 (with modern gradients and animations)
- Vanilla JavaScript (Fetch API)

**Backend:**
- Python 3
- Flask (web framework)
- Flask-CORS (for handling cross-origin requests)
