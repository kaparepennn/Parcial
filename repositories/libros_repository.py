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