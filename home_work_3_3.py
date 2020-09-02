#Поміняти між собою значення двох змінних, не використовуючи третьої змінної
a=input("Enter the first number: ")
b=input("Enter the second namber: ")
a,b=b,a
print(a)
print(b)