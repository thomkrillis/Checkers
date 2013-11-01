# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Show All Moves

def show_all_moves(board,player):
    from printboard import printboard
    from check_all_moves import check_all_moves

    [all_pieces,all_dests] = check_all_moves(board,player)

    printboard(board,all_pieces,all_dests)

    return all_pieces
