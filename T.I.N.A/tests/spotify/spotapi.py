from dotenv import load_dotenv #permite pegar variaveis de arquivos env
import os
import base64 #converte valores normais para base 64
from requests import post #permite fazer requests da web com o python
import json #pacotes de informação
import requests

load_dotenv()
#importa o client id e o client secret do arquivo env
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret   #concatena os dois client infos de cima para obter o valor base para o token
    auth_bytes = auth_string.encode("utf-8") # coda a concatenação de cima em utf 8
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8") #usa a biblioteca base64 para encodar em base64 o valor anterior

    url = "https://accounts.spotify.com/api/token" #url de solicitação do token
    headers = {
        "Authorization": "Basic " + auth_base64,   #criando o header que será enviado para o site como solicitação
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = post(url,headers = headers, data = data)  #postando para a url da api o header e os dados
    json_result = json.loads(result.content) #transformando em json os resultados vindos do post
    token  = json_result["access_token"]  #salvando o token em uma variável 
    return token #retornando ele da função

def get_auth_header(token):
    return {"Authorization": "Bearer " + token} #uma função de construção do header para lançar requests futuras




token = get_token()



#-------------------------------------------------
'''iniciando trecho de solicitação de musica'''
#-------------------------------------------------


url = 'https://api.spotify.com/v1/me/player'

# Parâmetro de mercado
market = 'BR'  # Substitua 'ES' pelo código do país desejado

# Cabeçalho da solicitação com token de autorização (substitua com seu token real)
headers = {
    {'Authorization': 'Bearer ' + token}
}

# Parâmetros da solicitação (se necessário)
params = {
    'market': market
}
# Parâmetro de tipos adicionais (tipos de itens suportados pelo cliente)
additional_types = 'track,episode'

# Realizar a solicitação GET
response = requests.get(url, headers=headers, params=params)

# Verificar se a solicitação foi bem-sucedida (código de status HTTP 200)
if response.status_code == 200:
    data = response.json()  # Converte a resposta em formato JSON
    print(data)
else:
    print('Erro na solicitação. Código de status:', response.status_code)
