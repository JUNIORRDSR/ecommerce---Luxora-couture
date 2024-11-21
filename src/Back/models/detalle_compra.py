import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from __init__ import db

class DetalleCompra(db.Model):
    __tablename__ = 'DetalleCompra'
    
    DetalleCompraID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CompraID = db.Column(db.Integer, db.ForeignKey('Compra.CompraID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    ProductoID = db.Column(db.Integer, db.ForeignKey('Producto.ProductoID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    Cantidad = db.Column(db.Integer, nullable=False)
    PrecioUnitario = db.Column(db.Numeric(10, 2), nullable=False)
    
    def __init__(self, CompraID, ProductoID, Cantidad, PrecioUnitario):
        self.CompraID = CompraID
        self.ProductoID = ProductoID
        self.Cantidad = Cantidad
        self.PrecioUnitario = PrecioUnitario
    
    def __repr__(self):
        return f'<DetalleCompra {self.DetalleCompraID}>'
    
    def save(self):
        if not self.DetalleCompraID:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def get_by_compra(cls, compra_id):
        return cls.query.filter_by(CompraID=compra_id).all()
    
    @classmethod
    def get_by_producto(cls, producto_id):
        return cls.query.filter_by(ProductoID=producto_id).all()