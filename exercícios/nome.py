nome = input('Qual é seu nome?'  )
idade = input('digite sua idade: ')

if nome != '' and idade != '':
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]} ')

    if ' ' in nome:
        print('seu nome contém espaço')
    elif ' ' not in nome:
        print('seu nome não contém espaço')
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primera letra do seu nome é {nome[0]}')
    print(f'a última letra do seu nome é {nome[-1]}')


else: {
    print('Desculpe, você deixou campos vazios')
}

# nome = input('Digite o seu nome: ')
# idade = input('Digite sua idade: ')

# if nome and idade:
#     print(f'Seu nome é {nome}')
#     print(f'Seu nome invertido é {nome[::-1]}')

#     if ' ' in nome:
#         print('Seu nome contém espaços')
#     else:
#         print('Seu nome NÃO contém espaços')

#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A última letra do seu nome é {nome[-1]}')
# else:
#     print("Desculpe, você deixou campos vazios.")