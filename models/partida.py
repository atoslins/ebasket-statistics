from models.base import db
from datetime import datetime

class Partida(db.Model):
    __tablename__ = 'partidas'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    data = db.Column(db.Date)
    hora = db.Column(db.String(10))
    arena = db.Column(db.String(100))
    status = db.Column(db.String(50))
    
    time1_nome = db.Column(db.String(100))
    time1_jogador = db.Column(db.String(100))
    time1_placar_final = db.Column(db.Integer)
    time1_placar_periodos = db.Column(db.String(50))
    
    time2_nome = db.Column(db.String(100))
    time2_jogador = db.Column(db.String(100))
    time2_placar_final = db.Column(db.Integer)
    time2_placar_periodos = db.Column(db.String(50))
    
    def __repr__(self):
        return f'<Partida {self.id}: {self.time1_jogador} vs {self.time2_jogador}>'
    
    @property
    def formatted_date(self):
        if self.data:
            return self.data.strftime('%d/%m/%Y')
        return "Data não disponível"
