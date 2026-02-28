lista = []

for i in range(4):
    item = input("digite um nome: ")
    lista.append(item)

remover = input("digite um nome para remover: ")

while True:
    if remover in lista:
        lista.remove(remover)
        break
    else:
        while remover not in lista:
            print("nome invalido")
            remover = input("digite um nome valido: ")

lista.sort()

print("lista de nomes:")
for value in lista:
    print(value)