L = float(input('Quanto de Largura:'))
A = float(input('Altura de Altura:'))
area = L * A
ldt = area / 2
print('A área da sua parede é {} m² e você necessita de {:.3f} Litros de tinta para pintá-la'.format(area, ldt))