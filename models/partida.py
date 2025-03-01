from models.base import db
from datetime import datetime

class Partida(db.Model):
    __tablename__ = 'matches'
    
    id = db.Column(db.Integer, primary_key=True)
    player1_id = db.Column(db.Integer, db.ForeignKey('jogadores.id'), nullable=False)
    player2_id = db.Column(db.Integer, db.ForeignKey('jogadores.id'), nullable=False)
    score_player1 = db.Column(db.Integer, nullable=False)
    score_player2 = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    player1 = db.relationship('Jogador', foreign_keys=[player1_id], backref='matches_as_player1')
    player2 = db.relationship('Jogador', foreign_keys=[player2_id], backref='matches_as_player2')
    
    def __repr__(self):
        return f'<Partida {self.player1.name} vs {self.player2.name} ({self.score_player1}-{self.score_player2})>'
