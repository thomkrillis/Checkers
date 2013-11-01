# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Col Mod (returns 0 for right-most pair of columns, 3 for leftmost, etc.)

def col_mod(piece):
    from math import log
    
    return int(log(piece)/log(2))%4
