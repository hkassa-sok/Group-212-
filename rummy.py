def calculate_score(rounds):
    """
    Calculates total score over multiple rounds of Gin Rummy.

    Each round is a tuple:
    (player_deadwood, opponent_deadwood, went_gin, knocked)
    """

    total_score = 0

    for round_data in rounds:
        player_deadwood, opponent_deadwood, went_gin, knocked = round_data

        # Player goes gin
        if went_gin:
            total_score += 20 + opponent_deadwood

        # Player knocks
        elif knocked:
            if player_deadwood < opponent_deadwood:
                total_score += opponent_deadwood - player_deadwood
            else:
                # Undercut (opponent wins bonus)
                total_score -= (10 + (player_deadwood - opponent_deadwood))

    return total_score