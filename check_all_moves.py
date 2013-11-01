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
        if bin(board[player]).count('1') - 1 == bin(board[player] - (test_piece)).count('1') and board[player] - (test_piece) >= 0:
            [piece,dests,jumped] = find_moves(test_piece,board,player)
            if dests != []:
                all_pieces.extend([piece])
                all_dests.extend(dests)
                if jumped != []:
                    all_jumpers.extend([piece])
                    jump_dests.extend(dests)
    if all_jumpers != []:
        all_pieces = all_jumpers
        all_dests = jump_dests

    return [all_pieces,all_dests]
