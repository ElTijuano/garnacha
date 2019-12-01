from app import app
from flask import reder_template

@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')
