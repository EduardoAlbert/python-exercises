valorInicial = float(input('Preço das compras: R$ '))
print(''''\nFORMAS DE PAGAMENTO
[1] À vista com Dinheiro/Cheque 
[2] À vista no Cartão 
[3] Em até 2x no cartão 
[4] 3x ou mais no cartão''')
condicao = int(input('\nSelecione uma opção: '))
valorFinal = float

if condicao == 1:
    valorFinal = valorInicial - (valorInicial * 10 / 100)

elif condicao == 2:
    valorFinal = valorInicial - (valorInicial * 5/100)

elif condicao == 3:
    valorFinal = valorInicial

elif condicao == 4:
    valorFinal = valorInicial + (valorInicial * 20/100)
    numParcelas = int(input('Quantas parcelas? '))
    valorParcelas = valorFinal / numParcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(numParcelas, valorParcelas))
else:
    print('Opção Inválida...')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valorInicial, valorFinal))