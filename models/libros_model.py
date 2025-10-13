from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from db import Base

class libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    autores = relationship("autor", back_populates="libro")

class autores(Base):
    __tablename__ = "autores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    libro_id = Column(Integer, ForeignKey("libros.id"))
    libro = relationship("libro", back_populates="autores")