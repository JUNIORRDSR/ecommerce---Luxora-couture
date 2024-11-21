import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import DetalleCompra
from __init__ import app, db

def test_detalle_compra():
    with app.app_context():
        detalle_id = None
        
        # Datos de prueba siguiendo el orden exacto de la tabla
        detalle_test = {
            "CompraID": 1,           # Asumiendo que existe una compra con ID 1
            "ProductoID": 1,         # Asumiendo que existe un producto con ID 1
            "Cantidad": 2,
            "PrecioUnitario": 99.99
        }
        
        print("🧪 Iniciando pruebas de DetalleCompra...")
        
        # 1. Prueba de creación de detalle
        print("\n1. Probando creación de detalle...")
        try:
            nuevo_detalle = DetalleCompra(
                CompraID=detalle_test["CompraID"],
                ProductoID=detalle_test["ProductoID"],
                Cantidad=detalle_test["Cantidad"],
                PrecioUnitario=detalle_test["PrecioUnitario"]
            )
            nuevo_detalle.save()
            detalle_id = nuevo_detalle.DetalleCompraID
            if detalle_id:
                print("✅ Detalle creado exitosamente")
                print(f"📝 ID del detalle: {detalle_id}")
            else:
                print("❌ Error al crear detalle")
        except Exception as e:
            print(f"❌ Excepción al crear detalle: {str(e)}")
        
        # 2. Prueba de búsqueda por ID
        print("\n2. Probando búsqueda por ID...")
        try:
            if detalle_id:
                detalle = DetalleCompra.get_by_id(detalle_id)
                if detalle:
                    print("✅ Detalle encontrado por ID exitosamente")
                    print(f"📝 Datos del detalle: {detalle}")
                else:
                    print("❌ Detalle no encontrado")
            else:
                print("⚠️ No se puede probar búsqueda por ID sin un detalle creado")
        except Exception as e:
            print(f"❌ Excepción al buscar por ID: {str(e)}")
        
        # 3. Prueba de búsqueda por compra
        print("\n3. Probando búsqueda por compra...")
        try:
            detalles_compra = DetalleCompra.get_by_compra(1)  # Compra ID 1
            if detalles_compra:
                print("✅ Detalles encontrados por compra exitosamente")
                print(f"📝 Cantidad de detalles: {len(detalles_compra)}")
                for detalle in detalles_compra:
                    print(f"📝 Detalle: {detalle}")
            else:
                print("❌ No se encontraron detalles para la compra")
        except Exception as e:
            print(f"❌ Excepción al buscar por compra: {str(e)}")
        
        # 4. Prueba de búsqueda por producto
        print("\n4. Probando búsqueda por producto...")
        try:
            detalles_producto = DetalleCompra.get_by_producto(1)  # Producto ID 1
            if detalles_producto:
                print("✅ Detalles encontrados por producto exitosamente")
                print(f"📝 Cantidad de detalles: {len(detalles_producto)}")
                for detalle in detalles_producto:
                    print(f"📝 Detalle: {detalle}")
            else:
                print("❌ No se encontraron detalles para el producto")
        except Exception as e:
            print(f"❌ Excepción al buscar por producto: {str(e)}")
        
        # 5. Prueba de actualización de detalle
        print("\n5. Probando actualización de detalle...")
        try:
            if detalle_id:
                detalle = DetalleCompra.get_by_id(detalle_id)
                if detalle:
                    detalle.Cantidad = 3
                    detalle.PrecioUnitario = 89.99
                    detalle.update()
                    print("✅ Detalle actualizado exitosamente")
                    print(f"📝 Detalle actualizado: {detalle}")
                else:
                    print("❌ No se encontró el detalle para actualizar")
            else:
                print("⚠️ No se puede probar actualización sin un detalle creado")
        except Exception as e:
            print(f"❌ Excepción al actualizar detalle: {str(e)}")
        
        # 6. Prueba de eliminación de detalle
        print("\n6. Probando eliminación de detalle...")
        try:
            if detalle_id:
                detalle = DetalleCompra.get_by_id(detalle_id)
                if detalle:
                    detalle.delete()
                    print("✅ Detalle eliminado exitosamente")
                else:
                    print("❌ No se encontró el detalle para eliminar")
            else:
                print("⚠️ No se puede probar eliminación sin un detalle creado")
        except Exception as e:
            print(f"❌ Excepción al eliminar detalle: {str(e)}")

if __name__ == "__main__":
    test_detalle_compra() 