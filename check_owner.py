def check_owner(square,board,player):
    from map_input import map_input
    from check_input import check_input

    if bin(board[player]).count('1') - 1 != bin(board[player] - square).count('1'):
        return check_owner(map_input(check_input(input('You have no piece on that square; select again: '))),board,player);
    else:
        return square
