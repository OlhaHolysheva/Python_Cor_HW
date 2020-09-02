#Напишіть скрипт, який перевіряє логін, який вводить користувач. 
#Якщо логін вірний (“First”), то привітайте користувача. 
#Якщо ні, то виведіть повідомлення про помилку. (необхідно використати цикл while)

login = str(input('Enter your login: '))

while login != "First":
    print("Invalid login!")
    login = str(input('Enter your login: '))
   #break
    #login = str(input('Enter your login: '))
    
else:
    print("Successful validation!")