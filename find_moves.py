# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Find Moves

def find_moves(piece,board,player,fm=1,king=0,root=''):
    from row_mod import row_mod
    from col_mod import col_mod
    from after_move import after_move

    dests = []
    jumped = []
    king_piece = 0
    if king or bin(board[2]).count('1') - 1 == bin(board[2] - (piece)).count('1'):
        king_piece = 1

    if player == 0 or (player == 1 and king_piece == 1):
        if 134217728 >= piece: #make sure piece not larger than board
            if row_mod(piece) != 0: #check which row piece is on (even in this case)
                #up and left
                if bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece<<4)).count('1'):
                    if fm:
                        if 2147483648L >= piece<<4:
                            dests.append(piece<<4)
                            jumped.append('')
                elif root != 'ul' and col_mod(piece) != 3 and bin(board[player]).count('1') - 1 != bin(board[player] - (piece<<4)).count('1') and bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece<<9)).count('1'):
                    if 2147483648L >= piece<<9:
                        if king_piece:
                            old_piece = piece
                            new_piece = piece<<9
                            jump_piece = piece<<4
                            [new_board,new_player] = after_move([old_piece,[new_piece,[jump_piece]]],[board,player])
                            [holder,new_dests,new_jumped] = find_moves(piece<<9,new_board,player,0,1,'dr')
                        else:
                            [holder,new_dests,new_jumped] = find_moves(piece<<9,board,player,0)
                        dests.extend(new_dests)
                        if new_dests == []:
                            dests.append(piece<<9)
                        if new_jumped != []:
                            if 1-fm:
                                for i in range(0,len(new_jumped)):
                                    jumped.append([piece<<4,new_jumped[i]])
                            else:
                                for i in range(0,len(new_jumped)):
                                    jumped.append([[piece<<4],[new_jumped[i]]])
                        elif fm:
                            jumped.append([piece<<4])
                        else:
                            jumped.extend([piece<<4])
                if col_mod(piece) != 0: #make sure not right edge
                    #up and right
                    if bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece<<3)).count('1'):
                        if fm:
                            if 2147483648L >= piece<<3:
                                dests.append(piece<<3)
                                jumped.append('')
                    elif root != 'ur' and bin(board[player]).count('1') - 1 != bin(board[player] - (piece<<3)).count('1') and bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece<<7)).count('1'):
                        if 2147483648L >= piece<<7:
                            if king_piece:
                                old_piece = piece
                                new_piece = piece<<7
                                jump_piece = piece<<3
                                [new_board,new_player] = after_move([old_piece,[new_piece,[jump_piece]]],[board,player])
                                [holder,new_dests,new_jumped] = find_moves(piece<<7,new_board,player,0,1,'dl')
                            else:
                                [holder,new_dests,new_jumped] = find_moves(piece<<7,board,player,0)
                            dests.extend(new_dests)
                            if new_dests == []:
                                dests.append(piece<<7)
                            if new_jumped != []:
                                if 1-fm:
                                    for i in range(0,len(new_jumped)):
                                        jumped.append([piece<<3,new_jumped[i]])
                                else:
                                    for i in range(0,len(new_jumped)):
                                        jumped.append([[piece<<3],[new_jumped[i]]])
                            elif fm:
                                jumped.append([piece<<3])
                            else:
                                jumped.extend([piece<<3])
            else: #odd row
                if col_mod(piece) != 3: #make sure not left edge
                    #up and left
                    if bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece<<5)).count('1'):
                        if fm:
                            if 2147483648L >= piece<<5:
                                dests.append(piece<<5)
                                jumped.append('')
                    elif root != 'ul' and bin(board[player]).count('1') - 1 != bin(board[player] - (piece<<5)).count('1') and bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece<<9)).count('1'):
                        if 2147483648L >= piece<<9:
                            if king_piece:
                                old_piece = piece
                                new_piece = piece<<9
                                jump_piece = piece<<5
                                [new_board,new_player] = after_move([old_piece,[new_piece,[jump_piece]]],[board,player])
                                [holder,new_dests,new_jumped] = find_moves(piece<<9,new_board,player,0,1,'dr')
                            else:
                                [holder,new_dests,new_jumped] = find_moves(piece<<9,board,player,0)
                            dests.extend(new_dests)
                            if new_dests == []:
                                dests.append(piece<<9)
                            if new_jumped != []:
                                if 1-fm:
                                    for i in range(0,len(new_jumped)):
                                        jumped.append([piece<<5,new_jumped[i]])
                                else:
                                    for i in range(0,len(new_jumped)):
                                        jumped.append([[piece<<5],[new_jumped[i]]])
                            elif fm:
                                jumped.append([piece<<5])
                            else:
                                jumped.extend([piece<<5])
                #up and right
                if bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece<<4)).count('1'):
                    if fm:
                        if 2147483648L >= piece<<4:
                            dests.append(piece<<4)
                            jumped.append('')
                elif root != 'ur' and col_mod(piece) != 0 and bin(board[player]).count('1') - 1 != bin(board[player] - (piece<<4)).count('1') and bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece<<7)).count('1'):
                    if 2147483648L >= piece<<7:
                        if king_piece:
                            old_piece = piece
                            new_piece = piece<<7
                            jump_piece = piece<<4
                            [new_board,new_player] = after_move([old_piece,[new_piece,[jump_piece]]],[board,player])
                            [holder,new_dests,new_jumped] = find_moves(piece<<7,new_board,player,0,1,'dl')
                        else:
                            [holder,new_dests,new_jumped] = find_moves(piece<<7,board,player,0)
                        dests.extend(new_dests)
                        if new_dests == []:
                            dests.append(piece<<7)
                        if new_jumped != []:
                            if 1-fm:
                                for i in range(0,len(new_jumped)):
                                    jumped.append([piece<<4,new_jumped[i]])
                            else:
                                for i in range(0,len(new_jumped)):
                                    jumped.append([[piece<<4],[new_jumped[i]]])
                        elif fm:
                            jumped.append([piece<<4])
                        else:
                            jumped.extend([piece<<4])



    if player == 1 or (player == 0 and king_piece == 1): #computer (or p2) xor king
        if 0 < piece: #make sure piece not smaller than board
            if row_mod(piece) == 0: #check which row piece is on (odd in this case)
                #down and right
                if bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece>>4)).count('1'):
                    if fm:
                        if 0 < piece>>4:
                            dests.append(piece>>4)
                            jumped.append('')
                elif root != 'dr' and col_mod(piece) != 0 and bin(board[player]).count('1') - 1 != bin(board[player] - (piece>>4)).count('1') and bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece>>9)).count('1'):
                    if 0 < piece>>9:
                        if king_piece:
                            old_piece = piece
                            new_piece = piece>>9
                            jump_piece = piece>>4
                            [new_board,new_player] = after_move([old_piece,[new_piece,[jump_piece]]],[board,player])
                            [holder,new_dests,new_jumped] = find_moves(piece>>9,new_board,player,0,1,'ul')
                        else:
                            [holder,new_dests,new_jumped] = find_moves(piece>>9,board,player,0)
                        dests.extend(new_dests)
                        if new_dests == []:
                            dests.append(piece>>9)
                        if new_jumped != []:
                            if 1-fm:
                                for i in range(0,len(new_jumped)):
                                    jumped.append([piece>>4,new_jumped[i]])
                            else:
                                for i in range(0,len(new_jumped)):
                                    jumped.append([[piece>>4],[new_jumped[i]]])
                        elif fm:
                            jumped.append([piece>>4])
                        else:
                            jumped.extend([piece>>4])
                if col_mod(piece) != 3: #make sure not left edge
                    #down and left
                    if bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece>>3)).count('1'):
                        if fm:
                            if 0 < piece>>3:
                                dests.append(piece>>3)
                                jumped.append('')
                    elif root != 'dl' and bin(board[player]).count('1') - 1 != bin(board[player] - (piece>>3)).count('1') and bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece>>7)).count('1'):
                        if 0 < piece>>7:
                            if king_piece:
                                old_piece = piece
                                new_piece = piece>>7
                                jump_piece = piece>>3
                                [new_board,new_player] = after_move([old_piece,[new_piece,[jump_piece]]],[board,player])
                                [holder,new_dests,new_jumped] = find_moves(piece>>7,new_board,player,0,1,'ur')
                            else:
                                [holder,new_dests,new_jumped] = find_moves(piece>>7,board,player,0)
                            dests.extend(new_dests)
                            if new_dests == []:
                                dests.append(piece>>7)
                            if new_jumped != []:
                                if 1-fm:
                                    for i in range(0,len(new_jumped)):
                                        jumped.append([piece>>3,new_jumped[i]])
                                else:
                                    for i in range(0,len(new_jumped)):
                                        jumped.append([[piece>>3],[new_jumped[i]]])
                            elif fm:
                                jumped.append([piece>>3])
                            else:
                                jumped.extend([piece>>3])
            else: #even row
                if col_mod(piece) != 0: #make sure not right edge
                    #down and right
                    if bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece>>5)).count('1'):
                        if fm:
                            if 0 < piece>>5:
                                dests.append(piece>>5)
                                jumped.append('')
                    elif root != 'dr' and bin(board[player]).count('1') - 1 != bin(board[player] - (piece>>5)).count('1') and bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece>>9)).count('1'):
                        if 0 < piece>>9:
                            if king_piece:
                                old_piece = piece
                                new_piece = piece>>9
                                jump_piece = piece>>5
                                [new_board,new_player] = after_move([old_piece,[new_piece,[jump_piece]]],[board,player])
                                [holder,new_dests,new_jumped] = find_moves(piece>>9,new_board,player,0,1,'ul')
                            else:
                                [holder,new_dests,new_jumped] = find_moves(piece>>9,board,player,0)
                            dests.extend(new_dests)
                            if new_dests == []:
                                dests.append(piece>>9)
                            if new_jumped != []:
                                if 1-fm:
                                    for i in range(0,len(new_jumped)):
                                        jumped.append([piece>>5,new_jumped[i]])
                                else:
                                    for i in range(0,len(new_jumped)):
                                        jumped.append([[piece>>5],[new_jumped[i]]])
                            elif fm:
                                jumped.append([piece>>5])
                            else:
                                jumped.extend([piece>>5])
                #down and left
                if bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece>>4)).count('1'):
                    if fm:
                        if 0 < piece>>4:
                            dests.append(piece>>4)
                            jumped.append('')
                elif root != 'dl' and col_mod(piece) != 3 and bin(board[player]).count('1') - 1 != bin(board[player] - (piece>>4)).count('1') and bin(sum(board[:2])).count('1') - 1 != bin(sum(board[:2]) - (piece>>7)).count('1'):
                    if 0 < piece>>7:
                        if king_piece:
                            old_piece = piece
                            new_piece = piece>>7
                            jump_piece = piece>>4
                            [new_board,new_player] = after_move([old_piece,[new_piece,[jump_piece]]],[board,player])
                            [holder,new_dests,new_jumped] = find_moves(piece>>7,new_board,player,0,1,'ur')
                        else:
                            [holder,new_dests,new_jumped] = find_moves(piece>>7,board,player,0)
                        dests.extend(new_dests)
                        if new_dests == []:
                            dests.append(piece>>7)
                        if new_jumped != []:
                            if 1-fm:
                                for i in range(0,len(new_jumped)):
                                    jumped.append([piece>>4,new_jumped[i]])
                            else:
                                for i in range(0,len(new_jumped)):
                                    jumped.append([[piece>>4],[new_jumped[i]]])
                        elif fm:
                            jumped.append([piece>>4])
                        else:
                            jumped.extend([piece>>4])
        
    check_jumps = 0
    for i in range(0,len(dests)):
        if jumped[i] != '':
            check_jumps = 1
    if fm and check_jumps:
        final_dests = []
        final_jumped = []
        for i in range(0,len(dests)):
            if jumped[i] != '':
                final_dests.append(dests[i])
                final_jumped.append(jumped[i])
    else:
        final_dests = dests
        final_jumped = jumped
            
    return [piece,final_dests,final_jumped]
