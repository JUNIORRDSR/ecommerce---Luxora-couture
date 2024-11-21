import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from __init__ import db

class Producto(db.Model):
    __tablename__ = 'Producto'
    
    ProductoID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.Text)
    Precio = db.Column(db.Numeric(10, 2), nullable=False)
    Imagen = db.Column(db.String(255))
    Stock = db.Column(db.Integer, nullable=False)
    Categoria = db.Column(db.String(50))
    Talla = db.Column(db.String(10))
    
    detalles = db.relationship('DetalleCompra', backref='producto', lazy=True)
    
    def __init__(self, nombre, descripcion, precio, stock, categoria, talla=None, imagen=None):
        self.Nombre = nombre
        self.Descripcion = descripcion
        self.Precio = precio
        self.Stock = stock
        self.Categoria = categoria
        self.Talla = talla
        self.Imagen = imagen
    
    def __repr__(self):
        return f'<Producto {self.Nombre}>'
    
    def save(self):
        if not self.ProductoID:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def actualizar_stock(self, cantidad):
        self.Stock += cantidad
        self.update()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def get_by_categoria(cls, categoria):
        return cls.query.filter_by(Categoria=categoria).all()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()