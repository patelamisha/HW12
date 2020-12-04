"""
    Testing Flask installation
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Stevens!"
    
@app.route('/Goodbye')
def bye():
    return "Thank You,See you later!"

app.run(debug=True)