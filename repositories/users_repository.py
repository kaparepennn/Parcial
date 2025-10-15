import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from models.users_model import User
from sqlalchemy.orm import Session

class UserRepository:

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_users(self):
        #SELECT * FROM users;
        logger.info("Obteniendo todos los usuarios desde el repositorio")
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):
        #SELECT * FROM users WHERE id = user_id;
        logger.info(f"Buscando usuario por ID: {user_id}")
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, username: str, password: str):
        #INSERT INTO users (username, password) VALUES (username, password);
        logger.info(f"Creando usuario: {username}")
        new_user = User(username=username, password=password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_user(self, user_id: int, username: str = None, password: str = None):
        user = self.get_user_by_id(user_id)
        if user:
            logger.info(f"Actualizando usuario: {user_id}")
            if username:
                user.username = username
            if password:
                user.password = password
            self.db.commit()
            self.db.refresh(user)
            return user
        logger.warning(f"Usuario no encontrado para actualizar: {user_id}")
        return None
    
    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            logger.info(f"Eliminando usuario: {user_id}")
            self.db.delete(user)
            self.db.commit()
            return user
        logger.warning(f"Usuario no encontrado para eliminar: {user_id}")
        return None