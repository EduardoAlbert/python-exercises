from datetime import date

dados = dict()      # Declarado o dicionario

dados['Nome'] = str(input('Nome: '))        # dicionario recebe o dado: Nome
anoDeNascimento = int(input('Ano de Nascimento: '))   # dicionario recebe o dado: Ano de Nasci...
anoAtual = date.today().year        # Variavel recebe o ano atual

dados['Idade'] = anoAtual - anoDeNascimento         # dicionario recebe a o dado: Idade

dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 se não tem): '))  # Nº Carteira de trab...

if dados['Carteira de Trabalho'] != 0:         # Se houver carteira de trabalho

    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: '))

    totalDeContribuicao = anoAtual - dados['Ano de Contratação']    # total em anos de contribuição
    faltaContribuir = 35 - totalDeContribuicao          # subtraido de 35 anos, resultado em quanto falta contribuir
    dados['Aposentadoria'] = dados['Idade'] + faltaContribuir       # somado com a idade

for item, dado in dados.items():

    print(f'{item} tem o valor {dado}')         # exibindo cada item e dado
