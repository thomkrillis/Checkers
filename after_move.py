# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# After Move (board after moving some specified move)

def after_move(move,state):
    from flatten import flatten
    from became_king import became_king

    piece = move[0]
    dest = move[1][0]
    jumped = move[1][1]
    
    board = state[0]
    board = board[:]
    player = state[1]

    king = 2

    #if piece was king
    if board[king] & piece:
        #update king position
        board[king] = board[king]-piece+dest
    else:
        #check if piece became king
        if became_king(dest,board,player):
            board[king] = board[king]+dest

    #update board
    board[player] = board[player]-piece+dest
    #if len(jumped) == 1:
    jumped = flatten(jumped)
    if jumped != [] and jumped != ['']:
        for i in range(0,len(jumped)):
            board[1-player] = board[1-player] - jumped[i]
            #if jumped piece was king
            if board[king] & jumped[i]:
                #update king position
                board[king] = board[king]-jumped[i]

    return [board,1-player]
