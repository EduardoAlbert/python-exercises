def registry(name='', goals=''):
    if name == '':
        name = '<desconhecido>'
    if not goals.isnumeric():
        goals = 0

    print(f'O jogador {name} fez {goals} gol(s) no campeonato.')


# Main Program
namePlayer = str(input('Nome do Jogador: '))
numGoals = str(input('Número de Gols: '))

registry(namePlayer, numGoals)
