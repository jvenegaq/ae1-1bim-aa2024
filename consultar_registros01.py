from sqlalchemy.orm import sessionmaker
from crear_entidades import Estadio
from base_datos import engine

Session = sessionmaker(bind=engine)  
session = Session()
estadios = session.query(Estadio).all()
for estadio in estadios:
    print(estadio)
