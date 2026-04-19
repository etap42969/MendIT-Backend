from database import SessionLocal, engine, Base
from models import Video

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Só insere se não houver vídeos
    if db.query(Video).count() > 0:
        db.close()
        return

    videos = [
        Video(
            titulo="Lâmpadas fluorescentes - Como trocar",
            descricao_curta="Aprende a trocar qualquer tipo de lâmpada em casa de forma rápida e segura.",
            descricao="Tutorial completo para trocar lâmpadas fluorescentes, LED e halogéneo em casa sem chamar eletricista.",
            video_url="file:///android_asset/lampadas.mp4",  # vídeo local
            duration="3:21",
            views="12K visualizações",
            categoria="Elétrica",
            ferramentas=[
                "Escadote ou banquinho",
                "Pano seco",
                "Lâmpada de substituição",
                "Luvas de borracha",
            ],
            dicas_seguranca=[
                "Desliga sempre o interruptor antes de começar",
                "Espera que a lâmpada arrefeça completamente",
                "Nunca toques na lâmpada com as mãos nuas (halogéneo)",
                "Usa escadote estável — nunca cadeiras",
            ],
        ),
        Video(
            titulo="Consertar torneira que pinga sem gastar nada",
            descricao_curta="Resolve o problema da torneira a pingar em menos de 10 minutos.",
            descricao="Com ferramentas básicas que tens em casa, consegues resolver este problema sozinho.",
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # substitui por URL real
            duration="5:47",
            views="8.4K visualizações",
            categoria="Hidráulica",
            ferramentas=[
                "Chave inglesa ajustável",
                "Chave de fendas",
                "Vedante/O-ring de substituição",
                "Massa vedante",
                "Balde pequeno",
            ],
            dicas_seguranca=[
                "Fecha o registro de água principal antes de começar",
                "Coloca um pano debaixo para absorver a água residual",
                "Não aperta demasiado as peças roscadas",
                "Testa devagar ao abrir a água no final",
            ],
        ),
        Video(
            titulo="Tomada sem energia — como diagnosticar",
            descricao_curta="Descobre por que uma tomada parou de funcionar e como resolver.",
            descricao="Guia passo a passo para diagnosticar e resolver o problema sem chamar eletricista.",
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            duration="4:10",
            views="21K visualizações",
            categoria="Elétrica",
            ferramentas=[
                "Multímetro ou testador de tomada",
                "Chave de fendas isolada",
                "Lanterna",
                "Disjuntor de substituição (se necessário)",
            ],
            dicas_seguranca=[
                "NUNCA trabalhes em tomadas com corrente ligada",
                "Desliga o disjuntor no quadro elétrico",
                "Verifica com testador se não há tensão antes de tocar",
                "Em caso de cheiro a queimado, chama um eletricista",
            ],
        ),
        Video(
            titulo="Pintar uma parede como um profissional",
            descricao_curta="Técnicas profissionais para pintar paredes sem manchas nem escorrimentos.",
            descricao="Aprende a preparar e pintar paredes em casa com resultado profissional.",
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            duration="8:15",
            views="34K visualizações",
            categoria="Pintura",
            ferramentas=[
                "Rolo de pintura",
                "Pincel de 2 polegadas",
                "Fita de pintor",
                "Protetor de chão",
                "Tinta de primário",
                "Lixa fina",
            ],
            dicas_seguranca=[
                "Ventila bem o espaço durante e após a pintura",
                "Usa máscara se estiveres a lixar tinta antiga",
                "Cobre tomadas e interruptores com fita isolante",
                "Não mistures tintas de base diferentes",
            ],
        ),
        Video(
            titulo="Porta rangendo — como resolver em 5 minutos",
            descricao_curta="Elimina o barulho de porta rangendo de forma simples e rápida.",
            descricao="Aprende as causas do rangido e como resolver definitivamente.",
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            duration="2:55",
            views="5.1K visualizações",
            categoria="Alvenaria",
            ferramentas=[
                "Spray lubrificante (WD-40)",
                "Chave de fendas",
                "Pano limpo",
            ],
            dicas_seguranca=[
                "Não uses óleo de cozinha — atrai pó e suja",
                "Aplica o lubrificante com a porta aberta",
            ],
        ),
    ]

    db.add_all(videos)
    db.commit()
    db.close()
    print("Base de dados populada com videos de exemplo!")

if __name__ == "__main__":
    seed()
