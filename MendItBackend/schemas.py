from pydantic import BaseModel, EmailStr
from typing import Optional, List

# ── Auth ──────────────────────────────────────────────────────────────────────

class RegisterRequest(BaseModel):
    nome: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

class AuthResponse(BaseModel):
    id: int
    nome: str
    email: str
    token: str

# ── Videos ────────────────────────────────────────────────────────────────────

class VideoResponse(BaseModel):
    id: int
    titulo: str
    descricao_curta: Optional[str] = None
    descricao: Optional[str] = None
    video_url: str
    duration: Optional[str] = None
    views: Optional[str] = None
    categoria: Optional[str] = None
    ferramentas: Optional[List[str]] = None
    dicas_seguranca: Optional[List[str]] = None

    class Config:
        from_attributes = True

# ── Favoritos ─────────────────────────────────────────────────────────────────

class AddFavoritoRequest(BaseModel):
    video_id: int
    user_id: int

class FavoritoResponse(BaseModel):
    id: int
    video_id: int
    user_id: int
    video: Optional[VideoResponse] = None

    class Config:
        from_attributes = True
