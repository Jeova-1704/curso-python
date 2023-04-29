import requests


# criar um decorator calcular_tempo
def calcular_tempo(funcao):
    def wrapperr():
        print('Vou pegar a cotação')
        funcao()
        print('A cotação atualizada já está acima')
    return wrapperr


@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisiicao = requests.get(link)
    requisiicao = requisiicao.json()
    print(requisiicao['USDBRL']['bid'])


pegar_cotacao_dolar()