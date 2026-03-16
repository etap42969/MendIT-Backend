from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

from database import engine, Base, get_db
from models import User, Video, Favorito
from schemas import (
    RegisterRequest, LoginRequest, AuthResponse,
    VideoResponse, AddFavoritoRequest, FavoritoResponse,
)
from auth import hash_password, verify_password, create_token
from seed import seed

# Cria as tabelas e popula com dados de exemplo
Base.metadata.create_all(bind=engine)
seed()

app = FastAPI(title="MendIt API", version="1.0.0")

# CORS — permite ligações do emulador Android e dispositivos locais
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Auth ──────────────────────────────────────────────────────────────────────

@app.post("/auth/register", response_model=AuthResponse)
def register(body: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == body.email).first():
        raise HTTPException(status_code=400, detail="Email já registado.")
    user = User(
        nome=body.nome,
        email=body.email,
        hashed_password=hash_password(body.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return AuthResponse(id=user.id, nome=user.nome, email=user.email, token=create_token(user.id, user.email))

@app.post("/auth/login", response_model=AuthResponse)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email).first()
    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
    return AuthResponse(id=user.id, nome=user.nome, email=user.email, token=create_token(user.id, user.email))

# ── Videos ────────────────────────────────────────────────────────────────────

@app.get("/videos", response_model=List[VideoResponse])
def get_videos(q: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Video)
    if q:
        query = query.filter(Video.titulo.ilike(f"%{q}%"))
    return query.all()

@app.get("/videos/{video_id}", response_model=VideoResponse)
def get_video(video_id: int, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Vídeo não encontrado.")
    return video

# ── Favoritos ─────────────────────────────────────────────────────────────────

@app.get("/favoritos/{user_id}", response_model=List[FavoritoResponse])
def get_favoritos(user_id: int, db: Session = Depends(get_db)):
    return db.query(Favorito).filter(Favorito.user_id == user_id).all()

@app.post("/favoritos", response_model=FavoritoResponse)
def add_favorito(body: AddFavoritoRequest, db: Session = Depends(get_db)):
    existing = db.query(Favorito).filter(
        Favorito.user_id == body.user_id,
        Favorito.video_id == body.video_id,
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Já está nos favoritos.")
    fav = Favorito(user_id=body.user_id, video_id=body.video_id)
    db.add(fav)
    db.commit()
    db.refresh(fav)
    return fav

@app.delete("/favoritos/{favorito_id}")
def remove_favorito(favorito_id: int, db: Session = Depends(get_db)):
    fav = db.query(Favorito).filter(Favorito.id == favorito_id).first()
    if not fav:
        raise HTTPException(status_code=404, detail="Favorito não encontrado.")
    db.delete(fav)
    db.commit()
    return {"ok": True}

# ── Health check ──────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"status": "MendIt API a funcionar ✅"}
