#Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

# def create_array(n):
#     res=[]
#     i=1
#     while i<=n: res+=[i]
#     return res

def create_array(n):
    res = []   
    i = 1
    while i <= n: 
        res += [i]
        i += 1
    return res


# 

# def create_array(n):
#     return [i for i in range(1,n+1)]

# def create_array(n):
#     res=[]
#     for a in range(0,n):
#         res.append(a+1)
#     return res

print(create_array(5))