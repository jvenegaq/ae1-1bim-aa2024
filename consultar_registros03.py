from sqlalchemy.orm import sessionmaker
from crear_entidades import Estadio
from base_datos import engine

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
