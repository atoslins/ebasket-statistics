from flask import Blueprint, render_template, request, jsonify
from models.schema_inspection import get_all_players, get_opponents

jogadores_bp = Blueprint('jogadores', __name__)

@jogadores_bp.route('/')
def index():
    players = get_all_players()
    return render_template('index.html', players=players)

@jogadores_bp.route('/api/opponents')
def get_player_opponents():
    player_name = request.args.get('player')
    if not player_name:
        return jsonify([])
    
    opponents = get_opponents(player_name)
    return jsonify(opponents)
