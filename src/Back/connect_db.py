from sqlalchemy import create_engine
from Back.config import DATABASE_URL

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Conectar a la base de datos
connection = engine.connect()

print("Conexión exitosa a la base de datos")