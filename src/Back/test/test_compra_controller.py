import os
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers import CompraController
from __init__ import app, db

def test_compra_controller():
    compra_id = None
    
    # Datos de prueba siguiendo el orden exacto de la tabla
    compra_test = {
        "usuario_id": 1,                    # UsuarioID
        "metodo_pago": "Tarjeta de Crédito", # MetodoPago
        "total": 299.97                     # Total
    }
    
    # Datos de prueba para los detalles de la compra
    detalles_test = [
        {
            "producto_id": 1,
            "cantidad": 2,
            "precio_unitario": 99.99,
            "subtotal": 199.98
        },
        {
            "producto_id": 2,
            "cantidad": 1,
            "precio_unitario": 99.99,
            "subtotal": 99.99
        }
    ]
    
    print("🧪 Iniciando pruebas de CompraController...")
    
    # 1. Prueba de creación de compra
    print("\n1. Probando creación de compra...")
    try:
        resultado_creacion = CompraController.create(compra_test, detalles_test)
        if resultado_creacion["success"]:
            print("✅ Compra creada exitosamente")
            compra_id = resultado_creacion["data"]["CompraID"]
            print(f"📝 Datos de la compra: {resultado_creacion['data']}")
        else:
            print(f"❌ Error al crear compra: {resultado_creacion['error']}")
    except Exception as e:
        print(f"❌ Excepción al crear compra: {str(e)}")
    
    # 2. Prueba de búsqueda por ID
    print("\n2. Probando búsqueda por ID...")
    try:
        if compra_id:
            resultado_busqueda_id = CompraController.get_by_id(compra_id)
            if resultado_busqueda_id["success"]:
                print("✅ Compra encontrada por ID exitosamente")
                print(f"📝 Datos de la compra: {resultado_busqueda_id['data']}")
            else:
                print(f"❌ Error al buscar compra por ID: {resultado_busqueda_id['error']}")
        else:
            print("⚠️ No se puede probar búsqueda por ID sin una compra creada")
    except Exception as e:
        print(f"❌ Excepción al buscar por ID: {str(e)}")
    
    # 3. Prueba de búsqueda por usuario
    print("\n3. Probando búsqueda por usuario...")
    try:
        resultado_usuario = CompraController.get_by_usuario(1)  # Usuario ID 1
        if resultado_usuario["success"]:
            print("✅ Compras encontradas por usuario exitosamente")
            print(f"📝 Cantidad de compras: {len(resultado_usuario['data'])}")
            print(f"📝 Datos de las compras: {resultado_usuario['data']}")
        else:
            print(f"❌ Error al buscar compras por usuario: {resultado_usuario['error']}")
    except Exception as e:
        print(f"❌ Excepción al buscar por usuario: {str(e)}")
    
    # 4. Prueba de obtener todas las compras
    print("\n4. Probando obtener todas las compras...")
    try:
        resultado_todos = CompraController.get_all()
        if resultado_todos["success"]:
            print("✅ Lista de compras obtenida exitosamente")
            print(f"📝 Cantidad total de compras: {len(resultado_todos['data'])}")
            print(f"📝 Datos de las compras: {resultado_todos['data']}")
        else:
            print(f"❌ Error al obtener todas las compras: {resultado_todos['error']}")
    except Exception as e:
        print(f"❌ Excepción al obtener todas las compras: {str(e)}")
    
    # 5. Prueba de actualización de compra
    print("\n5. Probando actualización de compra...")
    try:
        if compra_id:
            datos_actualizacion = {
                "metodo_pago": "PayPal",
                "total": 399.97
            }
            resultado_update = CompraController.update(compra_id, datos_actualizacion)
            if resultado_update["success"]:
                print("✅ Compra actualizada exitosamente")
                print(f"📝 Datos actualizados: {resultado_update['data']}")
            else:
                print(f"❌ Error al actualizar compra: {resultado_update['error']}")
        else:
            print("⚠️ No se puede probar actualización sin una compra creada")
    except Exception as e:
        print(f"❌ Excepción al actualizar compra: {str(e)}")
    
    # 6. Prueba de eliminación de compra
    print("\n6. Probando eliminación de compra...")
    try:
        if compra_id:
            resultado_eliminacion = CompraController.delete(compra_id)
            if resultado_eliminacion["success"]:
                print("✅ Compra y sus detalles eliminados exitosamente")
            else:
                print(f"❌ Error al eliminar compra: {resultado_eliminacion['error']}")
        else:
            print("⚠️ No se puede probar eliminación sin una compra creada")
    except Exception as e:
        print(f"❌ Excepción al eliminar compra: {str(e)}")

if __name__ == "__main__":
    test_compra_controller() 