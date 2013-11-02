# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# AlphaBeta

def alphabeta(state,depth,alpha,beta,maxp):
    from heuristic import heuristic
    from get_all_moves import get_all_moves
    from after_move import after_move

    move = []
    choice_moves = []

    if depth == 0: #or terminal(state)
        state_val = heuristic(state)
        return [state_val,[]]
    if maxp:
        moves = get_all_moves(state)
        for i in range(0,len(moves)):
            temp_state = after_move(moves[i],state)
            [a_temp,move_temp] = alphabeta(temp_state,depth-1,alpha,beta,0)
            if a_temp > alpha:
                alpha = a_temp
                move = moves[i]
                choice_moves = [move]
            elif a_temp == alpha:
                choice_moves.append([moves[i]])
            if beta <= alpha:
                break
        if len(choice_moves) > 1:
            from random import choice
            move = choice(choice_moves)
        return [alpha,move]
    else:
        moves = get_all_moves(state)
        for i in range(0,len(moves)):
            temp_state = after_move(moves[i],state)
            [b_temp,move_temp] = alphabeta(temp_state,depth-1,alpha,beta,1)
            if b_temp < beta:
                beta = b_temp
                move = moves[i]
                choice_moves = [move]
            elif b_temp == beta:
                choice_moves.extend([moves[i]])
            if beta <= alpha:
                break
        if len(choice_moves) > 1:
            from random import choice
            move = choice(choice_moves)
        return [beta,move]
