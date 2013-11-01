def check_free(square,board):
    from map_input import map_input
    from check_input import check_input

    full_board = sum(board)
    if bin(full_board).count('1') + 1 != bin(full_board + square).count('1'):
        return check_free(map_input(check_input(input('Square already occupied; select again: '))),board);
    else:
        return square
