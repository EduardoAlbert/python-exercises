table = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético,', 'Goiás', 'Botafogo', 'Bahia', 'São Paulo',
         'Conrinthias', 'Grêmio', 'Athletico-PR', 'Ceará SC', 'Fortaleza', 'Vasco da Gama', 'Fluminense', 'Chapecoense',
         'Cruzeiro', 'CSA', 'Avaí')

print('-='*30)
print('Lista de times do Brasileirão:', table)
print('-='*30)

print('Os 5 primeiros são', table[:5])
print('-='*30)

print('Os 4 útimos são', table[-4:])
print('-='*30)

print('Times em ordem alfabética:', sorted(table))
print('-='*30)

print(f'O Chapecoense etá na {table.index("Chapecoense") + 1}ª posição')
