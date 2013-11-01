# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Row Mod (returns 0 or 1 whether row is odd or even)

def row_mod(piece):
    from math import log
    
    return int(log(piece)/log(2))/4%2
