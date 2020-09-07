#Given an array of integers.
# Return an array, where the first element is the count of positives numbers 
# and the second element is sum of negative numbers.
#If the input array is empty or null, return an empty array.

# def count_positives_sum_negatives(arr):   
#     my_arr = []
#     positiv_count = 0
#     negativ_sum = 0
    
#     for i in arr:
#         if i > 0:
#             positiv_count += 1

#         elif i < 0:
#             negativ_sum += i

#     my_arr.append(positiv_count)
#     my_arr.append(negativ_sum)
    
#     if  not arr:
#         print([])
               
#     return my_arr

def count_positives_sum_negatives(arr):
        if not arr:
            return []
        pos = 0
        neg = 0
        for n in arr:
            if n > 0:
                pos = pos + 1
            else:
                neg = neg + n
        return [pos, neg]


# def count_positives_sum_negatives(arr):
#     return [] if not arr else [(count(x), sum(y)) for x, y in arr]

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
# print([arr[arr >= 0].size, arr[arr < 0].sum()])

print(count_positives_sum_negatives([]))
print(count_positives_sum_negatives([1]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0]))