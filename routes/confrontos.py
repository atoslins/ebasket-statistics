from flask import Blueprint, render_template, request
from sqlalchemy import or_, and_
from models.partida import Partida
from models.base import db
from statistics.stats_engine import get_confronto_statistics

confrontos_bp = Blueprint('confrontos', __name__)

@confrontos_bp.route('/confrontos')
def show_confrontos():
    player1 = request.args.get('player1')
    player2 = request.args.get('player2')
    
    if not player1 or not player2:
        return render_template('confrontos.html', matches=[], player1=None, player2=None)
    
    # Query matches where player1 and player2 faced each other
    matches = Partida.query.filter(
        or_(
            and_(Partida.time1_jogador == player1, Partida.time2_jogador == player2),
            and_(Partida.time1_jogador == player2, Partida.time2_jogador == player1)
        )
    ).order_by(Partida.data.desc()).all()
    
    # Get statistics for this confrontation
    estatisticas = get_confronto_statistics(player1, player2)
    
    return render_template('confrontos.html', 
                          matches=matches, 
                          player1=player1, 
                          player2=player2,
                          estatisticas=estatisticas)
