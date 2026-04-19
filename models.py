from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    favoritos = relationship("Favorito", back_populates="user", cascade="all, delete")

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao_curta = Column(String, nullable=True)
    descricao = Column(Text, nullable=True)
    video_url = Column(String, nullable=False)
    duration = Column(String, nullable=True)
    views = Column(String, nullable=True)
    categoria = Column(String, nullable=True)
    ferramentas = Column(JSON, nullable=True)       # lista de strings
    dicas_seguranca = Column(JSON, nullable=True)   # lista de strings
    favoritos = relationship("Favorito", back_populates="video", cascade="all, delete")

class Favorito(Base):
    __tablename__ = "favoritos"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    video_id = Column(Integer, ForeignKey("videos.id"), nullable=False)
    user = relationship("User", back_populates="favoritos")
    video = relationship("Video", back_populates="favoritos")
