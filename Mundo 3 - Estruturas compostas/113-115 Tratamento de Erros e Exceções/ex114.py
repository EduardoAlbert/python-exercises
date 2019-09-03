import requests

try:
    requests.get('http://pudim.com.br/')
except requests.exceptions.ConnectionError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')

