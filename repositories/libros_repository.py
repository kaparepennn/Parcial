<<<<<<< HEAD
from models.libros_model import libro
from sqlalchemy.orm import Session

class LibrosRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    # Recuperar todos los libros almacenados en la base de datos
    def get_all_libros(self):
        return self.db.query(libro).all()

    # Busca y retorna un libro por ID
    def get_libro_by_id(self, libro_id: int):
        return self.db.query(libro).filter(libro.id == libro_id).first()

    # Crea y almacena un nuevo libro en la base de datos
    def create_libro(self, name: str):
        nuevo_libro = libro(name=name)
        self.db.add(nuevo_libro)
        self.db.commit()
        self.db.refresh(nuevo_libro)
        return nuevo_libro

    # Actualizar la información de un libro existente
    def actualizar_libro(self, libro_id: int, name: str = None):
        libro_obj = self.get_libro_by_id(libro_id)
        if libro_obj and name:
            libro_obj.name = name
            self.db.commit()
            self.db.refresh(libro_obj)
        return libro_obj

    # Eliminar un libro por ID
    def eliminar_libro(self, libro_id: int):
        libro_obj = self.get_libro_by_id(libro_id)
        if libro_obj:
            self.db.delete(libro_obj)
            self.db.commit()
        return libro_obj
=======
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from models.libros_model import libro, autor
from sqlalchemy.orm import Session

class libroRepository:
#Repositorio para la gestión de libros en la base de datos
    def __init__(self, db_session: Session):
        self.db = db_session

#Recuperar todos los libros almacenados de la base de datos
    def get_all_libros(self):
        logger.info("Obteniendo todos los libros desde el repositorio")
        return self.db.query(libro).all()

#Busca y retorna un libro por ID
    def get_libro_by_id(self, libro_id: int):
        logger.info(f"Buscando libro por ID: {libro_id}")
        return self.db.query(libro).filter(libro.id == libro_id).first()

#Crea y almacena un nuevo libro en la base de datos
    def create_libro(self, name: str):
        logger.info(f"Creando libro: {name}")
        new_libro = libro(name=name)
        self.db.add(new_libro)
        self.db.commit()
        self.db.refresh(new_libro)
        return new_libro

#Actualizar la información de un libro  existente en la base de datos.
    def update_libro(self, libro_id: int, name: str = None):
        libro = self.get_libro_by_id(libro_id)
        if libro and name:
            logger.info(f"Actualizando libro: {libro_id}")
            libro.name = name
            self.db.commit()
            self.db.refresh(libro)
        else:
            logger.warning(f"libro no encontrado para actualizar: {libro_id}")
        return libro

#Eliminar un libro de la base de datos, según su ID
    def delete_libro(self, libro_id: int):
        libro = self.get_libro_by_id(libro_id)
        if libro:
            logger.info(f"Eliminando libro: {libro_id}")
            self.db.delete(libro)
            self.db.commit()
        else:
            logger.warning(f"libro no encontrado para eliminar: {libro_id}")
        return libro
>>>>>>> dev
