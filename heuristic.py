# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Heuristic

def heuristic(state):
    board = state[0]
    player = state[1]

    #player = 1 - player #heuristic is backwards... don't ask
    king = 2

    pp = bin(board[player])[2:].count('1') #number of player pieces
    op = bin(board[1-player])[2:].count('1') #number of opponent pieces
    pk = 0 #number of player kings
    ok = 0 #number of opponent kings

    #count player kings
    for i in range(0,32):
        test_piece = 2**i
        if bin(board[king]).count('1') - 1 == bin(board[king] - (test_piece)).count('1') and board[king] - (test_piece) >= 0:
            if bin(board[player]).count('1') - 1 == bin(board[player] - (test_piece)).count('1') and board[player] - (test_piece) >= 0:
                pk = pk + 1
            elif bin(board[1-player]).count('1') - 1 == bin(board[1-player] - (test_piece)).count('1') and board[1-player] - (test_piece) >= 0:
                ok = ok + 1

    #count pieces on back wall
    if player == 0:
        pw = bin(board[0])[2:].zfill(32)[28:32].count('1') #player pieces on wall
        ow = bin(board[1])[2:].zfill(32)[0:4].count('1') #opponent pieces on wall
    if player == 1:
        ow = bin(board[0])[2:].zfill(32)[28:32].count('1') #opponent pieces on wall
        pw = bin(board[1])[2:].zfill(32)[0:4].count('1') #player pieces on wall


    #heuristic is all player's piece minus all opponent's pieces (kings count as 1.5 pieces)
    h = pp - op + 0.75 * (pk - ok) + 0.5 * (pw - ow)

    #if player is going to lose, it's REALLY undesirable
    if pp == 0:
        h = -100

    return h
