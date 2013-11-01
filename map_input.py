# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Map Input

def map_input(square):
    i = square[0];
    j = square[1];

    i = i - (i + 1) % 2;

    if i == 1:
        b = 0b1000
    elif i == 3:
        b = 0b0100
    elif i == 5:
        b = 0b0010
    elif i == 7:
        b = 0b0001

    return b << 4*(j-1)
