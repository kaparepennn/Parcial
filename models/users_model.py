from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Column, Integer, String
from models.db import Base
from datetime import datetime

class user():
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow) #Un campo de tipo DateTime que se establece automáticamente con 
    #la fecha y hora actual cuando se crea un nuevo registro. Usamos datetime.utcnow() para obtener la hora en formato UTC.