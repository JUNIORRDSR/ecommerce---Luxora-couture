import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from __init__ import db, app
from sqlalchemy import text

def probar_conexion():
    with app.app_context():
        try:
            # Intenta ejecutar una consulta simple usando text()
            resultado = db.session.execute(text('SELECT * FROM usuario'))
            print("✅ Conexión exitosa a la base de datos")
            for fila in resultado:
                print(f"Valores en la fila: {fila}")
            return True
        except Exception as e:
            print(f"❌ Error de conexión: {str(e)}")
            return False

if __name__ == '__main__':
    probar_conexion() 