from models.base import db

class Jogador(db.Model):
    __tablename__ = 'jogadores'  # This table doesn't exist yet and needs to be created
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    @classmethod
    def get_all_jogadores(cls):
        """
        Extract unique player names from the partidas table since there's no jogadores table yet
        """
        from models.partida import Partida
        
        # Get unique player names from time1_jogador and time2_jogador
        jogadores_time1 = db.session.query(Partida.time1_jogador).distinct().all()
        jogadores_time2 = db.session.query(Partida.time2_jogador).distinct().all()
        
        # Combine and deduplicate
        jogadores_names = set([j[0] for j in jogadores_time1 if j[0]] + [j[0] for j in jogadores_time2 if j[0]])
        
        # Create Jogador objects (these won't be persisted to DB)
        return [{"id": idx, "name": name} for idx, name in enumerate(sorted(jogadores_names), 1)]
    
    def __repr__(self):
        return f'<Jogador {self.name}>'
