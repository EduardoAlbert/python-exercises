expression = str(input('Digite sua expressão: '))
eliminador = []

for simb in expression:

    if simb == '(':
        eliminador.append('(')
    elif simb == ')':
        if len(eliminador) > 0:
            eliminador.pop()
        else:
            eliminador.append(')')

if len(eliminador) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')