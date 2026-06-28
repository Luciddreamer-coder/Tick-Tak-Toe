# ❌⭕ Tic Tac Toe - Flask Web App

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-black?logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

> **A sleek, dark-themed Tic Tac Toe game built entirely with Flask (Python), HTML, and CSS - No JavaScript required!**


## ✨ Features

- 🎮 **Classic 3x3 Gameplay** - Traditional Tic Tac Toe rules
- 🎨 **Modern Dark Theme** - Eye-friendly dark interface with vibrant colors
- 🔴 **Color-Coded Players** - X in coral red, O in bright blue
- 🏆 **Instant Win Detection** - Server-side validation highlights winning combinations
- 📱 **Responsive Design** - Works perfectly on all screen sizes
- 🔄 **One-Click Reset** - Quick "Reset Game" button to start over
- 💬 **Live Status Updates** - Real-time match status display
- 🚫 **Zero JavaScript** - Pure Python/Flask backend with HTML/CSS frontend

## 🛠️ Tech Stack

**Backend:**
- Python 3.10+
- Flask 2.3+
- Jinja2 Templating
- `os` module

**Frontend:**
- HTML5
- CSS3 (Custom styling with Flexbox/Grid)
- **No JavaScript** - All logic handled server-side!

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

## 🚀 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/[your-username]/[your-repo-name].git
cd [your-repo-name]

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Set the Flask app
export FLASK_APP=app.py          # macOS/Linux
# or
set FLASK_APP=app.py             # Windows

# Run the server
flask run

5. Open in browser:
Navigate to http://127.0.0.1:5000
🎮 How to Play
Player X goes first (marked in 🔴 coral red)
Click any empty cell to place your mark
Players alternate turns (X → O → X...)
Player O is marked in 🔵 bright blue
Get 3 in a row (horizontal, vertical, or diagonal) to win!
If all cells are filled with no winner, it's a draw
Click "Reset Game" to start a new match

Project Structure
tic-tac-toe/
├── app.py                 # Flask backend & game logic
├── requirements.txt       # Python dependencies
├── static/
│   └── css/
│       └── style.css      # Dark theme styling
├── templates/
│   └── index.html         # Main game interface
└── README.md

🎨 Design Features
Dark Background - Reduces eye strain during extended play
Coral Red (X) - Vibrant color for Player X
Bright Blue (O) - Eye-catching color for Player O
Green Win Message - Clear success indicator
Yellow Reset Button - Prominent call-to-action
Smooth Hover Effects - Enhanced user experience with CSS only
🔧 How It Works (No JavaScript!)
All game logic is handled server-side with Flask:
Form Submissions - Each cell click submits a form to the server
Session Management - Game state stored in Flask session
Win Detection - Python checks all 8 winning combinations
Page Reloads - Server re-renders the board with updated state
CSS Styling - All visual effects and layout handled by CSS
📄 License
MIT License - feel free to use this project for learning or personal use!
Author - Peeyush
GitHub: Luciddreamer-coder
