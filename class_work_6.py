 def ser_ar(*arg):
    return sum(arg)/len(arg)
 
print(ser_ar(1,2,3,4,5))


def max_number(*arg):
    '''This function return max element from numbers'''
    return max(arg)

print(max_number(2,3,4))


def max(num1,num2):
    """Function enter 2 variable and return the biggest one"""
    return num1 if num1 > num2 else num2


def max(x, y):
 	if x > y:
	return (x)
	else:
	return (y)
print( max(5, 6))


#Написати програму, яка обчислює площу прямокутника, трикутника та кола 
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)

def triangle(a,b,c):
    p = (a+b+c)/2
    from math import sqrt
    return sqrt(p*(p-a)*(p-b)*(p-c))

def rectangle(a,b):
    return a*b

def circle(r):
    from math import pi
    return pi * (r**2)

variant = int(input("Ener 1 if you wont to culculate the square of triangle, 2 - for rectangle and 3 - for circle "))
if variant == 1:
    A = int(input("enter the value of triangles side A: "))
    B = int(input("enter the value of triangles side B: "))
    C = int(input("enter the value of triangles side C: "))
    print(triangle(A,B,C))

elif variant == 2:
    A = int(input("enter the value of rectangle side A: "))
    B = int(input("enter the value of rectangle side B: "))
    print(rectangle(A,B))

elif variant == 3:
    R = int(input("enter the value of circle radius R: "))
    print(circle(R))
    


#Написати функцію, яка обчислює кількість символів, які входять в задану стрічку

def list_counter(my_list):
    resulte = {}
    for i in my_list:
        if i in resulte:
            continue
        else:
            resulte.update({str(i): my_list.count(i)})
    return resulte

a_list = str(input("Enter your string: "))

print(list_counter(a_list))


def count_symbol(word):
    '''Counting simbols in the words'''
    my_tuple_full = tuple(''.join(word.split()))
    my_dict = {symbol: my_tuple_full.count(symbol) for symbol in my_tuple_full}
    return my_dict


print(count_symbol("Hello word"))