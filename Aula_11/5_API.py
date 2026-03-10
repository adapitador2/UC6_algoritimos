import requests

url = "https://rickandmortyapi.com/api/character"

reposta = requests.get(url)

print(reposta)

json = reposta.json()

# print(json)

personagem = json["results"]

# print(personagem)

for nome in personagem:
    print(nome["name"], nome["gender"])