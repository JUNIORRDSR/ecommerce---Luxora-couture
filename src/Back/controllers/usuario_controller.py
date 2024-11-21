import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Usuario
from schemas import UsuarioSchema
from __init__ import db, app

class UsuarioController:
    @staticmethod
    def get_all():
        with app.app_context():
            try:
                usuarios = Usuario.query.all()
                schema = UsuarioSchema(many=True)
                return {"success": True, "data": schema.dump(usuarios)}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def get_by_id(usuario_id):
        with app.app_context():
            try:
                usuario = Usuario.query.get_or_404(usuario_id)
                schema = UsuarioSchema()
                return {"success": True, "data": schema.dump(usuario)}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def create(data):
        with app.app_context():
            try:
                nuevo_usuario = Usuario(
                    nombre_completo=data['nombre_completo'],
                    email=data['email'],
                    contraseña=data['contraseña'],
                    cedula=data['cedula'],
                    telefono=data.get('telefono')
                )
                
                db.session.add(nuevo_usuario)
                db.session.commit()
                
                schema = UsuarioSchema()
                return {"success": True, "data": schema.dump(nuevo_usuario)}
            except Exception as e:
                db.session.rollback()
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def get_by_email(email):
        with app.app_context():
            try:
                usuario = Usuario.query.filter_by(Email=email).first()
                schema = UsuarioSchema()
                return {"success": True, "data": schema.dump(usuario)}
            except Exception as e:
                return {"success": False, "error": str(e)}
            
    @staticmethod
    def get_by_cedula(cedula):
        with app.app_context():
            try:
                usuario = Usuario.query.filter_by(Cedula=cedula).first()
                schema = UsuarioSchema()
                return {"success": True, "data": schema.dump(usuario)}
            except Exception as e:
                return {"success": False, "error": str(e)}
            
    @staticmethod
    def update(id, data):
        with app.app_context():
            try:
                usuario = Usuario.query.get(id)
                if usuario:
                    if 'nombre_completo' in data:
                        usuario.nombre_completo = data['nombre_completo']
                    if 'email' in data:
                        usuario.email = data['email']
                    if 'contraseña' in data:
                        usuario.contraseña = data['contraseña']
                    if 'cedula' in data:
                        usuario.cedula = data['cedula']
                    if 'telefono' in data:
                        usuario.telefono = data['telefono']
                    
                    db.session.commit()
                    schema = UsuarioSchema()
                    return {"success": True, "data": schema.dump(usuario)}
                return {"success": False, "error": "Usuario no encontrado"}
            except Exception as e:
                db.session.rollback()
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def delete(id):
        with app.app_context():
            try:
                usuario = Usuario.query.get_or_404(id)
                if usuario:
                    db.session.delete(usuario)
                    db.session.commit()
                    return {"success": True, "message": "Usuario eliminado exitosamente"}
                return {"success": False, "error": "Usuario no encontrado"}
            except Exception as e:
                db.session.rollback()
                return {"success": False, "error": str(e)}
            
