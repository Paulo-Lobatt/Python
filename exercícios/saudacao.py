hora_atual = input('horário atual: ')

try:
    hora = int(hora_atual)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde')
    elif hora <= 23:
        print('boa noite')
    else:
        print('não conheço esse horário')
except:
    print('digite número inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""