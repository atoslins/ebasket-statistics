from flask import Blueprint, render_template, request, jsonify
from models.base import db
from models.jogador import Jogador
from models.partida import Partida
from sqlalchemy import or_, and_

confrontos_bp = Blueprint('confrontos', __name__)

@confrontos_bp.route('/confrontos')
def confrontos():
    jogador1_id = request.args.get('jogador1', type=int)
    jogador2_id = request.args.get('jogador2', type=int)
    
    if not jogador1_id or not jogador2_id:
        return render_template('confrontos.html', error="Selecione dois jogadores para ver os confrontos")
    
    jogador1 = Jogador.query.get_or_404(jogador1_id)
    jogador2 = Jogador.query.get_or_404(jogador2_id)
    
    # Get all matches between the two players
    partidas = Partida.query.filter(
        or_(
            and_(Partida.player1_id == jogador1_id, Partida.player2_id == jogador2_id),
            and_(Partida.player1_id == jogador2_id, Partida.player2_id == jogador1_id)
        )
    ).order_by(Partida.date.desc()).all()
    
    # Process matches for display
    confrontos_list = []
    for partida in partidas:
        if partida.player1_id == jogador1_id:
            confronto = {
                'date': partida.date,
                'jogador1_score': partida.score_player1,
                'jogador2_score': partida.score_player2,
                'vencedor': jogador1.name if partida.score_player1 > partida.score_player2 else jogador2.name
            }
        else:
            confronto = {
                'date': partida.date,
                'jogador1_score': partida.score_player2,
                'jogador2_score': partida.score_player1,
                'vencedor': jogador1.name if partida.score_player2 > partida.score_player1 else jogador2.name
            }
        confrontos_list.append(confronto)
    
    return render_template('confrontos.html', 
                          jogador1=jogador1, 
                          jogador2=jogador2, 
                          confrontos=confrontos_list)

@confrontos_bp.route('/api/confrontos')
def get_confrontos():
    jogador1_id = request.args.get('jogador1', type=int)
    jogador2_id = request.args.get('jogador2', type=int)
    
    if not jogador1_id or not jogador2_id:
        return jsonify({'error': 'Selecione dois jogadores para ver os confrontos'}), 400
    
    # Get all matches between the two players
    partidas = Partida.query.filter(
        or_(
            and_(Partida.player1_id == jogador1_id, Partida.player2_id == jogador2_id),
            and_(Partida.player1_id == jogador2_id, Partida.player2_id == jogador1_id)
        )
    ).order_by(Partida.date.desc()).all()
    
    # Process matches for display
    confrontos_list = []
    for partida in partidas:
        if partida.player1_id == jogador1_id:
            confronto = {
                'date': partida.date.strftime('%Y-%m-%d'),
                'jogador1_score': partida.score_player1,
                'jogador2_score': partida.score_player2,
                'vencedor': jogador1_id if partida.score_player1 > partida.score_player2 else jogador2_id
            }
        else:
            confronto = {
                'date': partida.date.strftime('%Y-%m-%d'),
                'jogador1_score': partida.score_player2,
                'jogador2_score': partida.score_player1,
                'vencedor': jogador1_id if partida.score_player2 > partida.score_player1 else jogador2_id
            }
        confrontos_list.append(confronto)
    
    return jsonify(confrontos_list)
