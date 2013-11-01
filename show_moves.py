# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Show Moves

def show_moves(piece,board,player):
    from printboard import printboard
    from find_moves import find_moves

    [piece,dests,jumped] = find_moves(piece,board,player)

    printboard(board,piece,dests)
    
    if dests == []:
        print "No valid moves for that piece"
        from check_input import check_input
        from map_input import map_input
        from check_owner import check_owner
        [piece, dests,jumped] = show_moves(check_owner(map_input(check_input(input('Choose piece to move: '))),board,player),board,player)
    
    return [piece,dests,jumped]
