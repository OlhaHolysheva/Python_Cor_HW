#Double Char
#Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    return ''.join([i*2 for i in s])




print(double_char("String")) #"SSttrriinngg"