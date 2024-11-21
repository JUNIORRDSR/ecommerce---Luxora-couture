import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Compra, DetalleCompra
from schemas import CompraSchema, DetalleCompraSchema
from __init__ import db, app

class CompraController:
    @staticmethod
    def get_all():
        with app.app_context():
            try:
                compras = Compra.query.all()
                schema = CompraSchema(many=True)
                return {"success": True, "data": schema.dump(compras)}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def get_by_id(compra_id):
        with app.app_context():
            try:
                compra = Compra.query.get_or_404(compra_id)
                schema = CompraSchema()
                return {"success": True, "data": schema.dump(compra)}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def create(data, detalles):
        with app.app_context():
            try:
                # Crear nueva compra
                nueva_compra = Compra(
                    UsuarioID=data['usuario_id'],
                    MetodoPago=data['metodo_pago'],
                    Total=data['total']
                )
                
                db.session.add(nueva_compra)
                db.session.flush()  # Para obtener el ID de la compra
                
                # Crear los detalles de la compra
                detalles_creados = []
                for detalle in detalles:
                    nuevo_detalle = DetalleCompra(
                        CompraID=nueva_compra.CompraID,
                        ProductoID=detalle['producto_id'],
                        Cantidad=detalle['cantidad'],
                        PrecioUnitario=detalle['precio_unitario']
                    )
                    db.session.add(nuevo_detalle)
                    detalles_creados.append(nuevo_detalle)
                
                db.session.commit()
                
                # Preparar respuesta
                schema_compra = CompraSchema()
                schema_detalle = DetalleCompraSchema(many=True)
                respuesta = schema_compra.dump(nueva_compra)
                respuesta['detalles'] = schema_detalle.dump(detalles_creados)
                
                return {"success": True, "data": respuesta}
            except Exception as e:
                db.session.rollback()
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def get_by_usuario(usuario_id):
        with app.app_context():
            try:
                compras = Compra.query.filter_by(UsuarioID=usuario_id).all()
                schema = CompraSchema(many=True)
                return {"success": True, "data": schema.dump(compras)}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def get_by_estado(estado):
        with app.app_context():
            try:
                compras = Compra.query.filter_by(Estado=estado).all()
                schema = CompraSchema(many=True)
                return {"success": True, "data": schema.dump(compras)}
            except Exception as e:
                return {"success": False, "error": str(e)}
            
    @staticmethod
    def update(id, data):
        with app.app_context():
            try:
                compra = Compra.query.get_or_404(id)
                if compra:
                    if 'estado' in data:
                        compra.Estado = data['estado']
                    if 'total' in data:
                        compra.Total = data['total']
                    
                    db.session.commit()
                    schema = CompraSchema()
                    return {"success": True, "data": schema.dump(compra)}
                return {"success": False, "error": "Compra no encontrada"}
            except Exception as e:
                db.session.rollback()
                return {"success": False, "error": str(e)}
    
    @staticmethod
    def delete(id):
        with app.app_context():
            try:
                compra = Compra.query.get_or_404(id)
                if compra:
                    # Primero eliminar los detalles asociados
                    for detalle in compra.detalles:
                        db.session.delete(detalle)
                    # Luego eliminar la compra
                    db.session.delete(compra)
                    db.session.commit()
                    return {"success": True, "message": "Compra y sus detalles eliminados exitosamente"}
                return {"success": False, "error": "Compra no encontrada"}
            except Exception as e:
                db.session.rollback()
                return {"success": False, "error": str(e)}