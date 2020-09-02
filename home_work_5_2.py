#Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)

#n=int(input('Enter the value of "N" number: '))
#f=1
#while n > 1:
#    f = f*n
#    n -= 1
#print(f)


#n=int(input('Enter the value of "N" number: '))
#f=1
#for i in range(1,n+1):
#    f *= i
#print(f)


def f(n):
    if n == 0:
        return 1
    return f(n-1)*n

print(f(7))