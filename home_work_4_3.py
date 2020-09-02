#Перевірити чи список містить непарні числа.(Підказка: використати оператор break)
my_list=[1,2,3,4,7,8,9,34.566,236,876,980]
el=False
for i in my_list:
    if not i%2==0:
        el=True
    break
print(el)