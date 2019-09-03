print('='*30)
print('     10 TERMOS DE UMA P.A')
print('='*30)

termos = int(input('Digite o Primeiro Termo da P.A: '))
razao = int(input('Razão: '))

total = 0
ctrl = 1
maisTermos = 10
while maisTermos != 0:
    total += maisTermos
    while ctrl <= total:
        print('{}'.format(termos), end=' ➡ ')
        termos += razao
        ctrl += 1
    print('PAUSA')
    maisTermos = int(input('Quer mostrar mais quantos termos? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
