print('='*30)
print('     10 TERMOS DE UMA P.A')
print('='*30)

primeiroTermo = int(input('Digite o Primeiro Termo da P.A: '))
razao = int(input('Razão: '))
decimo = primeiroTermo + (10-1) * razao
x = 0
for i in range(primeiroTermo, decimo+razao, razao):
    x += 1
    print(i, end=' ➡ ️')
    if x == 10:
        break
print('ACABOU')
