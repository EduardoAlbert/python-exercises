print('='*30)
print('     10 TERMOS DE UMA P.A')
print('='*30)

primeiroTermo = int(input('Digite o Primeiro Termo da P.A: '))
razao = int(input('Razão: '))
termos = primeiroTermo
ctrl = 1
while ctrl <= 10:
    print('{}'.format(termos), end=' ➡ ')
    termos += razao
    ctrl += 1
print('ACABOU')
