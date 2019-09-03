nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Média {:.1f} / Reprovado.'.format(media))
elif 5 < media < 6.9:
    print('Média {:.1f} / Recuperação.'.format(media))
elif media >= 7:
    print('Média {:.1f} / Aprovado.'.format(media))
