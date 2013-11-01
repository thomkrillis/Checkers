# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Main

from printboard import printboard
from map_input import map_input
from check_input import check_input
from check_owner import check_owner
from show_all_moves import show_all_moves
from show_moves import show_moves
from check_dest import check_dest
from check_free import check_free
from check_all_moves import check_all_moves
from flatten import flatten
from row_mod import row_mod
from col_mod import col_mod
from became_king import became_king

import numpy
from numpy import linalg
import re
import itertools
from random import choice
from time import sleep

#NEED TO INDICATE WHICH PIECES ARE KINGS

#NEED TO ADD AI                                     (mad hard)
#NEED TO ADD GRAPHICS COLOURS                       (medium)

#NEED TO REMOVE CHECK_MOVE file
#need to update check_input to make sure it receives two ints

board_player1 = 0b00000000000000000000111111111111;
board_player2 = 0b11111111111100000000000000000000;
board_kings   = 0b00000000000000000000000000000000;

#board_player1 = 0b00000000000001000000000000000000;
#board_player2 = 0b00000000010000000000000000000000;
#board_kings   = 0b00000000000000000000000000000000;

board = [board_player1, board_player2, board_kings]

printboard(board)

#board_matrix = re.findall('....', format(board[0]+2*board[1], '#034b'))
#board_matrix = re.findall('....',re.sub('('str(int(bin(board[0])[2:].zfill(32)) + 2 * int(bin(board[1])[2:].zfill(32)))))

time = 0
player = 0 #0 indicates black (bottom), 1 is red (top)
king = 2
turn = 0 #indicate which turn it is
two_pl = raw_input('Two player game? (y/n)') == 'y'
if two_pl:
    self = 0
else:
    random = raw_input('Should computer play randomly? (y/n)') == 'y'
    self = raw_input('Should computer play itself? (y/n)') == 'y'

while bin(board[0]).count('1') != 0 and bin(board[1]).count('1') != 0:
    print "Turn: " + str(turn)
    if self:
        #make computer play itself
        if random:
            sleep(time)
            print "Computer " + str(player+1) + " is looking at its options."
            all_pieces = show_all_moves(board,player)
            sleep(time)
            print "It's picked a piece..."
            [piece,dests,jumped] = show_moves(choice(all_pieces),board,player)
            for i in range(0,len(jumped)):
                jumped[i] = flatten(jumped[i])
            [dest,jumped] = check_dest(choice(dests),dests,jumped,piece,board,1)
            sleep(time)
            print "And now it's moved:"
        else:
            print "Do AI, dumby"
    elif player == 0: #player's turn
        print "Player 1's turn."
        show = raw_input('Show all possible moves? (y/n)') == 'y'
        if show:
            show_all_moves(board,player)
        [piece,dests,jumped] = show_moves(check_owner(map_input(check_input(input('Choose piece to move: '))),board,player),board,player);
        for i in range(0,len(jumped)):
            jumped[i] = flatten(jumped[i])
        [dest,jumped] = check_dest(check_free(map_input(check_input(input('Choose piece destination: '))),board),dests,jumped,piece,board);
        print "Player 1 moved:"

    else: #computer's turn or 2nd players turn
        if two_pl:
            print "Player 2's turn."
            show = raw_input('Show all possible moves? (y/n)') == 'y'
            if show:
                all_pieces = show_all_moves(board,player)
            [piece,dests,jumped] = show_moves(check_owner(map_input(check_input(input('Choose piece to move: '))),board,player),board,player);
            if piece == []:
                print "PLAYER 1 WINS!!one!1!"
                break
            for i in range(0,len(jumped)):
                jumped[i] = flatten(jumped[i])
            [dest,jumped] = check_dest(check_free(map_input(check_input(input('Choose piece destination: '))),board),dests,jumped,piece,board);
            print "Player 2 moved:"
        else:
            if random:
                sleep(time)
                print "The computer is looking at its options."
                all_pieces = show_all_moves(board,player)
                sleep(time)
                print "It's picked a piece..."
                [piece,dests,jumped] = show_moves(choice(all_pieces),board,player)
                for i in range(0,len(jumped)):
                    jumped[i] = flatten(jumped[i])
                [dest,jumped] = check_dest(choice(dests),dests,jumped,piece,board,1)
                sleep(time)
                print "And now it's moved:"
            else:
                print "Do AI, dumby"

    #if piece was king
    if bin(board[king]).count('1') - 1 == bin(board[king] - (piece)).count('1'):
        #update king position
        board[king] = board[king]-piece+dest
    else:
        #check if piece became king
        if became_king(dest,board,player):
            board[king] = board[king]+dest

    #update board
    board[player] = board[player]-piece+dest
    if len(jumped) == 1:
        jumped = flatten(jumped)
    if jumped != []:
        for i in range(0,len(jumped)):
            board[1-player] = board[1-player] - jumped[i]
            #if jumped piece was king
            if bin(board[king]).count('1') - 1 == bin(board[king] - (jumped[i])).count('1'):
                #update king position
                board[king] = board[king]-jumped[i]
    printboard(board)        

    if bin(board[0]).count('1') == 0:
        print "PLAYER 2 WINS!!1!one!!"
        break
    if bin(board[1]).count('1') == 0:
        print "PLAYER 1 WINS!!one!1!"
        break

    turn = turn + 1
    player = player ^ 1 #switch players

    [check_pieces,check_dests] = check_all_moves(board,player)
    if check_pieces == []:
        print "PLAYER " + str(2-player) + " WINS!!one!1!"
        break

#might want to check that selected piece can move anywhere
#prob best to give option to check_move to change piece selection or show all possible moves if move already chosen not valid
# like this piece = rechoose(showmoves(check_owner(map_input(check_input(input('Choose piece to move: '))),board,player)));
# where show_moves does some check_move thing that returns all moves as some symbol (using printboard with extra param)

#show board in binary representation
#print format(board, '#034')
