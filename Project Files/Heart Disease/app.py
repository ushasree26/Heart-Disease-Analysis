from flask import Flask, render_template

app = Flask(__name__)

# Landing Page
@app.route('/')
def index():
    return render_template('index.html')

# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Story Page
@app.route('/story')
def story():
    return render_template('story.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)