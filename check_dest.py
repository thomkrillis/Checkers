# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Check Dest

def check_dest(dest,dests,jump_chain,piece,board,com=0):
    double = 0
    jumped = []
    if any(dest == i for i in dests):
        for i in range(0,len(dests)):
            if dests[i] == dest:
                from math import log

                jumped.append(jump_chain[i])
                double = double + 1
        if double > 1:
            if com:
                from random import choice
                i = choice(range(0,double))
                dest = dests[i]
                jumped = jump_chain[i]
            else:
                from reverse_map import reverse_map
                #multiple paths to same destination
                print "Multiple posible paths"
                print "Please specify which pieces you are jumping"
                print jumped
                for i in range(0,double):
                    map_jump = []
                    for j in range(0,len(jumped[i])):
                        map_jump.append(reverse_map(jumped[i][j]))
                    print "Move " + str(i) + ": " + str(map_jump)
                i = input('Choice: ')
                dest = dests[i]
                jumped = jump_chain[i]
            
        return [dest,jumped]
    else:
        from map_input import map_input
        from check_input import check_input
        from check_free import check_free
        return check_dest(check_free(map_input(check_input(input('Not a valid destination, try again: '))),board),dests,jump_chain,piece,board);
