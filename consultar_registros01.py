from sqlalchemy.orm import sessionmaker
# Importar la clase Estadio desde el archivo crear_entidades
from crear_entidades import Estadio
# Importar el engine
from base_datos import engine

# Se crea una clase llamada Session, desde el generador de clases de SQLAlchemy sessionmaker.
Session = sessionmaker(bind=engine)  # Se usa el engine
# Importante, se crea un objeto llamado session de tipo Session, que permite guardar, eliminar, actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Estadio. Se hace uso del método query. all, significa que se obtienen todos los registros.
estadios = session.query(Estadio).all()
# La variable estadios tendrá un listado de objetos de tipo Estadio.

# Se realiza un proceso iterativo para presentar la información de cada objeto.
for estadio in estadios:
    print(estadio)
