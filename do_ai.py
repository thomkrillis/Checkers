# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Do AI

def do_ai(board,player):
    from alphabeta import alphabeta
    from flatten import flatten
    import globes
    
    from time import time

    alpha = float("-inf")
    beta = float("inf")

    depth_limit = 1
    while 1:
        [holder,move,timeout,first] = alphabeta([board,player],0,depth_limit,alpha,beta,1,player,1)
        if timeout:
            if first:
                print "Only one move."
                print "Depth finished: " + str(depth_limit-1)
                break
            else:
                print "time up"
                print "Depth finished: " + str(depth_limit-1)
                move = old_move
                holder = old_holder
                break
        if move == []:
            old_move = flatten(old_move)
            old_move[2] = [old_move[2]]
            return [old_move,old_holder]
        elif move[0] == '':
            old_move = flatten(old_move)
            old_move[2] = [old_move[2]]
            return [old_move,old_holder]
        current_time = time() - globes.timer
        if current_time > 0.90 * globes.limit:
            print "TIME UP"
            print "Depth finished: " + str(depth_limit)
            break
        old_move = move
        old_holder = holder
        depth_limit = depth_limit+1

    move = flatten(move)

    if len(move) == 3:
        piece = move[0]
        dest = move[1]
        jumped = [move[2]]
    elif len(move) > 3:
        piece = move[0]
        dest = move[1]
        jumped = [move[2:]]
    else:
        piece = move[0]
        dest = move[1][0]
        jumped = [move[1][1]]

    print "heur: " + str(holder)
    return [piece,dest,jumped,holder]
