from models.base import db
from datetime import datetime

class Partida(db.Model):
    __tablename__ = 'partidas'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    hora = db.Column(db.String)
    arena = db.Column(db.String)
    status = db.Column(db.String)
    
    time1_nome = db.Column(db.String)
    time1_jogador = db.Column(db.String)
    time1_placar_final = db.Column(db.Integer)
    time1_placar_periodos = db.Column(db.String)
    
    time2_nome = db.Column(db.String)
    time2_jogador = db.Column(db.String)
    time2_placar_final = db.Column(db.Integer)
    time2_placar_periodos = db.Column(db.String)
    
    def __repr__(self):
        return f'<Partida {self.time1_nome} vs {self.time2_nome} ({self.time1_placar_final}-{self.time2_placar_final})>'
