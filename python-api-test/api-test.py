import requests
import random
import string
import json

# Função para gerar uma string aleatória (usada para os dados do POST)
def gerar_string_aleatoria(tamanho=10):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for i in range(tamanho))

# 1. Teste GET
def teste_get():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        print("GET request successful!")
    else:
        print(f"GET request failed with status code: {response.status_code}")
        return
    
    # Valida se a resposta é um JSON e se é uma lista de posts
    try:
        dados = response.json()
        if isinstance(dados, list):
            print(f"GET request returned {len(dados)} posts.")
        else:
            print("GET request did not return a list.")
            return
    except json.JSONDecodeError:
        print("Resposta não é um JSON válido.")
        return

    # Validação da estrutura dos dados
    for post in dados[:5]:  # Verificando apenas os primeiros 5 posts
        if all(key in post for key in ["userId", "id", "title", "body"]):
            print("Post structure is valid.")
        else:
            print("Post structure is invalid.")
            return

# 2. Teste POST
def teste_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Gerando dados aleatórios para o POST
    dados = {
        "title": gerar_string_aleatoria(),
        "body": gerar_string_aleatoria(),
        "userId": random.randint(1, 10)  # Gerando um userId aleatório
    }
    
    # Enviando requisição POST
    response = requests.post(url, json=dados)
    
    # Valida resposta
    if response.status_code == 201:
        print("POST request successful!")
    else:
        print(f"POST request failed with status code: {response.status_code}")
        return
    
    # Valida se o ID foi gerado e está presente na resposta
    try:
        dados_resposta = response.json()
        if "id" in dados_resposta:
            print(f"ID gerado: {dados_resposta['id']}")
        else:
            print("O campo 'id' não foi retornado na resposta.")
            return
    except json.JSONDecodeError:
        print("Resposta não é um JSON válido.")
        return

    # Valida se os dados enviados são consistentes
    if dados_resposta['title'] == dados['title'] and dados_resposta['body'] == dados['body']:
        print("POST data consistency check passed.")
    else:
        print("POST data consistency check failed.")
        return

    # Teste de ID único: Vamos salvar o ID retornado para compará-lo em futuras requisições
    global ids_gerados
    if 'ids_gerados' not in globals():
        ids_gerados = []

    # Verificar se o ID gerado é único
    if dados_resposta['id'] not in ids_gerados:
        ids_gerados.append(dados_resposta['id'])
        print("ID is unique.")
    else:
        print("ID is not unique!")
        return

# 3. Execução dos testes
def executar_testes():
    teste_get()
    teste_post()

# Executando os testes
if __name__ == "__main__":
    executar_testes()
