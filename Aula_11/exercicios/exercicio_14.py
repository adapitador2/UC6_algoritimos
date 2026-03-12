import requests

# url = "https://rickandmortyapi.com/api/character"
# reposta = requests.get(url)
# json = reposta.json()
# personagens = json["results"]

# # for info in personagens:
#     print("nome: ",info["name"])
#     print("status: ",info["status"])
#     print("genero: ",info["gender"])

id = int(input("digite um id: "))

link_api = f"https://rickandmortyapi.com/api/character/{id}"
reposta = requests.get(link_api)
json = reposta.json()


print(json)
print("nome: ",json["name"])
print("status: ",json["status"])
print("status: ",json["species"])
print("status: ",json["type"])
print("genero: ",json["gender"])
print("status: ",json["origin"["name"]])
print("status: ",json["location"])


# name, status, species, type, gender, origin, location