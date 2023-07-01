# def dup(n):
#     return n * 2

# def tri(n):
#     return n * 3

# def qua(n):
#     return n * 4


# duplicar = dup(20)
# print(duplicar)
# triplicar = tri(20)
# print(triplicar)
# quadriplicar = qua(20)
# print(quadriplicar)

#solução

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))