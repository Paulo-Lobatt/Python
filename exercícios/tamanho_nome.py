nome = input('Qual é o seu primeiro nome? ')

Lnome = len(nome)

if Lnome <= 4:
    print('seu nome é curto')
elif Lnome <= 6:
    print('seu nome é médio')
else:
    print('seu nome é grande')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""