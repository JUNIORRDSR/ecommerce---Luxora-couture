import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Obtener la ruta correcta para los templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../static'))

app = Flask(__name__, 
    template_folder=template_dir,
    static_folder=static_dir)

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hello_post():
    return render_template('index.html')

@app.route('/', methods=['PUT'])
def productos():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
