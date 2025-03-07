from flask import Flask
from config import Config
from models.base import db
from models.partida import Partida
from routes import register_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    
    # Create tables if missing
    with app.app_context():
        db.create_all()
    
    # Register blueprints
    register_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
