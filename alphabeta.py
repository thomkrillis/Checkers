# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# AlphaBeta

def alphabeta(state,depth,depth_limit,alpha,beta,maxp,op,first=0):
    from heuristic import heuristic
    from get_all_moves import get_all_moves
    from after_move import after_move
    import globes

    from time import time

    move = []
    choice_moves = []
    timeout = 0
    percent = 0.97
    offset = 0.08

    if depth_limit - depth == 0 or bin(state[0][0])[2:].count('1') == 0 or bin(state[0][1])[2:].count('1') == 0:
        state[1] = op
        state_val = heuristic(state)
        current_time = time() - globes.timer
        if current_time > percent * globes.limit - offset:
            timeout = 1
        return [state_val,[],timeout,0]
    if maxp:
        moves = get_all_moves(state)
        if len(moves) == 1 and first:
            return [0,moves,1,1]
        for i in range(0,len(moves)):
            temp_state = after_move(moves[i],state)
            [a_temp,move_temp,timeout,holder] = alphabeta(temp_state,depth+1,depth_limit,alpha,beta,0,op)
            if timeout:
                break
            if a_temp > alpha:
                alpha = a_temp
                move = moves[i]
                choice_moves = [move]
            elif a_temp == alpha:
                choice_moves.append([moves[i]])
            if beta < alpha:
                break
            current_time = time() - globes.timer
            if current_time > percent * globes.limit - offset:
                timeout = 1
                break
        if len(choice_moves) > 1:
            from random import choice
            move = choice(choice_moves)
        if moves == []:
            return [100,[],timeout,0]
        else:
            return [alpha,move,timeout,0]
    else:
        moves = get_all_moves(state)
        for i in range(0,len(moves)):
            temp_state = after_move(moves[i],state)
            [b_temp,move_temp,timeout,holder] = alphabeta(temp_state,depth+1,depth_limit,alpha,beta,1,op)
            if timeout:
                break
            if b_temp < beta:
                beta = b_temp
                move = moves[i]
                choice_moves = [move]
            elif b_temp == beta:
                choice_moves.extend([moves[i]])
            if beta < alpha:
                break
            current_time = time() - globes.timer
            if current_time > percent * globes.limit - offset:
                timeout = 1
                break
        if len(choice_moves) > 1:
            from random import choice
            move = choice(choice_moves)
        if moves == []:
            return [-100,[],timeout,0]
        else:
            return [beta,move,timeout,0]
