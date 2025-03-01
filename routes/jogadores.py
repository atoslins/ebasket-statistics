from flask import Blueprint, render_template, request, jsonify
from models.base import db
from models.jogador import Jogador
from models.partida import Partida
from sqlalchemy import or_, and_

jogadores_bp = Blueprint('jogadores', __name__)

@jogadores_bp.route('/')
def index():
    jogadores = Jogador.get_all_jogadores()
    return render_template('index.html', jogadores=jogadores)

@jogadores_bp.route('/api/jogadores')
def get_jogadores():
    jogadores = Jogador.get_all_jogadores()
    return jsonify(jogadores)

@jogadores_bp.route('/api/jogadores/<string:jogador_name>/adversarios')
def get_adversarios(jogador_name):
    # Find all players who have played against the selected player
    adversarios_query = db.session.query(Partida.time2_jogador.distinct())\
        .filter(Partida.time1_jogador == jogador_name)
    
    adversarios_query2 = db.session.query(Partida.time1_jogador.distinct())\
        .filter(Partida.time2_jogador == jogador_name)
    
    # Combine results and remove duplicates
    adversarios_names = set([a[0] for a in adversarios_query.all() if a[0]] + 
                           [a[0] for a in adversarios_query2.all() if a[0]])
    
    # Remove the player themselves
    if jogador_name in adversarios_names:
        adversarios_names.remove(jogador_name)
    
    # Format for JSON response
    adversarios = [{'id': idx, 'name': name} for idx, name in enumerate(sorted(adversarios_names), 1)]
    
    return jsonify(adversarios)
