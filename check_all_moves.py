# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Check All Moves

def check_all_moves(board,player):
    from find_moves import find_moves

    all_pieces = []
    all_dests = []
    all_jumpers = []
    jump_dests = []
    for i in range(0,32):
        test_piece = 2**i
        if (board[player] & (test_piece)) and board[player] - (test_piece) >= 0:
            [piece,dests,jumped] = find_moves(test_piece,board,player)
            if dests != []:
                all_pieces.extend([piece])
                all_dests.extend(dests)
                for j in range(0,len(jumped)):
                    if jumped[j] != '':
                        all_jumpers.extend([piece])
                        jump_dests.extend([dests[j]])
    if all_jumpers != []:
        all_pieces = all_jumpers
        all_dests = jump_dests

    return [all_pieces,all_dests]
