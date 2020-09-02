#Reversing Words in a String

#def reverse(st):
#    return st[::-1]

#print(reverse("OLGA"))    


#def reverse(st):
#   return reversed(st.split(st))
#print(reverse('Hello World'))

def reverse(st):
    a = st.split()
    a = list(a[::-1])
    return (' '.join(a))

print(reverse('Hello World'))