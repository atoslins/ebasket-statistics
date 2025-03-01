from flask import Blueprint, render_template, request, jsonify
from models.base import db
from models.jogador import Jogador
from models.partida import Partida
from sqlalchemy import or_, and_

jogadores_bp = Blueprint('jogadores', __name__)

@jogadores_bp.route('/')
def index():
    jogadores = Jogador.query.order_by(Jogador.name).all()
    return render_template('index.html', jogadores=jogadores)

@jogadores_bp.route('/api/jogadores')
def get_jogadores():
    jogadores = Jogador.query.order_by(Jogador.name).all()
    return jsonify([{'id': j.id, 'name': j.name} for j in jogadores])

@jogadores_bp.route('/api/jogadores/<int:jogador_id>/adversarios')
def get_adversarios(jogador_id):
    # Find all players who have played against the selected player
    subquery = db.session.query(Partida.player2_id.distinct())\
        .filter(Partida.player1_id == jogador_id).subquery()
    
    subquery2 = db.session.query(Partida.player1_id.distinct())\
        .filter(Partida.player2_id == jogador_id).subquery()
    
    adversarios = Jogador.query\
        .filter(or_(
            Jogador.id.in_(subquery),
            Jogador.id.in_(subquery2)
        ))\
        .filter(Jogador.id != jogador_id)\
        .order_by(Jogador.name)\
        .all()
    
    return jsonify([{'id': j.id, 'name': j.name} for j in adversarios])
