import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

if not os.path.exists('estadio.db'):
    print("Error: El archivo de base de datos 'estadio.db' no existe.")
    exit(1)

engine = create_engine(
    'sqlite:///estadio.db',
    pool_size=5,
    connect_args={'check_same_thread': False}
)

try:
    with engine.connect() as connection:
        print("Conexión a la base de datos establecida correctamente.")
except FileNotFoundError as e:
    print(f"Error: El archivo de base de datos no se encontró: {e}")
except OperationalError as e:
    print(f"Error de base de datos: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
