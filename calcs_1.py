# calcs simple with if elif else

operator = input("Enter either +, -, *, %, //, or divide: ")
number_1 = float(input("Enter First Number: "))
number_2 = float(input("Enter Second Number: "))

if operator == '+':
    print(number_1 + number_2)
elif operator == '-':
    print(number_1 - number_2)
elif operator == '*':
    print(number_1 * number_2)
elif operator == '%':
    print(number_1 % number_2)
elif operator == '//':
    print(number_1 // number_2)
elif operator == '/':
    print(number_1 / number_2)
else:
    print('Invalid operator')





