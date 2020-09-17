# def summation(num):
#     sum = 0
#     for x in range (1,num+1):
#         sum = sum + x 
#     return sum
      

# print(summation(2))

def summation(num):
    sum = 0
    while num > 0:
        sum += num
        num = num-1
    return sum
    
print(summation(2))


# def summation(num):
#     return (1+num) * num / 2

# def summation(num):
#     return sum(range(1,num+1))

# def summation(num):
#     return sum([x for x in xrange(num+1)])
    