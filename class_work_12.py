#Rewrite the following code through using the map function. 
# The function takes a list of real names and replaces them with the appropriate 
# hash combinations using the hashing method.

# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names) 

########################################################

# names = ['Sam', 'Don', 'Daniel']
# hashed_names = list(map(hash,names))
# print(hashed_names)

#Display a list of list items that have the values ​​"red", 
# ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", “yellow”] 
# using the filter function.

# colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]

# filtered_colors = list(filter(lambda n: n == "red", colors))
# print(filtered_colors)

#All these numbers in the list have a string data type, for example 
# ['1', '2', '3', '4', '5', '7'], convert this list to a list, 
# all numbers of which have the data type integer : 1) using the append method 
# 2) using the map method

# number_list = ['1', '2', '3', '4', '5', '7']
# number_list_int = []
# for i in number_list:
#     number_list_int.append(int(i))

# print(number_list_int)

# ############################
# number_list = ['1', '2', '3', '4', '5', '7']
# number_list_int = map(int, number_list)

# print(list(number_list_int))

#Convert list containing miles to list containing kilometers (1 mile = 1.6 kilometers) 
# a) using the map function b) using the map and lambda function 

# def convert_m_to_km(num_miles):
#     return round(num_miles * 1.6, 2)

# miles_list = [1,2,3,4,5,6]
# kilometers_list = list(map(convert_m_to_km, miles_list))
# print(kilometers_list)

#################################################################

# miles_list = [1,2,3,4,5,6]
# kilometers_list = list(map(lambda x: round(x*1.6, 2), miles_list))
# print(kilometers_list)

#Find the largest item in the list using the reduce function 

# number_list = [1,2,3,4,5,6]
# from functools import reduce

# result = reduce(lambda x,y: x + y, number_list)
# print(result)

#####################################
# number_list = [1,2,3,4,5,6]
# from functools import reduce

# max_el = reduce(lambda x,y: x if (x > y) else y, number_list)
# print(max_el)

#Create a simple generator function similar to the range iterator.

def my_range(first, second, step):
    number=first
    while (number<second):
        yield number
        number += step

def main():
    for i in my_range(5, 25, 3):
        print(i)

    print("-------------")

    generator = my_range(1, 10, 1)
    try:
        while True:
            print("generator: ", next(generator))
    except StopIteration:
        print("-------------")
        print("Stop program")
if __name__ == '__main__':
    main()

###########################################################

g = (x*x for x in range(1,10))   #генератор списку
print(g)


#Using several decorators, create a sandwich consisting of lettuce, tomatoes and meat. 
# <\ ^^^^^^^ /> 
# tomato #
# --meat– 
# ~ salad ~
# <\ ______ />

# def bread(func):
#     def wrapper():
#         print("<\^^^^^^^/>")
#         func()
#         print("<\______/>")
#     return wrapper

# def ingredients(func):
#     def wrapper():
#         print("#tomatos#")
#         func()
#         print("~salad~")
#     return wrapper

# # def sandwich(food="--meat--"):
# #     print(food)

# # sandwich = bread(ingredients(sandwich)

# # sandwich()
# ###########################або
# @bread
# @ingredients
# def sandwich(food="--meat--"):
#     print(food)

# sandwich()
