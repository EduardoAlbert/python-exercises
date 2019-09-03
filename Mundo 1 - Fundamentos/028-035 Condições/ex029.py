speed = float(input('Qual é a velocidade atual do carro? '))
if speed > 80:
    multa = speed - 80
    print('\033[32mVocê foi multado em \033[31mR${:.2f} \033[32mpor execeder \033[31m{}Km \033[32mda velocidade limite de 80Km/h!\033[m'.format(multa*7, multa))
else:
    kms = 80 - speed
    print('\033[34mA velocidade limite é \033[31m80Km/h\033[34m, você está a {:.1f}Km/h abaixo do limite.\033[32m Dirija com segurança!'.format(kms))
