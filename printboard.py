# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Print Board

def printboard(board,selected=[],dests=[]):
    from string import maketrans
    import re
    import math

    from flatten import flatten

#    if selected != '':
#        print bin(selected)[2:].zfill(32)

    #add player piece locations together to make string (0 no pieces, 1 player 1's piece, 2 player 2's piece)
    board_string = str(int(bin(board[0])[2:].zfill(32)) + 2 * int(bin(board[1])[2:].zfill(32)) + 4 * int(bin(board[2])[2:].zfill(32))).zfill(32)

    selected = flatten([selected])
    if selected != []:
        board_list = list(board_string)
        for i in range(0,len(selected)):
            board_list[len(board_list)-int(math.log(selected[i],2))-1] = '3'
        board_string = "".join(board_list)

    if dests != []:
        board_list = list(board_string)
        for i in range(0,len(dests)):
            board_list[len(board_list)-int(math.log(dests[i],2))-1] = '4'
        board_string = "".join(board_list)

    #add underscores to represent unplayable squares
    board_string = re.sub('(.{0})', '\\1|', board_string, 4, re.DOTALL)
    board_string = board_string[:8] + re.sub('(.{1})', '\\1|', board_string[8:], 4, re.DOTALL)
    board_string = board_string[:16] + re.sub('(.{0})', '\\1|', board_string[16:], 4, re.DOTALL)
    board_string = board_string[:24] + re.sub('(.{1})', '\\1|', board_string[24:], 4, re.DOTALL)
    board_string = board_string[:32] + re.sub('(.{0})', '\\1|', board_string[32:], 4, re.DOTALL)
    board_string = board_string[:40] + re.sub('(.{1})', '\\1|', board_string[40:], 4, re.DOTALL)
    board_string = board_string[:48] + re.sub('(.{0})', '\\1|', board_string[48:], 4, re.DOTALL)
    board_string = board_string[:56] + re.sub('(.{1})', '\\1|', board_string[56:], 4, re.DOTALL)

    #add a space between every adjacent square in each row
    board_string = re.sub('(.{1})', '\\1 ', board_string, 0, re.DOTALL)

    #add newlines every 8 squares to create the 2D representation
    board_string = re.sub('(.{16})', '\\1\n', board_string, 0, re.DOTALL)

    #change representation of player pieces and empty squares
    board_string = board_string.translate(maketrans('0123456','_HOPDKJ'),"'[]")

    print board_string
