from flask import render_template, request, jsonify
from __init__ import app
from controllers import *
# Rutas para Productos
@app.route('/api/productos', methods=['GET'])
def get_productos():
    return jsonify(ProductoController.get_all())

@app.route('/api/productos/<int:id>', methods=['GET'])
def get_producto(id):
    return jsonify(ProductoController.get_by_id(id))

@app.route('/api/productos', methods=['POST'])
def crear_producto():
    return jsonify(ProductoController.create(request.json))

@app.route('/api/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    return jsonify(ProductoController.update(id, request.json))

@app.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    return jsonify(ProductoController.delete(id))

# Rutas para Usuarios
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(UsuarioController.get_all())

@app.route('/api/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    return jsonify(UsuarioController.get_by_id(id))

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    return jsonify(UsuarioController.create(request.json))

@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    return jsonify(UsuarioController.update(id, request.json))

@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    return jsonify(UsuarioController.delete(id))

# Rutas para Compras
@app.route('/api/compras', methods=['GET'])
def get_compras():
    return jsonify(CompraController.get_all())

@app.route('/api/compras/<int:id>', methods=['GET'])
def get_compra(id):
    return jsonify(CompraController.get_by_id(id))

@app.route('/api/compras', methods=['POST'])
def crear_compra():
    data = request.json
    return jsonify(CompraController.create(data['compra'], data['detalles']))

@app.route('/api/compras/<int:id>', methods=['PUT'])
def actualizar_compra(id):
    return jsonify(CompraController.update(id, request.json))

@app.route('/api/compras/<int:id>', methods=['DELETE'])
def eliminar_compra(id):
    return jsonify(CompraController.delete(id))

# Rutas adicionales
@app.route('/api/usuarios/email/<email>')
def get_usuario_por_email(email):
    return jsonify(UsuarioController.get_by_email(email))

@app.route('/api/usuarios/cedula/<cedula>')
def get_usuario_por_cedula(cedula):
    return jsonify(UsuarioController.get_by_cedula(cedula))

@app.route('/api/compras/usuario/<int:usuario_id>')
def get_compras_por_usuario(usuario_id):
    return jsonify(CompraController.get_by_usuario(usuario_id))

# Rutas de vistas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario')
def usuario():
    return render_template('pages/usuario.html')

@app.route('/login')
def login():
    return render_template('pages/login.html')

