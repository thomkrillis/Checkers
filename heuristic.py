# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Heuristic

def heuristic(state):
    board = state[0]
    player = state[1]

    #player = 1 - player #heuristic is backwards... don't ask
    king = 2

    pp = bin(board[player])[2:].count('1') #number of player pieces
    op = bin(board[1-player])[2:].count('1') #number of opponent pieces
    pk = 0 #number of player kings
    ok = 0 #number of opponent kings

    #count player kings
    pk = bin(board[player] & board[2]).count('1')
    ok = bin(board[1-player] & board[2]).count('1')

    #non-kings
    noking = []
    noking.append(board[0] - (board[0] & board[2]))
    noking.append(board[1] - (board[1] & board[2]))

    #count pieces on back wall (except kings)
    if player == 0:
        pb = bin(noking[0])[2:].zfill(32)[28:32].count('1') #player pieces on back wall
        ob = bin(noking[1])[2:].zfill(32)[0:4].count('1') #opponent pieces on back wall
    if player == 1:
        ob = bin(noking[0])[2:].zfill(32)[28:32].count('1') #opponent pieces on back wall
        pb = bin(noking[1])[2:].zfill(32)[0:4].count('1') #player pieces on back wall

    #count pieces on side wall (except kings)
    ps = bin(noking[player])[2:].zfill(32)[4::8].count('1') #number of player pieces on side walls
    os = bin(noking[1-player])[2:].zfill(32)[4::8].count('1') #number of opponent pieces on side walls
    ps = ps + bin(noking[player])[2:].zfill(32)[3::8].count('1') #number of player pieces on side walls
    os = os + bin(noking[1-player])[2:].zfill(32)[3::8].count('1') #number of opponent pieces on side walls

    #incentivize forward movement (except kings, and back row, sort of...)
    pfm = 0
    ofm = 0
    if player == 0:
        for i in range(0,6):
            pfm = pfm + (6-i) * bin(noking[0])[2:].zfill(32)[4*i:4*i+4].count('1')
            ofm = ofm + (i+1) * bin(noking[1])[2:].zfill(32)[4*i+8:4*i+12].count('1')
    if player == 1:
        for i in range(0,6):
            ofm = ofm + (6-i) * bin(noking[0])[2:].zfill(32)[4*i:4*i+4].count('1')
            pfm = pfm + (i+1) * bin(noking[1])[2:].zfill(32)[4*i+8:4*i+12].count('1')

    #incentivize kings to move toward centre
    kings = []
    kings.append(bin(board[0] & board[2])[2:].zfill(32))
    kings.append(bin(board[1] & board[2])[2:].zfill(32))
    pkc = kings[0][9:22:4].count('1') + kings[0][10:23:4].count('1') + kings[0][14:18:3].count('1')
    okc = kings[0][9:22:4].count('1') + kings[0][10:23:4].count('1') + kings[0][14:18:3].count('1')

    #when fewer pieces, make kings more desirable
    kingscale = 0
    if pp + op < 10:
        kingscale = 2

    #heuristic is all player's piece minus all opponent's pieces (kings count as 2.25 pieces, etc. 84 is above max values of fm's)
    h = pp - op + (1.25 + kingscale) * (pk - ok) + 0.75 * (pb - ob) + 0.5 * (ps - os) + 0.25 * (pfm - ofm)/84 + 0.5 * (pkc - okc)

    #if player is going to lose, it's REALLY undesirable
    if pp == 0:
        h = -100

    return h
