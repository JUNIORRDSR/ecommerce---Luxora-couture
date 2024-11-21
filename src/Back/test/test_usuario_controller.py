import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers import UsuarioController
from __init__ import app, db

def test_usuario_controller():
    usuario_id = None
    
    # Datos de prueba con nombres que coinciden con el constructor
    usuario_test = {
        "nombre_completo": "Usuario Prueba",
        "email": "usuario.prueba@email.com",
        "contraseña": "contraseña123",
        "cedula": "1234567890",
        "telefono": "3001234567"
    }
    
    print("🧪 Iniciando pruebas de UsuarioController...")
    
    # 1. Prueba de creación de usuario
    print("\n1. Probando creación de usuario...")
    try:
        resultado_creacion = UsuarioController.create(usuario_test)
        if resultado_creacion["success"]:
            print("✅ Usuario creado exitosamente")
            usuario_id = resultado_creacion["data"]["UsuarioID"]
            print(f"📝 Datos del usuario: {resultado_creacion['data']}")
        else:
            print(f"❌ Error al crear usuario: {resultado_creacion['error']}")
    except Exception as e:
        print(f"❌ Excepción al crear usuario: {str(e)}")
    
    # 2. Prueba de búsqueda por ID
    print("\n2. Probando búsqueda por ID...")
    try:
        if usuario_id:
            resultado_busqueda_id = UsuarioController.get_by_id(usuario_id)
            if resultado_busqueda_id["success"]:
                print("✅ Usuario encontrado por ID exitosamente")
                print(f"📝 Datos del usuario: {resultado_busqueda_id['data']}")
            else:
                print(f"❌ Error al buscar usuario por ID: {resultado_busqueda_id['error']}")
        else:
            print("⚠️ No se puede probar búsqueda por ID sin un usuario creado")
    except Exception as e:
        print(f"❌ Excepción al buscar por ID: {str(e)}")
    
    # 3. Prueba de búsqueda por email
    print("\n3. Probando búsqueda,  por email...")
    try:
        resultado_email = UsuarioController.get_by_email("carlos.rodriguez@example.com")
        if resultado_email["success"]:
            print("✅ Usuario encontrado por email exitosamente")
            print(f"📝 Datos del usuario: {resultado_email['data']}")
        else:
            print(f"❌ Error al buscar usuario por email: {resultado_email['error']}")
    except Exception as e:
        print(f"❌ Excepción al buscar por email: {str(e)}")
    
    # 4. Prueba de búsqueda por cédula
    print("\n4. Probando búsqueda por cédula...")
    try:
        resultado_cedula = UsuarioController.get_by_cedula("123456789")
        if resultado_cedula["success"]:
            print("✅ Usuario encontrado por cédula exitosamente")
            print(f"📝 Datos del usuario: {resultado_cedula['data']}")
        else:
            print(f"❌ Error al buscar usuario por cédula: {resultado_cedula['error']}")
    except Exception as e:
        print(f"❌ Excepción al buscar por cédula: {str(e)}")
    
    # 5. Prueba de obtener todos los usuarios
    print("\n5. Probando obtener todos los usuarios...")
    try:
        resultado_todos = UsuarioController.get_all()
        if resultado_todos["success"]:
            print("✅ Lista de usuarios obtenida exitosamente")
            print(f"📝 Cantidad total de usuarios: {len(resultado_todos['data']),resultado_todos['data']}")
        else:
            print(f"❌ Error al obtener todos los usuarios: {resultado_todos['error']}")
    except Exception as e:
        print(f"❌ Excepción al obtener todos los usuarios: {str(e)}")
    
    # 6. Prueba de actualización de usuario
    print("\n6. Probando actualización de usuario...")
    try:
        usuario_actualizado = usuario_test.copy()
        usuario_actualizado["nombre_completo"] = "Usuario Actualizado"
        resultado_update = UsuarioController.update(3, usuario_actualizado)  # Usando ID 3 que existe
        if resultado_update["success"]:
            print("✅ Usuario actualizado exitosamente")
            print(f"📝 Datos actualizados: {resultado_update['data']}")
        else:
            print(f"❌ Error al actualizar usuario: {resultado_update['error']}")
    except Exception as e:
        print(f"❌ Excepción al actualizar usuario: {str(e)}")
    
    # 7. Prueba de eliminación de usuario
    print("\n7. Probando eliminación de usuario...")
    try:
        resultado_eliminacion = UsuarioController.delete(3)  # Usando ID 3 que existe
        if resultado_eliminacion["success"]:
            print("✅ Usuario eliminado exitosamente")
        else:
            print(f"❌ Error al eliminar usuario: {resultado_eliminacion['error']}")
    except Exception as e:
        print(f"❌ Excepción al eliminar usuario: {str(e)}")

if __name__ == "__main__":
    test_usuario_controller() 