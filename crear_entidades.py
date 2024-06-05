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

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)  
session = Session()
lista_estadios = session.query(Estadio).order_by(Estadio.capacidad).all()

print("Estadios:")
for estadio in lista_estadios:
    print(f"Nombre: {estadio.nombre}")
    print(f"Ubicación: {estadio.ubicacion}")
    print(f"Tamaño: {estadio.tamaño}")
    print(f"Capacidad: {estadio.capacidad}")
    print(f"Tipo de césped: {estadio.tipo_césped}")
    print()  
