#def bool_to_word(boolean):
#    if boolean == True:
#        return 'Yes'
#    else:
#        return 'No'

#print(bool_to_word(True))

#def bool_to_word(boolean):
#    return "Yes" if boolean else "No"
#
#print(bool_to_word(True))

def bool_to_word(bool):
    return ['No', 'Yes'][bool]
print(bool_to_word(False))