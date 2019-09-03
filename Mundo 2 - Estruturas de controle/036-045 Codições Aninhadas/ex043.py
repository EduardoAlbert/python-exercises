print('-*- IMC -*-')

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura: '))

imc = peso / altura**2
status = str

if imc < 18.5:
    status = 'Abaixo do Peso'

elif 18.5 <= imc < 25:
    status = 'Peso Ideal'

elif 25 <= imc < 30:
    status = 'Sobrepeso'

elif 30 <= imc < 40:
    status = 'Obesidade'

elif imc >= 40:
    status = 'Obesidade Morbida'

print('Seu Status de IMC é: ', status)
