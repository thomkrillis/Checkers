# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Reverse Map 

def reverse_map(bit):
    from math import log
    from row_mod import row_mod
    from col_mod import col_mod

    rm = row_mod(bit)
    cm = col_mod(bit)

    pos = log(bit)/log(2)

    j = int(pos/4) + 1
    i = 2*(4-cm) - (1-rm)

    return [i,j]

