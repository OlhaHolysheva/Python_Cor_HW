#In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks. 
# The last person to take a stick wins. For example:

def make_move(sticks):
    step = sticks % 4
    return step



# import random
# def makeMove(sticks):
#     if sticks % 4 != 0:
#         return sticks % 4
#     else:
#         return random.randint(1, 3)
