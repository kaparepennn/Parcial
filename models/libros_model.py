import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from sqlalchemy import Column, Integer, String, ForeignKey
<<<<<<< HEAD
from sqlalchemy.orm import relationship, declarative_base
=======
from sqlalchemy.orm import relationship
>>>>>>> dev
from models.db import Base

class libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    autores = relationship('autor', back_populates='libro', cascade='all, delete-orphan')

class autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True, index=True)
<<<<<<< HEAD
    name = Column(String(255), nullable=False)
    libro_id = Column(Integer, ForeignKey("libros.id"))
    libro = relationship("libro", back_populates="autores")
=======
    title = Column(String(255), nullable=False)
    libro_id = Column(Integer, ForeignKey('libros.id'))
    libro = relationship('libro', back_populates='autores')
>>>>>>> dev
