#Is the string uppercase?
#Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

def is_uppercase(inp):
    return False if not inp.isupper() else True

# def is_uppercase(inp):
#     return inp.isupper()

print(is_uppercase("c")) 
print(is_uppercase("C")) 
print(is_uppercase("hello I AM DONALD")) 
print(is_uppercase("HELLO I AM DONALD")) 
print(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"))