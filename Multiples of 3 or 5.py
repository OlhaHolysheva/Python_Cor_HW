#Multiples of 3 or 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

#Note: If the number is a multiple of both 3 and 5, only count it once. Also, 
# if a number is negative, return 0(for languages that


def solution(number):

    if number < 0:
        return 0

    sum_number = 0
    for i in range(1,number):
        if i % 3 == 0 or i % 5 == 0:
            sum_number = sum_number + i  
    return sum_number

print(solution(10))


# def f(x): return x%3 == 0 or x%5 == 0
# print(sum(filter(f, range(1, 10))))