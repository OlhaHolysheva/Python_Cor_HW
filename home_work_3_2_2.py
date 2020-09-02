#Міняємо цифри місцями
n_1=input("Enter your namber: ")
n_list=list(n_1)
n_list.reverse()
n_2=" ".join(n_list)
print("Reversed number is: ", n_list)

#n_1=input("Enter your namber: ")
#n_0=0
#while n1>0:
#    element=n_1%10
#    n_1=n_1//10
#    n_2=n_2*10
#    n_2=n_2+element
#print(n_2)