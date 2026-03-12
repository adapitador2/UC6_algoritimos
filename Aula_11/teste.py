import requests

def resultado(p):
    print("========================")
    print("id: ",p["id"])
    print("nome: ",p["name"])
    print("status: ",p["status"])
    print("specie: ",p["species"])
    # print("tipo: ",p["type"])
    print("genero: ",p["gender"])
    print("origem: ",p["origin"]["name"])
    print("localização: ",p["location"]["name"])
    print("========================\n")




while True:
    print("digite 1 para retorno por id \ndigite 2 para retorno por nome \ndigite 3 para retornar todos os personagens \ndigite 4 para sair")

    menu = input("digite o numero: ")

    if menu == "1":
        id = int(input("id do personagem: "))
        url = f"https://rickandmortyapi.com/api/character/{id}"
        reposta = requests.get(url)
        json = reposta.json()
        resultado(json)

    elif menu == "2":
        nome = input("nome do personagem: ")
        url = f"https://rickandmortyapi.com/api/character/?name={nome}"
        reposta = requests.get(url)
        json = reposta.json()
        for n in json["results"]:
            resultado(n)

    elif menu == "3": #limite de 20?
        url = f"https://rickandmortyapi.com/api/character"
        reposta = requests.get(url)
        json = reposta.json()
        for a in json["results"]:
            resultado(a)

    elif menu == "4":
        break

    else:
        print("numero invalido, digite novamente\n")