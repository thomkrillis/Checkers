# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Get All Moves

def get_all_moves(state):
    from find_moves import find_moves

    board = state[0]
    player = state[1]

    move_set = []
    legal_move_set = []
    all_pieces = []
    all_dests = []
    all_jumpers = []
    jump_dests = []
    for i in range(0,32):
        test_piece = 2**i
        if bin(board[player]).count('1') - 1 == bin(board[player] - (test_piece)).count('1') and board[player] - (test_piece) >= 0:
            [piece,dests,jumped] = find_moves(test_piece,board,player)
            if dests != []:
                for j in range(0,len(dests)):
                    move_set.append([piece,[dests[j],jumped[j]]])
                    if jumped[j] != '':
                        legal_move_set.append([piece,[dests[j],jumped[j]]])
    if legal_move_set != []:
        move_set = legal_move_set

    return move_set
