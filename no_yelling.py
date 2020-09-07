#Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. 
#String should be capitalized and properly spaced. Using re and string is not allowed.


def filter_words(st):
    my_st = (" ".join(st.split())).capitalize()
    return my_st
    
# def filter_words(st):
#     lista = st.split()
#     string = ''
#     for i in lista:
#         if i == lista[0]:
#             i = i.capitalize()
#             string += i
#         else:
#             i = i.lower()
#             string += ' ' + i
#     return string

# def filter_words(st):
#     return st[0].upper() + " ".join([x.lower() for x in st[1:].split()])


print(filter_words('HELLO    world!'))