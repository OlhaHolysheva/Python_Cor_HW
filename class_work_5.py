#Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

#n = input('Enter the number of elements in your list: ')
#n = int(n)

#my_list = []
#for i in range(n):
#    el = int(input('Enter the number: '))
#    my_list.append(el)
#print(my_list)
#
#max_el = my_list[0]
#min_el = my_list[0]
#
#for i in range(n):
#    if my_list[i] > 0:
#        max_el = my_list[i]
#    if my_list[i] < 0:
#        min_el = my_list[i]
#
#print('Maximum number is: %d. Minimum number is: %d.' %(max_el,min_el))
#print('Maximum number is: {}. Minimum number is: {}. '.format(max_el,min_el))


#list_2 = [int(input('Enter the number: ')) for i in range(int(input('Enter the amount of elements in your list: ')))]
list_2 = [int(input('Enter the {} number: '.format(i+1)) for i in range(int(input('Enter the amount of elements in your list: '))))]
print(list_2)

#print('Maximum number is: {}. Minimum number is: {}'.format(max(list_2),min(list_2))