from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.exc import IntegrityError

# Configuración de la conexión a la base de datos
engine = create_engine('mysql://usuario:contraseña@localhost/nombre_de_la_base_de_datos')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definición de las clases para las tablas
class ListaTarea(Base):
    __tablename__ = 'ListasTareas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    fecha_creacion = Column(Date, nullable=False, default=datetime.now().date())
    fecha_actualizacion = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate=datetime.now())
    usuario_id = Column(Integer, nullable=False)

class Tarea(Base):
    __tablename__ = 'Tareas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    fecha_creacion = Column(Date, nullable=False, default=datetime.now().date())
    fecha_vencimiento = Column(Date)
    completada = Column(Boolean, nullable=False, default=False)
    lista_id = Column(Integer, nullable=False)

# Insertar datos de ejemplo en las tablas
try:
    # Crear una lista de tareas
    lista = ListaTarea(nombre='Compras', descripcion='Lista de compras semanales', usuario_id=1)
    session.add(lista)
    session.commit()

    # Agregar tareas a la lista
    tarea1 = Tarea(nombre='Comprar leche', lista_id=lista.id)
    tarea2 = Tarea(nombre='Comprar pan', lista_id=lista.id)

    session.add_all([tarea1, tarea2])
    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"Error: {str(e)}")
finally:
    session.close()
