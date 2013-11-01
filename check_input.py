# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Check Input

def check_input(square):
    if sum(square) % 2 == 1 or square[0] < 1 or square[0] > 8 or square[1] < 1 or square[1] > 8:
        return check_input(input('Invalid square, choose again: '))
    else:
        return square
