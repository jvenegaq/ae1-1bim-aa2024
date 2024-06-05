from sqlalchemy.orm import sessionmaker
# Importar la clase Estadio desde el archivo crear_entidades
from crear_entidades import Estadio
# Importar el engine
from base_datos import engine

# Se crea una clase llamada Session, desde el generador de clases de SQLAlchemy sessionmaker.
Session = sessionmaker(bind=engine)  # Se usa el engine
# Importante, se crea un objeto llamado session de tipo Session, que permite guardar, eliminar, actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Estadio con una condición.
# Se hace uso del método query.
# filter permite agregar condiciones a la búsqueda, con base a las propiedades de la entidad
estadios_nombre = session.query(Estadio).filter(Estadio.nombre == "Estadio Olímpico")
estadios_ubicacion = session.query(Estadio).filter(Estadio.ubicacion == "Quito")

# Se realiza un proceso iterativo para presentar la información de cada objeto.
print("Estadios con el nombre 'Estadio Olímpico':")
for estadio in estadios_nombre:
    print(estadio)

print("\nEstadios en la ubicación 'Quito':")
for estadio in estadios_ubicacion:
    print(estadio)
