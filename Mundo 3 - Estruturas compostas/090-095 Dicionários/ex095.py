dados = dict()
players = list()
golsPartida = list()

while True:
    dados.clear()   # Dicionário dados é resetado

    dados['Nome'] = str(input('Nome do Jogador: '))   # Dicionário recebe nome do jogador
    numPartidas = int(input(f"Quantas partidas {dados['Nome']} jogou? "))   # Variável guarda o número de partidas

    golsPartida.clear()     # Lista de gols é resetada
    for partidas in range(0, numPartidas):  # Para cada partida

        golsPartida.append(int(input(f'Quantos gols na partida {partidas}? ')))    # Quantos gols na partida

    dados['Gols'] = golsPartida[:]    # Dicionário dados recebe a lista com os gols p/partida
    dados['Total'] = sum(golsPartida)   # Dicionário dados recebe o soma de todos os gols

    players.append(dados.copy())    # Uma lista recebe uma cópia do dicio dados

    option = str(input('Quer continuar? [S|N]')).strip().upper()[0]     # Opção para continuar ou não

    while option not in 'SN':

        print('ERRO! Digite apenas S ou N.')
        option = str(input('Quer continuar? [S|N]')).strip().upper()[0]

    if option == 'N':
        break           # Se 'N' como resposta, o While para

print('-='*30)
print('cod ', end='')

for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)

for pos, player in enumerate(players):

    print(f'{pos:>3}', end=' ')

    for data in player.values():

        print(f"{str(data):<15}", end='')     # Exibido os dados de cada jogador em ordem
    print()

while True:
    survey = int(input('Mostrar dados de qual jogador? (999 para parar) '))  # Escolher qual levantamento mostrar de
    # acordo com o COD do jogador
    if survey == 999:       # Se 999 o While para
        break

    while survey > len(players):    # Enquanto o erro persistir
        print(f'ERRO! Não existe jogador com código {survey}! Tente novamente')
        print('-' * 42)

        survey = int(input('Mostrar dados de qual jogador? '))

    print(f"-- LEVANTAMENTO DO JOGADOR {players[survey]['Nome']}:")     # Exibindo o levatamento do jogador escolhido

    for pos, gol in enumerate(players[survey]['Gols']):     # Exibindo o levantamento de gols por partida
        print(f'   No jogo {pos} fez {gol}')
    print('-' * 40)
print('<<VOLTE SEMPRE>>')   # Fim
