print('\033[32m=-=\033[m'*10)
print('\033[31mAnalisador de Triângulos')
print('\033[32m=-=\033[m'*10)
r1 = float(input('\033[35mComprimento da reta 1:\n'))
r2 = float(input('\033[36mComprimento da reta 2:\n'))
r3 = float(input('\033[33mComprimento da reta 3:\n'))
dife = r1 - r2 - r3
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Sim! É possível formar um triângulo com essas retas!')
else:
    print('\033[31mNão! Não é possível formar um triângulo com essas retas!')
