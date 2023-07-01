valor = 0

def mult(*args):
    global valor
    total = 1
    for num in args:
        total *= num
    valor = total
    return valor
  

mult(11, 3)


def impar(n):
    if(n % 2 == 0):
        print('é par')
    else:
        print('é impar')


impar(valor)