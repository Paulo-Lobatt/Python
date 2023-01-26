import os

os.system('cls')

try:
    lista = []

    while True:
        print('[I]nserir [A]pagar [L]istar   ')
        R = input('escolha uma opção: ').strip().upper()
        R = R[0]
        
        if 'I' in R:
            os.system('cls')
            valor = input('valor: ')
            lista.append(valor)
        elif 'A' in R:
            valor = input('escolha o indice para apagar: ')
            if valor in lista:
                lista.remove(valor)
            else:
                print('não foi possível apagar esse indice')
        elif 'L' in R:
            os.system('cls')
            if len(lista) <= 0:
                print('não há nada para listar')
            for item in enumerate(lista):
                num, name = item
                print(num, name)
        else:
            print('escolha uma opção válida')
except:
    print('erro')
    