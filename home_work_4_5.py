#Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
fib_1=1
fib_2=1
fib_1=fib_2
n=input("Enter the number of element in Fibonachi list")
n=int(n)

if n<2:
    quit()
print(fib_1, end=' ')
print(fib_2, end=' ')

for i in range (2,n):
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    print(fib_2, end=' ')

print()