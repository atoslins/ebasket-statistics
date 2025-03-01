"""
Script para criar a tabela de estatísticas de confrontos
"""
from models.base import db
from models.estatistica import EstatisticaConfronto
from app import create_app

def create_estatisticas_table():
    """
    Cria a tabela de estatísticas de confrontos no banco de dados
    """
    app = create_app()
    with app.app_context():
        # Cria a tabela se ela não existir
        db.create_all()
        print("Tabela de estatísticas de confrontos criada com sucesso!")

if __name__ == "__main__":
    create_estatisticas_table()
