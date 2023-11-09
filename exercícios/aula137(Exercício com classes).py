# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

motor1 = Motor('Motor bom')
motor2 = Motor('Motor ruim')

fabricante1 = Fabricante('Fabricante bom')
fabricante2 = Fabricante('Fabricante ruim')

carro1 = Carro('Carro bonito', motor2, fabricante2)
carro2 = Carro('Carro feio', motor1, fabricante1)
# fabricante1 = Fabricante('Fabricante bom')

# print('motor do carro 1:', motor1.nome)
print('carro 1 tem as seguintes informações:')
print('nome:', carro1.nome)
print('motor:', carro1.motor.nome)
print('fabricante:', carro1.fabricante.nome)
print()
print('carro 2 tem as seguintes informações:')
print('nome:', carro2.nome)
print('motor:', carro2.motor.nome)
print('fabricante:', carro2.fabricante.nome)