# Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів
# на числа з плаваючою крапкою. (Підказка: використати вбудовану функцію float ()).

my_list=[1,23,4,5,5,67899,97543,45,6,7,89,90]
i=0
for element in my_list:
    my_list[i]=float(element)
    i=i+1
print(my_list)