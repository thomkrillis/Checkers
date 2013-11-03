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

    #count pieces on side wall (except kings)   SIDE WALL actually BAD???
    ps = bin(noking[player])[2:].zfill(32)[4:21:8].count('1') #number of player pieces on side walls
    os = bin(noking[1-player])[2:].zfill(32)[4:21:8].count('1') #number of opponent pieces on side walls
    ps = ps + bin(noking[player])[2:].zfill(32)[11:32:8].count('1') #number of player pieces on side walls
    os = os + bin(noking[1-player])[2:].zfill(32)[11:32:8].count('1') #number of opponent pieces on side walls

    #incentivize forward movement (except kings, and back row, sort of...)  THIS MIGHT BE GETTING SCALED DOWN TO ALMOST NOTHING...
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

    #force trades when ahead
    trade = 0
    if pp > op:
        trade = (12 - op) / 12
    if op > pp:
        trade = -((12 - pp) / 12)

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

    #2 kings to one king logic
    k2to1 = 0
    if pk == 2 and ok == 1:
        from reverse_map import reverse_map
        from math import log
        pkings = []
        for i in range(0,32):
            test_piece = 2**i
            if (board[player] & (test_piece)):
                pkings.append(test_piece)
            elif (board[1-player] & (test_piece)):
                oking = test_piece
        [ipk1,jpk1] = reverse_map(pkings[0])
        [ipk2,jpk2] = reverse_map(pkings[1])
        [iok,jok] = reverse_map(oking)
        k2to1 = -log((iok-ipk1)**2 + (iok-ipk2)**2 + (jok-jpk1)**2 + (jok-jpk2)**2) / 4
        if (iok <= 3 or jok >= 6) and ([ipk1,jpk1] == [1,7] or [ipk1,jpk1] == [2,8] or [ipk2,jpk2] == [1,7] or [ipk2,jpk2] == [2,8]):
            k2to1 = k2to1 + 1
        if (iok >= 6 or jok <= 3) and ([ipk1,jpk1] == [7,1] or [ipk1,jpk1] == [8,2] or [ipk2,jpk2] == [7,1] or [ipk2,jpk2] == [8,2]):
            k2to1 = k2to1 + 1
        if [ipk1,jpk1] == [1,1] or [ipk1,jpk1] == [8,8] or [ipk2,jpk2] == [1,1] or [ipk2,jpk2] == [8,8]:
            k2to1 = k2to1 - 5
        if [iok,jok] == [1,7] or [iok,jok] == [2,8]:
            k2to1 = k2to1 - 0.3
    elif ok == 2 and pk == 1:
        from reverse_map import reverse_map
        from math import log
        okings = []
        for i in range(0,32):
            test_piece = 2**i
            if (board[1-player] & (test_piece)):
                okings.append(test_piece)
            elif (board[player] & (test_piece)):
                pking = test_piece
        [iok1,jok1] = reverse_map(okings[0])
        [iok2,jok2] = reverse_map(okings[1])
        [ipk,jpk] = reverse_map(pking)
        k2to1 = log((ipk-iok1)**2 + (ipk-iok2)**2 + (jpk-jok1)**2 + (jpk-jok2)**2) / 4
        if (ipk <= 3 or jpk >= 6) and ([iok1,jok1] == [1,7] or [iok1,jok1] == [2,8] or [iok2,jok2] == [1,7] or [iok2,jok2] == [2,8]):
            k2to1 = k2to1 - 1
        if (ipk >= 6 or jpk <= 3) and ([iok1,jok1] == [7,1] or [iok1,jok1] == [8,2] or [iok2,jok2] == [7,1] or [iok2,jok2] == [8,2]):
            k2to1 = k2to1 - 1
        if [iok1,jok1] == [1,1] or [iok1,jok1] == [8,8] or [iok2,jok2] == [1,1] or [iok2,jok2] == [8,8]:
            k2to1 = k2to1 + 5
        if [ipk,jpk] == [1,7] or [ipk,jpk] == [2,8]:
            k2to1 = k2to1 + 0.3

    if pp + op == pk + ok:
        pb = 0
        ob = 0
        ps = 0
        os = 0
        pfm = 0
        ofm = 0
        pkc = 0
        okc = 0

    #heuristic is all player's piece minus all opponent's pieces (kings count as 2.25 pieces, etc. 84 is above max values of fm's)
    h = pp - op + (1.25 + kingscale) * (pk - ok) + 0.5 * (pb - ob) - 0.25 * (ps - os) + 0.25 * (pfm - ofm)/12 + (0.5 + 0.2 * kingscale) * (pkc - okc) + k2to1 + trade

    #if player is going to lose, it's REALLY undesirable
    if pp == 0:
        h = -100

    return h
