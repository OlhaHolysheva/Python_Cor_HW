# #Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне,
# #  врахувати випадок введення  некоректних даеих.

def is_even(number):
    try:
        return 'even number' if int(number)%2 else 'odd number'

    except  ValueError as e:
        print(e)

    except  TypeError as e:
        print(e)

print(is_even (input ("Enter an integer")))

# #Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
# # передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. 
# # Використати блоки else та finally.

try:
    num_1, num_2 = eval(input("Enter two numbers by a comma: "))
    divide_result = num_1 / num_2
    
    print("Resuld of dividing is: ", divide_result)

except ZeroDivisionError:
    print("Dividing by zero is error!!!")

except ValueError:
    print("Value errore!!!")

except SyntaxError:
    print("Comma is missing! Enter numbers separetly by a comma!")

except:
    print("Wrong input!")
    
else:
    print("No exceptions.")
    
finally:
    print("This is OK!")
    
#Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить 
# повідомлення про те чи вік є парним чи непарним числом. В програмі необхідно передбачити 
# можливість введення від’ємного числа, і в цьому випадку згенерувати виняткову ситуацію. 
# Головний код має викликати функцію, яка обробляє введену інформацію. 

def analiz_age(age):
    try:
        if int(age) <= 0:
            raise ValueError("That is not a positive number!")
        else:
            return 'Your age is an even  number' if int(age)%2 else 'Your age is an odd number'
    except ValueError as e: 
        print(e)

print(analiz_age(input("Enter your age: ")))

#Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

day_list = ["Mon", "Tue", "Wed", "Thu", "Frid", "Sat", "Sun"]

try:
    num = int(input("Enter the number in range from 1 to 7: "))
    if num <= 0 or num > 7:
        raise IndexError("Your number is out of range!")
    print(day_list[num - 1])                             # -1 бо інндексація починається з 0
except ValueError:
    print("Wrong input!")

#############################################################

day_dict = {
    1: "Mon",
    2: "Tue",
    3: "Wed",
    4: "Thu",
    5: "Frid", 
    6: "Sat",
    7: "Sun"
}
while True:
    try:
        num = int(input("Enter the number in range from 1 to 7: "))
    except ValueError:
        print("Wrong input!")
    else:
        print(day_dict.get(num, "There is no such a day of week!"))