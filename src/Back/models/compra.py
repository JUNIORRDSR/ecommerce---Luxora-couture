import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from __init__ import db
from datetime import datetime

class Compra(db.Model):
    __tablename__ = 'Compra'
    
    CompraID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UsuarioID = db.Column(db.Integer, db.ForeignKey('Usuario.UsuarioID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    FechaCompra = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    MetodoPago = db.Column(db.String(50), nullable=False)
    Total = db.Column(db.Numeric(10, 2), nullable=False)
    
    detalles = db.relationship('DetalleCompra', backref='compra', lazy=True)
    
    def __init__(self, UsuarioID, MetodoPago, Total):
        self.UsuarioID = UsuarioID
        self.MetodoPago = MetodoPago
        self.Total = Total
    
    def __repr__(self):
        return f'<Compra {self.CompraID}>'
    
    def save(self):
        if not self.CompraID:
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
    def get_by_usuario(cls, usuario_id):
        return cls.query.filter_by(UsuarioID=usuario_id).all()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()