import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers import ProductoController
from __init__ import app, db

def test_producto_controller():
    producto_id = None
    
    # Datos de prueba con nombres en minúscula para el constructor
    producto_test = {
        "nombre": "Producto Prueba",
        "descripcion": "Descripción del producto de prueba",
        "precio": 99.99,
        "imagen": "ruta/imagen.jpg",
        "stock": 100,
        "categoria": "Electrónicos",
        "talla": "M"
    }
    
    print("🧪 Iniciando pruebas de ProductoController...")
    
    # 1. Prueba de creación de producto
    print("\n1. Probando creación de producto...")
    try:
        resultado_creacion = ProductoController.create(producto_test)
        if resultado_creacion["success"]:
            print("✅ Producto creado exitosamente")
            producto_id = resultado_creacion["data"]["ProductoID"]
            print(f"📝 Datos del producto: {resultado_creacion['data']}")
        else:
            print(f"❌ Error al crear producto: {resultado_creacion['error']}")
    except Exception as e:
        print(f"❌ Excepción al crear producto: {str(e)}")
    
    # 2. Prueba de búsqueda por ID
    print("\n2. Probando búsqueda por ID...")
    try:
        if producto_id:
            resultado_busqueda_id = ProductoController.get_by_id(1)
            if resultado_busqueda_id["success"]:
                print("✅ Producto encontrado por ID exitosamente")
                print(f"📝 Datos del producto: {resultado_busqueda_id['data']}")
            else:
                print(f"❌ Error al buscar producto por ID: {resultado_busqueda_id['error']}")
        else:
            print("⚠️ No se puede probar búsqueda por ID sin un producto creado")
    except Exception as e:
        print(f"❌ Excepción al buscar por ID: {str(e)}")
    
    # 3. Prueba de búsqueda por categoría
    print("\n3. Probando búsqueda por categoría...")
    try:
        resultado_categoria = ProductoController.get_by_categoria("Electrónicos")
        if resultado_categoria["success"]:
            print("✅ Productos encontrados por categoría exitosamente")
            print(f"📝 Cantidad de productos: {len(resultado_categoria['data'])}")
        else:
            print(f"❌ Error al buscar productos por categoría: {resultado_categoria['error']}")
    except Exception as e:
        print(f"❌ Excepción al buscar por categoría: {str(e)}")
    
    # 4. Prueba de obtener todos los productos
    print("\n4. Probando obtener todos los productos...")
    try:
        resultado_todos = ProductoController.get_all()
        if resultado_todos["success"]:
            print("✅ Lista de productos obtenida exitosamente")
            print(f"📝 Cantidad total de productos: {len(resultado_todos['data'])}")
        else:
            print(f"❌ Error al obtener todos los productos: {resultado_todos['error']}")
    except Exception as e:
        print(f"❌ Excepción al obtener todos los productos: {str(e)}")
    
    # 5. Prueba de actualización de stock
    print("\n5. Probando actualización de stock...")
    try:
        if producto_id:
            resultado_actualizacion = ProductoController.actualizar_stock(producto_id, 50)
            if resultado_actualizacion["success"]:
                print("✅ Stock actualizado exitosamente")
                print(f"📝 Nuevo stock: {resultado_actualizacion['data']['Stock']}")
            else:
                print(f"❌ Error al actualizar stock: {resultado_actualizacion['error']}")
        else:
            print("⚠️ No se puede probar actualización de stock sin un producto creado")
    except Exception as e:
        print(f"❌ Excepción al actualizar stock: {str(e)}")
    
    # 6. Prueba de actualización de producto
    print("\n6. Probando actualización de producto...")
    try:
        if producto_id:
            producto_actualizado = producto_test.copy()
            producto_actualizado["Precio"] = 149.99
            resultado_update = ProductoController.update(producto_id, producto_actualizado)
            if resultado_update["success"]:
                print("✅ Producto actualizado exitosamente")
                print(f"📝 Datos actualizados: {resultado_update['data']}")
            else:
                print(f"❌ Error al actualizar producto: {resultado_update['error']}")
        else:
            print("⚠️ No se puede probar actualización sin un producto creado")
    except Exception as e:
        print(f"❌ Excepción al actualizar producto: {str(e)}")
    
    # 7. Prueba de eliminación de producto
    print("\n7. Probando eliminación de producto...")
    try:
        if producto_id:
            resultado_eliminacion = ProductoController.delete(producto_id)
            if resultado_eliminacion["success"]:
                print("✅ Producto eliminado exitosamente")
            else:
                print(f"❌ Error al eliminar producto: {resultado_eliminacion['error']}")
        else:
            print("⚠️ No se puede probar eliminación sin un producto creado")
    except Exception as e:
        print(f"❌ Excepción al eliminar producto: {str(e)}")

if __name__ == "__main__":
    test_producto_controller() 