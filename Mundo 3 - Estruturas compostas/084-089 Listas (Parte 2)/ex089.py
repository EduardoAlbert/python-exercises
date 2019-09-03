todos = list()
aluno = list()
num = 0
mostraNotas = 0

while True:

    aluno.append(str(input('Nome do Aluno: ')))
    aluno.append(float(input('Nota1: ')))
    aluno.append(float(input('Nota2: ')))

    todos.append(aluno[:])
    aluno.clear()

    option = str(input('Quer continuar? [S|N] ')).upper().strip()[0]

    if option == 'N':
        break

print('-='*30)
print('No. NOME', ' '*9, 'MÉDIA')
print('-'*30)

for alunos in todos:

    print(f'{num:}   {alunos[0]:<14} '
          f'{(alunos[1] + alunos[2]) / 2}')

    num += 1

while True:

    print('-' * 30)

    mostraNotas = int(input('Mostrar nota de qual aluno? (999 interrompe): '))

    if mostraNotas != 999:
        print(f'Notas de {todos[mostraNotas][0]} são {todos[mostraNotas][1:]}')
    else:
        break

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

