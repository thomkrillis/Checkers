# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Became King

def became_king(piece,board,player):
    if player == 0: #bottom player
        if piece >= 268435456:
            return 1
    elif player == 1: #top player
        if piece <= 8:
            return 1
