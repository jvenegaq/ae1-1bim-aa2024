import pymongo

# Conectar a MongoDB local
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['mi_base_de_datos']  

    print("Conexión a la base de datos establecida correctamente.")
except pymongo.errors.ConnectionFailure as e:
    print(f"Error de conexión a la base de datos: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")

# Registros de la colección LocalesComida por calificación
lista_LocalesComida = db['LocalesComida'].find().sort("calificacion", pymongo.ASCENDING)

# Registros de la colección CentrosDeportivos por costo de membresía
lista_CentrosDeportivos = db['CentrosDeportivos'].find().sort("costo_membresia", pymongo.ASCENDING)

# Presenta la información de cada documento en LocalesComida
print("Locales de Comida:")
for localescomida in lista_LocalesComida:
    print(f"Nombre: {localescomida['nombre']}")
    print(f"Calificación: {localescomida['calificacion']}")

# Presentar la información de cada documento en CentrosDeportivos
print("\nCentros Deportivos:")
for centrosdeportivos in lista_CentrosDeportivos:
    print(f"Nombre: {centrosdeportivos['nombre']}")
    print(f"Costo membresía: {centrosdeportivos['costo_membresia']}")
