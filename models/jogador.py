from models.base import db

class Jogador(db.Model):
    """
    This is a virtual model that doesn't exist in the database.
    It's used to represent players extracted from the matches table.
    """
    __tablename__ = 'jogadores_view'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Jogador {self.nome}>'
