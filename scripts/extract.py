import os
import json
import requests

WEATHER_API = "65e43c0549a432343eeae082305fb77b"
CIDADE = "recife"

data_apis = {
    "api_posts": {
        "url": "https://jsonplaceholder.typicode.com/posts",
        "caminho_save": "posts",
        "nome_api": "Posts"
    },
    "api_rnm": {
        "url": "https://rickandmortyapi.com/api/character",
        "caminho_save": "rnm",
        "nome_api": "Rick and Morty"
    },
    "api_clima": {
        "url": f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={WEATHER_API}&units=metric&lang=pt_br",
        "caminho_save": "clima",
        "nome_api": "Clima"
    }
}


def extract_data(nome):
    try:
        api = data_apis[nome]

        response = requests.get(api["url"])
        response.raise_for_status()

        dados_brutos = response.json()

        caminho_save = f"../data/raw/raw_{api['caminho_save']}.json"

        with open(caminho_save, "w", encoding="utf-8") as f:
            json.dump(dados_brutos, f, ensure_ascii=False, indent=4)
        
        print(f"Dados da API {api['nome_api']} salva")
            
    
    except requests.exceptions.RequestException as e:
        print(f"ERRO: {e}")

# def extract_data_rnm():
#     try:
#         response = requests.get(data_apis["api_rnm"]["url"])
#         response.raise_for_status()

#         dados_brutos = response.json()

#         caminho_save = f"data/raw/raw_{data_apis['api_rnm']['caminho_save']}.json"

#         with open(caminho_save, "w", encoding="utf-8") as f:
#             json.dump(dados_brutos, f, ensure_ascii=False, indent=4)

    
#     except requests.exceptions.RequestException as e:
#         print(f"ERRO: {e}")

# def extract_data_clima():
#     try:
#         response = requests.get(data_apis["api_clima"]["url"])
#         response.raise_for_status()

#         dados_brutos = response.json()

#         caminho_save = f"data/raw/raw_{data_apis['api_clima']['caminho_save']}.json"

#         with open (caminho_save, "w", encodinh="utf-8") as f:
#             json.dump(dados_brutos, f, ensure_ascii=False, indent=4)

#     except requests.exceptions.RequestException as e:
#         print(f"ERRO: {e}")


def selector(num):
    if num == 1:
        return "api_posts"
    elif num == 2:
        return "api_rnm"
    elif num == 3:
        return "api_clima"
    else:
        print("selecione um numero valido da proxima")

if __name__ == "__main__":
    select = int(input("Qual get?\n1-JSON\n2-RnM\n3-Clima\n"))
    api = selector(select)
    if api:
        extract_data(api)
