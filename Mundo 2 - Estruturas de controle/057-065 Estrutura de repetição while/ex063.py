n = int(input('Mostrar Quantos elementos da sequência de Fibonacci: '))

ctrl = 1
anterior = 0
num = 1

while ctrl <= n:
    somaAnterior_Num = anterior + num
    print(anterior, end=' ')
    anterior = num
    num = somaAnterior_Num
    ctrl += 1
