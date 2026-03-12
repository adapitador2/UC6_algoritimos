import requests

url = "https://rickandmortyapi.com/api/character"

# pergunta para o server se ta tudo funcionando
reposta = requests.get(url)

print(reposta)

# transforma tudo em json(formato de lista)
json = reposta.json()

# print(json)

# retorna apenas os resultados dentro do json 
personagem = json["results"]

# print(personagem)

# chama apenas os nomes e genero dos personagens
for nome in personagem:
    print(nome["name"], nome["gender"])