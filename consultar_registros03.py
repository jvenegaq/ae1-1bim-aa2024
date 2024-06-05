from sqlalchemy.orm import sessionmaker
# Se importa la clase Estadio desde el archivo crear_entidades
from crear_entidades import Estadio
# Se importa el engine
from base_datos import engine

# Se crea una clase llamada Session, desde el generador de clases de SQLAlchemy sessionmaker.
Session = sessionmaker(bind=engine)  # Se usa el engine
# Importante, se crea un objeto llamado session de tipo Session, que permite guardar, eliminar, actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Estadio.
# Se hace uso del método query.
# order_by permite ordenar la búsqueda, con base a las propiedades de la entidad
lista_estadios = session.query(Estadio).order_by(Estadio.capacidad).all()
# La variable lista_estadios tendrá un listado de objetos de tipo Estadio
# ordenados por la propiedad capacidad de la entidad

# Se realiza un proceso iterativo para presentar la información de cada objeto.
print("Estadios:")
for estadio in lista_estadios:
    print(f"Nombre: {estadio.nombre}")
    print(f"Ubicación: {estadio.ubicacion}")
    print(f"Tamaño: {estadio.tamaño}")
    print(f"Capacidad: {estadio.capacidad}")
    print(f"Tipo de césped: {estadio.tipo_césped}")
    print()  # Para separar cada estadio con una línea en blanco
