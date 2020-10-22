# Завдання2.3
# Користувачем з клавіатури вводяться 2 натуральних числа. Треба з’ясувати, чи є задані числа взаємно простими.

while True:
    try:
        number1 = int (input("Введіть натуральне число: "))
       		number1 != 1, "Одиниця не розглядається в контексті простих чисел"
        if number1 >= 2:
       
        else:
       ("Введене число має бути натуральним!")
    except ValueError:
       дьте уважні - вводіть лише числа!") 
    except AssertionError as ae:
       
while True:
    try
        number2 = int (input("Введіть натуральне число: "))
       mber2 != 1, "Одиниця не розглядається в контексті простих чисел"
        if number2 >= 2:
       
        else:
       ("Введене число має бути натуральним!")
    except ValueError:
       дьте уважні - вводіть лише числа!") 
finally:
  print("");
    except AssertionError as ae:
        print(ae)

flag = False
if number2 > number1:
    tmp = number1
    number1 = number2
    number2 = tmp
     number1, number2 = number2, number1
if number1 % number2 == 0:
    flag = True
else:
    if number % 2 == 0:
        flag = True
    else:
        divisor = 3
        while divisor <= number1//2: # while divisor <= int(number**(1/2)):
            if number1 % divisor == 0:
                if number2 % divisor == 0:
                    flag = True
                    break
            divisor = divisor + 2
if flag:
    print ("Числа не є взаємно простими")
else:
    print("Числа є взаємно простими")