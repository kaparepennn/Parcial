import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from repositories.libros_repository import libroRepository
from models.libros_model import libro
from sqlalchemy.orm import Session

class libroService:
    def __init__(self, db_session: Session):
        self.repository = libroRepository(db_session)
        logger.info("Servicio de libros inicializado")

    def listar_libros(self):
        logger.info("Listando todos los libros")
        return self.repository.get_all_libros()

    def obtener_libro(self, libro_id: int):
        logger.info(f"Obteniendo libro por ID: {libro_id}")
        return self.repository.get_libro_by_id(libro_id)

    def crear_libro(self, name: str):
        logger.info(f"Creando libro: {name}")
        return self.repository.create_libro(name)

    def actualizar_libro(self, libro_id: int, name: str = None):
        logger.info(f"Actualizando libro: {libro_id}")
        return self.repository.update_libro(libro_id, name)

    def eliminar_libro(self, libro_id: int):
        logger.info(f"Eliminando libro: {libro_id}")
        return self.repository.delete_libro(libro_id)
