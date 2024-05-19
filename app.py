# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Assuming you have an HTML file named 'index.html' in the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
