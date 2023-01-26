nome = 'paulo'
# tamanho = len(nome)
cont = 0
novo_nome = ''

while cont < len(nome):
    letra = nome[cont]
    novo_nome += f'*{letra}'
    cont += 1
    

novo_nome += '*'
print(novo_nome)


