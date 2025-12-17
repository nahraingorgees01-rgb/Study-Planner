import os
from flask import Flask, render_template

app = Flask(__name__)

# Route for the Homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for the Planner page (planner.html)
@app.route('/planner')
def planner():
    return render_template('planner.html')

# This part is crucial for Render.com deployment
if __name__ == "__main__":
    # Render provides a PORT environment variable. If it's not there, it uses 5000.
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' allows the app to be accessible on the web
    app.run(host='0.0.0.0', port=port)