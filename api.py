import requests

i = 0

personagens = []

for i in range(1,51):
    url = f"https://rickandmortyapi.com/api/character/{i}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar a API", response.status_code)
        continue 
    
    dados = response.json()
    personagens.append(dados)

    print(dados["name"])




    


