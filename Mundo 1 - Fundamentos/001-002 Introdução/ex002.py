nome = str(input('Qual é o seu nome?')).strip()
while '0' in nome or '1' in nome or '2' in nome or '3' in nome or '4' in nome or '5' in nome or '6' in nome or '7' in \
        nome or '8' in nome or '9' in nome:

    print('Não é comum existirem números em nomes! Tente novamente...')
    nome = str(input('Qual é o seu nome?')).strip()
print('Olá', nome, '!', 'Prazer em te conhecer!')
