from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text

from base_datos import engine

Base = declarative_base()

class Estadio(Base):
    __tablename__ = "estadios"
    id_estadio = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    ubicacion = Column(String(255), nullable=False)
    tamaño = Column(String(255), nullable=False)
    capacidad = Column(Integer, nullable=False)
    tipo_césped = Column(String(255), nullable=False)

    def __str__(self):
        return f"{self.nombre} ({self.ubicacion}) - Capacidad: {self.capacidad}, Tipo de césped: {self.tipo_césped}"

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una clase Session, desde el generador de clases de SQLAlchemy sessionmaker.
Session = sessionmaker(bind=engine)  # Se usa el engine
# Crear un objeto llamado session de tipo Session, que permite guardar, eliminar, actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Estadio.
# Se hace uso del método query.
# order_by permite ordenar la búsqueda, con base a las propiedades de la entidad
lista_estadios = session.query(Estadio).order_by(Estadio.capacidad).all()
# La variable lista_estadios tendrá un listado de objetos de tipo Estadio ordenados por la propiedad capacidad de la entidad

# Se realiza un proceso iterativo para presentar la información de cada objeto.
print("Estadios:")
for estadio in lista_estadios:
    print(f"Nombre: {estadio.nombre}")
    print(f"Ubicación: {estadio.ubicacion}")
    print(f"Tamaño: {estadio.tamaño}")
    print(f"Capacidad: {estadio.capacidad}")
    print(f"Tipo de césped: {estadio.tipo_césped}")
    print()  # Para separar cada estadio con una línea en blanco
