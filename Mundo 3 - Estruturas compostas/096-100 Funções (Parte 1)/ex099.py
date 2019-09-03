def maior(*valueS):
    print('-='*30)
    print('Analisando os valores passados...')

    for value in valueS:
        print(value, end=' ')

    print(f'Foram informados {len(valueS)} valores ao todo.')
    print(f'O maior valor informado foi {max(valueS)}' if len(valueS) > 0
          else 'O maior valor informado foi 0')


# Main Program
maior(2, 9, 4, 5, 7, 1)
maior(2, 5, 6, 2)
maior()
