import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db

class Usuario(db.Model, UserMixin):
    __tablename__ = 'Usuario'
    
    UsuarioID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NombreCompleto = db.Column(db.String(150), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Contraseña = db.Column(db.String(255), nullable=False)
    Cedula = db.Column(db.String(20), unique=True, nullable=False)
    Telefono = db.Column(db.String(20))
    
    # Relación con Compra
    compras = db.relationship('Compra', backref='usuario', lazy=True)
    
    # Constructor
    def __init__(self, nombre_completo, email, contraseña, cedula, telefono=None):
        self.NombreCompleto = nombre_completo
        self.Email = email
        self.Contraseña = contraseña
        self.Cedula = cedula
        self.Telefono = telefono
    
    # Para compatibilidad con Flask-Login
    def get_id(self):
        return str(self.UsuarioID)
    
    # Representación del usuario
    def __repr__(self):
        return f'<Usuario {self.Email}>'
    
    # Métodos para el manejo seguro de contraseñas
    def set_contraseña(self, contraseña):
        self.Contraseña = generate_password_hash(contraseña)
        
    def check_contraseña(self, contraseña):
        return check_password_hash(self.Contraseña, contraseña)
    
    # Métodos CRUD básicos
    def save(self):
        if not self.UsuarioID:
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
    def get_by_email(cls, email):
        return cls.query.filter_by(Email=email).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()