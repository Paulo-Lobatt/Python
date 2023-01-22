numero = input('digite um número inteiro: ')

try:
    numero = int(numero)

    if numero % 2 == 0:
        print('sla')
    else:
        print('ímpar')
except:
        print('não é um número inteiro')





"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""