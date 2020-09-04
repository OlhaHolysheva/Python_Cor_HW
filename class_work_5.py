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



#В інтервалі від 1 до 10 визначити числа 
# - парні, які діляться на 2,
# - непарні, які діляться на 3, 
# - числа, які не діляться на 2 та 3.

#for i in range(1,11):
#    if i % 2 == 0:
#        print(i)

#for i in range(1,10):  
#    if i % 3 == 0 and not i % 2 == 0:
#        print(i)

#for i in range(1,11):
#    if not i % 2 == 0 and not i % 3 == 0:
#        print(i)


for i in range(1,11):
    if i % 2 != 0 and i % 3 != 0:
        print(i)



#Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)

n=int(input('Enter the value of "N" number: '))
f=1
while n > 1:
    f = f*n
    n -= 1
print(f)


n=int(input('Enter the value of "N" number: '))
f=1
for i in range(1,n+1):
    f *= i
print(f)


#def f(n):
#    if n == 0:
#        return 1
#    return f(n-1)*n

#print(f(7))


#Напишіть скрипт, який перевіряє логін, який вводить користувач. 
#Якщо логін вірний (“First”), то привітайте користувача. 
#Якщо ні, то виведіть повідомлення про помилку. (необхідно використати цикл while)

login = str(input('Enter your login: '))

while login != "First":
    print("Invalid login!")
    login = str(input('Enter your login: '))
   #break
        
else:
    print("Successful validation!")