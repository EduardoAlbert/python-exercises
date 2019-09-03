nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', "oito", 'nove', 'dez',
        'onze', 'doze,', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

finishOrContinue = str

while finishOrContinue != 'N':
    choices = int(input('Digite um número entre 0 e 20: '))

    while choices < 0 or choices > 20:
        choices = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    if 0 <= choices <= 20:
        print('Você digitou o número', nums[choices])

    finishOrContinue = str(input('Quer continuar?(S/N): ')).upper().strip()[0]


