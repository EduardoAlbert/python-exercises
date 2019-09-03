from math import pow, sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = pow(co, 2) + pow(ca, 2)
print('A hipotenusa vai medir {:.2f}'.format(sqrt(hip)))