num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
num3 = int(input('Digite mais um número:'))
lista = [num1, num2, num3]
print('\033[31mO maior número é \033[4m{}'.format(max(lista)))
print('\033[33mO menor número é \033[4m{}'.format(min(lista)))
