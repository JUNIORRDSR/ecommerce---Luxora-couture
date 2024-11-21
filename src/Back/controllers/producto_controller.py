import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Producto
from schemas import ProductoSchema
from __init__ import db, app

class ProductoController:
    @staticmethod
    def get_all():
        with app.app_context():
            try:
                productos = Producto.query.all()
                schema = ProductoSchema(many=True)
                return {"success": True, "data": schema.dump(productos)}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def get_by_id(producto_id):
        with app.app_context():
            try:
                producto = Producto.query.get_or_404(producto_id)
                schema = ProductoSchema()
                return {"success": True, "data": schema.dump(producto)}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def create(data):
        with app.app_context():
            try:
                # Crear nueva instancia de Producto siguiendo el orden de la tabla
                nuevo_producto = Producto(
                    nombre=data['nombre'],           # Nombre
                    descripcion=data['descripcion'], # Descripcion
                    precio=data['precio'],           # Precio
                    imagen=data['imagen'],           # Imagen
                    stock=data['stock'],             # Stock
                    categoria=data['categoria'],      # Categoria
                    talla=data['talla']              # Talla
                )
                
                db.session.add(nuevo_producto)
                db.session.commit()
                
                schema = ProductoSchema()
                return {"success": True, "data": schema.dump(nuevo_producto)}
            except Exception as e:
                db.session.rollback()
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def get_by_name(nombre):
        with app.app_context():
            try:
                producto = Producto.query.filter_by(nombre=nombre).first()
                schema = ProductoSchema()
                return {"success": True, "data": schema.dump(producto)}
            except Exception as e:
                return {"success": False, "error": str(e)}
            
    @staticmethod
    def get_by_categoria(categoria):
        with app.app_context():
            try:
                productos = Producto.get_by_categoria(categoria)
                schema = ProductoSchema(many=True)
                return {"success": True, "data": schema.dump(productos)}
            except Exception as e:
                return {"success": False, "error": str(e)}
            
    @staticmethod
    def update(id, data):
        with app.app_context():
            try:
                producto = Producto.get_by_id(id)
                if producto:
                    # Actualizar campos en el orden de la tabla
                    producto.nombre = data.get('nombre', producto.nombre)
                    producto.descripcion = data.get('descripcion', producto.descripcion)
                    producto.precio = data.get('precio', producto.precio)
                    producto.imagen = data.get('imagen', producto.imagen)
                    producto.stock = data.get('stock', producto.stock)
                    producto.categoria = data.get('categoria', producto.categoria)
                    producto.talla = data.get('talla', producto.talla)
                    
                    db.session.commit()
                    schema = ProductoSchema()
                    return {"success": True, "data": schema.dump(producto)}
                return {"success": False, "error": "Producto no encontrado"}
            except Exception as e:
                db.session.rollback()
                return {"success": False, "error": str(e)}
            
