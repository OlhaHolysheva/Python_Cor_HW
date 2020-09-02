#Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for)

#i=0
#while i<100:
#    if i%2 == 0:
#        print(i)
#    i+=1

#for i in range(101):
#    if i%2 == 0:
#        print(i)

#for i in range(0,101,2):
#    print(i)

print(list(range(0,101,2)))