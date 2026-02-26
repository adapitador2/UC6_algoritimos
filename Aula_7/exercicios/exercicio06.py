"""
dados = {
    "nome": "",
    "idade": "",
    "cidade": ""
}

dados["nome"] = input("digite nome: ")
dados["idade"] = int(input("digite idade: "))
dados["cidade"] = input("digite cidade: ")

for key, values in dados.items():
    print (key, ": ", values)
"""

dados = {

}

dados["nome"] = input("nome: ")
dados["idade"] = int(input("idade: "))
dados["cidade"] = input("cidade: ")

print (dados)
for key, values in dados.items():
    print (key, ": ", values)