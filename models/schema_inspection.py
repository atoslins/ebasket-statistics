from sqlalchemy import inspect, MetaData, Table, select, func
from models.base import db
from models.jogador import Jogador
from models.partida import Partida

def inspect_database():
    """Inspect the database and print table information"""
    inspector = inspect(db.engine)
    
    for table_name in inspector.get_table_names():
        print(f"Table: {table_name}")
        print("  Columns:")
        for column in inspector.get_columns(table_name):
            print(f"    - {column['name']}: {column['type']} "
                  f"{'(PK)' if column.get('primary_key') else ''} "
                  f"{'NOT NULL' if not column.get('nullable') else ''}")
        print()

def get_all_players():
    """
    Extract unique player names from the matches table
    """
    # Query all unique player names from time1_jogador
    query1 = select(Partida.time1_jogador.label('nome')).distinct()
    
    # Query all unique player names from time2_jogador
    query2 = select(Partida.time2_jogador.label('nome')).distinct()
    
    # Union the two queries to get all unique player names
    union_query = query1.union(query2)
    
    # Execute the query and return the results
    with db.engine.connect() as conn:
        result = conn.execute(union_query)
        players = [row[0] for row in result if row[0]]
    
    return sorted(players)

def get_opponents(player_name):
    """
    Get all players who have played against the given player
    """
    # Find opponents from time2_jogador where player is in time1_jogador
    query1 = select(Partida.time2_jogador.label('nome')).where(
        Partida.time1_jogador == player_name
    ).distinct()
    
    # Find opponents from time1_jogador where player is in time2_jogador
    query2 = select(Partida.time1_jogador.label('nome')).where(
        Partida.time2_jogador == player_name
    ).distinct()
    
    # Union the two queries
    union_query = query1.union(query2)
    
    # Execute the query and return the results
    with db.engine.connect() as conn:
        result = conn.execute(union_query)
        opponents = [row[0] for row in result if row[0]]
    
    return sorted(opponents)
