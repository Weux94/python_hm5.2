user_request = input('If you need calculator enter Y if no enter NO ')

while user_request == 'Y':
    user_num1 = int(input('Введите первое число '))
    user_num2 = int(input('Введите второе число '))
    user_digit = input('Введите знак ')

    if user_digit == '+':
        print(user_num1 + user_num2)
        user_request = input('If you need calculator enter Y if no enter NO ')
    elif user_digit == '-':
        print(user_num1 - user_num2)
        user_request = input('If you need calculator enter Y if no enter NO ')
    elif user_digit == '*':
        print(user_num1 * user_num2)
        user_request = input('If you need calculator enter Y if no enter NO ')
    elif user_digit == '/' and user_num2 != 0:
        print(user_num1 / user_num2)
        user_request = input('If you need calculator enter Y if no enter NO ')
    else:
        print('Invalid input')
        break
