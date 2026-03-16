# MendIt Backend — FastAPI + SQLite

## Instalação

```bash
# 1. Instalar Python 3.10+ se não tiveres
# https://www.python.org/downloads/

# 2. Entrar na pasta
cd MendItBackend

# 3. Criar ambiente virtual
python -m venv venv

# 4. Ativar ambiente virtual
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 5. Instalar dependências
pip install -r requirements.txt

# 6. Iniciar o servidor
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Testar

Abre o browser em:
- http://localhost:8000 → health check
- http://localhost:8000/docs → documentação interativa (Swagger)

## Endpoints

| Método | URL | Descrição |
|--------|-----|-----------|
| POST | /auth/register | Registar utilizador |
| POST | /auth/login | Login |
| GET | /videos | Listar vídeos (opcional ?q=pesquisa) |
| GET | /videos/:id | Vídeo por ID |
| GET | /favoritos/:userId | Favoritos do utilizador |
| POST | /favoritos | Adicionar favorito |
| DELETE | /favoritos/:id | Remover favorito |

## Ligação ao emulador Android

No emulador Android, o localhost do PC é `10.0.2.2`.

Em `src/services/api.ts` da app:
```ts
export const BASE_URL = 'http://10.0.2.2:8000';
```
