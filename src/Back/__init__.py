import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI  

# Obtener la ruta correcta para los templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../static'))

# Crear la aplicación Flask
app = Flask(__name__, 
    template_folder=template_dir,
    static_folder=static_dir)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from routes import *

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
