# lista de compras, inserir 3 itens, mostrar lista completa
lista = []

num = int(input("numero de itens: "))

for i in range(num):
    item = input("digite um item: ")
    lista.append(item)

lista.sort()

print ("lista:")

for values in lista:
    print(values)