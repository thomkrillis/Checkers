# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Do AI

def do_ai(board,player):
    from alphabeta import alphabeta
    from flatten import flatten

    alpha = float("-inf")
    beta = float("inf")

    [holder,move] = alphabeta([board,player],1,alpha,beta,1)

    move = flatten(move)

    piece = move[0]
    dest = move[1]
    jumped = [move[2]]

    return [piece,dest,jumped]
