# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# After Move (board after moving some specified move)

def after_move(move,state):
    from flatten import flatten

    piece = move[0]
    dest = move[1][0]
    jumped = move[1][1]
    
    board = state[0]
    board = board[:]
    player = state[1]

    king = 2

    #update board
    board[player] = board[player]-piece+dest
    #if len(jumped) == 1:
    jumped = flatten(jumped)
    if jumped != [] and jumped != ['']:
        for i in range(0,len(jumped)):
            board[1-player] = board[1-player] - jumped[i]
            #if jumped piece was king
            if bin(board[king]).count('1') - 1 == bin(board[king] - (jumped[i])).count('1'):
                #update king position
                board[king] = board[king]-jumped[i]

    return [board,1-player]
