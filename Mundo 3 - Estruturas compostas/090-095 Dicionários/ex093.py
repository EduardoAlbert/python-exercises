gols = list()
somaGols = 0

dados = {'Nome': str(input('Nome do Jogador: '))}
numPartidas = int(input(f"Quantas partidas {dados['Nome']} jogou? "))

for partidas in range(0, numPartidas):

    golPartida = int(input(f'Quantos gols na partida {partidas}? '))
    gols.append(golPartida)
    somaGols += golPartida

dados['Gols'] = gols
dados['Total'] = somaGols

print('-='*30)
print(dados)
print('-='*30)

for key, value in dados.items():

    print(f'O campo {key} tem o valor {value}')

print('-='*30)
print(f"O jogador {dados['Nome']} jogou {numPartidas} partidas.")

for pos, i in enumerate(gols):

    print(f"=> Na partida {pos}, fez {i} gols.")

print(f'Foi um total de {dados["Total"]} gols.')
