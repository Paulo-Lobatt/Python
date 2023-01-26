try: 
    number1 = int(input('number one: '))
    number2 = int(input('number two: '))
    operator = input('digite o operador desejado: ')
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
           
        print('isso não é um operador')
    else:
        if operator == '+':
            print(f'{number1} + {number2} = {number1 + number2}')
        elif operator == '-':
            print(f'{number1} - {number2} = {number1 - number2}')
        elif operator == '*':
            print(f'{number1} * {number2} = {number1 * number2}')
        elif operator == '/':
            print(f'{number1} / {number2} = {number1 / number2}')
    
except:
    print('isso não é um número.')