sal = float(input('Qual é o salário do funcionário?\n\033[32mR$\033[m'))
if sal >= 1250:
    rise = (sal * 10) / 100
    print('Você terá um aumento de \033[31m10%\033[m no seu salário, totalizando: \033[32mR${:.2f}\033[m'.format(sal + rise))
else:
    rise = (sal * 15) / 100
    print('Você terá um aumento de \033[31m15%\033[m no seu salário, totalizando: \033[32mR${:.2f}\033[m'.format(sal + rise))
