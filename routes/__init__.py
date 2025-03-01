from routes.jogadores import jogadores_bp
from routes.confrontos import confrontos_bp

def register_routes(app):
    app.register_blueprint(jogadores_bp)
    app.register_blueprint(confrontos_bp)
