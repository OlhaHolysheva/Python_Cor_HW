#Знаходимо добуток цифр в числі
n=1292
dob_n=1
while n>0:
    element=n%10 
    dob_n=dob_n*element
    n=n//10
print(dob_n)

#n=abs(int(input("Enter your number:")))
#dob_n=1
#if n==0:
#    dob_n=0
#while n>0:
#    element=n%10
#    if element!=0:
#        dob_n+=element
#       n=n//10

#print(dob_n)