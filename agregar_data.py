from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///estadio.db')
Base = declarative_base()
class Estadio(Base):
    __tablename__ = 'estadios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
    tamaño = Column(String, nullable=False)
    capacidad = Column(Integer, nullable=False)
    tipo_césped = Column(String, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

session = Session()

estadio1 = Estadio(nombre="Estadio Monumental", ubicacion="Quito", tamaño="105m x 68m", capacidad=55000, tipo_césped="Natural")
estadio2 = Estadio(nombre="Estadio Olímpico", ubicacion="Guayaquil", tamaño="105m x 70m", capacidad=60000, tipo_césped="Artificial")
estadio3 = Estadio(nombre="Estadio Nacional", ubicacion="Cuenca", tamaño="100m x 65m", capacidad=45000, tipo_césped="Mixto")

session.add_all([estadio1, estadio2, estadio3])

try:
    session.commit()
    print("Estadios almacenados correctamente en la base de datos.")
except Exception as e:
    print(f"Error al almacenar datos: {e}")
    session.rollback()

session.close()
