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