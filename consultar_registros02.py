from sqlalchemy.orm import sessionmaker
from crear_entidades import Estadio
from base_datos import engine

Session = sessionmaker(bind=engine)  
session = Session()
estadios_nombre = session.query(Estadio).filter(Estadio.nombre == "Estadio Olímpico")
estadios_ubicacion = session.query(Estadio).filter(Estadio.ubicacion == "Quito")

print("Estadios con el nombre 'Estadio Olímpico':")
for estadio in estadios_nombre:
    print(estadio)

print("\nEstadios en la ubicación 'Quito':")
for estadio in estadios_ubicacion:
    print(estadio)
