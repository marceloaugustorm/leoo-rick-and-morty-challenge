import requests
import csv

personagens = []

for i in range(1, 51):
    url = f"https://rickandmortyapi.com/api/character/{i}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Erro ao acessar personagem {i}: Status {response.status_code}")
        continue  
    
    dados = response.json()
    personagens.append(dados)

arquivo = "personagens.csv"

with open(arquivo, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    
  
    writer.writerow(["id", "name", "status", "species", "type", "gender"])
    
    for personagem in personagens:
        writer.writerow([
            personagem["id"],
            f"{personagem['name']}",  
            f"{personagem['status']}",
            f"{personagem['species']}",
            f"{personagem['type']}",
            f"{personagem['gender']}"
        ])
