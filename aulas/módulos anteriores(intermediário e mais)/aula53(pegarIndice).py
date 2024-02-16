"""
enumerate para enumerar valores de iteráveis (pegar índices))
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')


# cada monte de código faz a mesma coisa, mas a primeira opção seria a mais fácil e a melhor]

# eu faço uso do enumarete no exercício lista de compras

# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34613676#questions