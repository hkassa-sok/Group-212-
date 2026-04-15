def find_sets(hand):
    """
    Finds all the common sets that a player has in their hand in order to
    highlight how many points they possibly have
    """
    groups_sets = {}
    # Ranking the cards based on what group they are in
    for card in hand:
        ranks = card[0]

        if ranks not in groups_sets:
            groups_sets[ranks] = []

        groups_sets[ranks].append(card)

        # Find valid sets
        sets = []
        for ranks in groups_sets:
           if len(groups_sets[ranks]) >= 3:
               sets.append(groups_sets[ranks])
               
        return sets
              

def can_knock(hand):
    """
    Checks if the player can knock by adding up
    the deadwood points in their hand.
    Returns True if deadwood is 10 or less.
    """
    total = 0

    for card in hand:
        points = card["points"]
        total += points

    if total <= 10:
        return True
    else:
        return False
