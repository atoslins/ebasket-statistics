"""
This module contains functions for statistical analysis of match data.
"""
from models.partida import Partida
from models.estatistica import EstatisticaConfronto
from models.base import db
from sqlalchemy import or_, and_

def calculate_win_percentage(player1, player2, matches):
    """
    Calculate the win percentage for player1 against player2
    """
    total_matches = len(matches)
    if total_matches == 0:
        return 0
    
    player1_wins = 0
    
    for match in matches:
        if (match.time1_jogador == player1 and match.time1_placar_final > match.time2_placar_final) or \
           (match.time2_jogador == player1 and match.time2_placar_final > match.time1_placar_final):
            player1_wins += 1
    
    return (player1_wins / total_matches) * 100

def calculate_average_score(player, matches):
    """
    Calculate the average score for a player across all matches
    """
    if not matches:
        return 0
    
    total_score = 0
    player_matches = 0
    
    for match in matches:
        if match.time1_jogador == player:
            total_score += match.time1_placar_final or 0
            player_matches += 1
        elif match.time2_jogador == player:
            total_score += match.time2_placar_final or 0
            player_matches += 1
    
    if player_matches == 0:
        return 0
        
    return total_score / player_matches

def update_confronto_statistics(player1, player2):
    """
    Update or create statistics for confrontation between player1 and player2
    """
    # Ensure player1 and player2 are in alphabetical order for consistency
    if player1 > player2:
        player1, player2 = player2, player1
    
    # Get all matches between these players
    matches = Partida.query.filter(
        or_(
            and_(Partida.time1_jogador == player1, Partida.time2_jogador == player2),
            and_(Partida.time1_jogador == player2, Partida.time2_jogador == player1)
        )
    ).all()
    
    # Get or create statistics record
    estatistica = EstatisticaConfronto.get_or_create(player1, player2)
    
    # Calculate statistics
    total_matches = len(matches)
    vitorias_player1 = 0
    vitorias_player2 = 0
    empates = 0
    pontos_player1 = 0
    pontos_player2 = 0
    
    for match in matches:
        # Determine which player is which in this match
        if match.time1_jogador == player1:
            p1_score = match.time1_placar_final or 0
            p2_score = match.time2_placar_final or 0
        else:  # player1 is time2_jogador
            p1_score = match.time2_placar_final or 0
            p2_score = match.time1_placar_final or 0
        
        # Add to total points
        pontos_player1 += p1_score
        pontos_player2 += p2_score
        
        # Determine winner
        if p1_score > p2_score:
            vitorias_player1 += 1
        elif p2_score > p1_score:
            vitorias_player2 += 1
        else:
            empates += 1
    
    # Update statistics
    estatistica.total_partidas = total_matches
    estatistica.vitorias_jogador1 = vitorias_player1
    estatistica.vitorias_jogador2 = vitorias_player2
    estatistica.empates = empates
    estatistica.media_pontos_jogador1 = pontos_player1 / total_matches if total_matches > 0 else 0
    estatistica.media_pontos_jogador2 = pontos_player2 / total_matches if total_matches > 0 else 0
    
    db.session.commit()
    
    return estatistica

def get_confronto_statistics(player1, player2):
    """
    Get statistics for confrontation between player1 and player2
    If statistics don't exist, they will be calculated and stored
    """
    # Ensure player1 and player2 are in alphabetical order for consistency
    if player1 > player2:
        player1, player2 = player2, player1
        swapped = True
    else:
        swapped = False
    
    estatistica = EstatisticaConfronto.query.filter_by(jogador1=player1, jogador2=player2).first()
    
    if not estatistica:
        estatistica = update_confronto_statistics(player1, player2)
    
    # If players were swapped, swap the statistics back
    if swapped:
        return {
            'jogador1': player1,
            'jogador2': player2,
            'total_partidas': estatistica.total_partidas,
            'vitorias_jogador1': estatistica.vitorias_jogador2,
            'vitorias_jogador2': estatistica.vitorias_jogador1,
            'empates': estatistica.empates,
            'media_pontos_jogador1': estatistica.media_pontos_jogador2,
            'media_pontos_jogador2': estatistica.media_pontos_jogador1,
            'percentual_vitorias_jogador1': estatistica.percentual_vitorias_jogador2,
            'percentual_vitorias_jogador2': estatistica.percentual_vitorias_jogador1,
            'percentual_empates': estatistica.percentual_empates
        }
    else:
        return {
            'jogador1': player1,
            'jogador2': player2,
            'total_partidas': estatistica.total_partidas,
            'vitorias_jogador1': estatistica.vitorias_jogador1,
            'vitorias_jogador2': estatistica.vitorias_jogador2,
            'empates': estatistica.empates,
            'media_pontos_jogador1': estatistica.media_pontos_jogador1,
            'media_pontos_jogador2': estatistica.media_pontos_jogador2,
            'percentual_vitorias_jogador1': estatistica.percentual_vitorias_jogador1,
            'percentual_vitorias_jogador2': estatistica.percentual_vitorias_jogador2,
            'percentual_empates': estatistica.percentual_empates
        }
