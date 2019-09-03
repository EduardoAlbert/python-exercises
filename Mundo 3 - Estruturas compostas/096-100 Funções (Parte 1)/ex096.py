def titulo(texto):
    print('-'*30)
    print(f"{texto:^30}")
    print('-'*30)


def area(larg, comp):
    print(f'A área de um terreno {larg}x{comp} é de {larg*comp}m².')


# Main Program
titulo('Controle de Terrenos')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
