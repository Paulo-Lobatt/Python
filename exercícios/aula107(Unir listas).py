# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]



def zipper(city, state):
    if len(city) != len(state):
        raise ValueError('As listas bla bla bla erro')
    
    city_and_states = []
    for i in range(len(city)):
        cidade = city(i)
        estado = state(i)   
        city_and_states.append(f'{cidade}, {estado}')

    return city_and_states

cidades = ['Salvador', 'Bahia', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']

city_and_states = zipper(cidades, uf)
print(city_and_states)