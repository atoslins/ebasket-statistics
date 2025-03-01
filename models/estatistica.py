from models.base import db
from datetime import datetime

class EstatisticaConfronto(db.Model):
    __tablename__ = 'estatisticas_confronto'
    
    id = db.Column(db.Integer, primary_key=True)
    jogador1 = db.Column(db.String(100), nullable=False)
    jogador2 = db.Column(db.String(100), nullable=False)
    total_partidas = db.Column(db.Integer, default=0)
    vitorias_jogador1 = db.Column(db.Integer, default=0)
    vitorias_jogador2 = db.Column(db.Integer, default=0)
    empates = db.Column(db.Integer, default=0)
    media_pontos_jogador1 = db.Column(db.Float, default=0.0)
    media_pontos_jogador2 = db.Column(db.Float, default=0.0)
    ultima_atualizacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, jogador1, jogador2, total_partidas=0, vitorias_jogador1=0, 
                 vitorias_jogador2=0, empates=0, media_pontos_jogador1=0.0, 
                 media_pontos_jogador2=0.0):
        # Garantir que jogador1 e jogador2 estejam em ordem alfabética para consistência
        if jogador1 > jogador2:
            jogador1, jogador2 = jogador2, jogador1
            vitorias_jogador1, vitorias_jogador2 = vitorias_jogador2, vitorias_jogador1
            media_pontos_jogador1, media_pontos_jogador2 = media_pontos_jogador2, media_pontos_jogador1
            
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.total_partidas = total_partidas
        self.vitorias_jogador1 = vitorias_jogador1
        self.vitorias_jogador2 = vitorias_jogador2
        self.empates = empates
        self.media_pontos_jogador1 = media_pontos_jogador1
        self.media_pontos_jogador2 = media_pontos_jogador2
        
    @property
    def percentual_vitorias_jogador1(self):
        if self.total_partidas == 0:
            return 0
        return (self.vitorias_jogador1 / self.total_partidas) * 100
        
    @property
    def percentual_vitorias_jogador2(self):
        if self.total_partidas == 0:
            return 0
        return (self.vitorias_jogador2 / self.total_partidas) * 100
        
    @property
    def percentual_empates(self):
        if self.total_partidas == 0:
            return 0
        return (self.empates / self.total_partidas) * 100
        
    @classmethod
    def get_or_create(cls, jogador1, jogador2):
        # Garantir que jogador1 e jogador2 estejam em ordem alfabética para consistência
        if jogador1 > jogador2:
            jogador1, jogador2 = jogador2, jogador1
            
        estatistica = cls.query.filter_by(jogador1=jogador1, jogador2=jogador2).first()
        if not estatistica:
            estatistica = cls(jogador1=jogador1, jogador2=jogador2)
            db.session.add(estatistica)
            db.session.commit()
        return estatistica
