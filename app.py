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
    # Get the port from the environment (Render needs this)
    # Default to 5001 to avoid the Mac AirPlay conflict
    port = int(os.environ.get("PORT", 5006))
    
    # Run the app on 0.0.0.0 so it's accessible to the web
    app.run(host='0.0.0.0', port=port, debug=True)