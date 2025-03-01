"""
This module will contain functions for statistical analysis of match data.
It's prepared for future implementation.
"""

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

# More statistical functions will be added in the future
