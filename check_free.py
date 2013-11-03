def check_free(square,board):
    from map_input import map_input
    from check_input import check_input

    if (sum(board[:2]) & square):
        return check_free(map_input(check_input(input('Square already occupied; select again: '))),board);
    else:
        return square
