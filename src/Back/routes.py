
from flask import render_template
from __init__ import app

# Crear las rutas de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hello_post():
    return render_template('index.html')

@app.route('/', methods=['PUT'])
def productos():
    return render_template('index.html')

@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    return render_template('pages/usuario.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('pages/login.html')

