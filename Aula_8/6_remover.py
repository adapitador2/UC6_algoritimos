lista = ["item1", "item2", "item3", "item4", "item5", "item5"]

# remove um item de mesmo valor da lista
lista.remove("item1")
# retira apenas o primeiro item encontrado
lista.remove("item5")

print (lista)

# remove da posição na lista (considera a lista após a remoção anterior, tira o item 3)
lista.pop(1)
# se não especificado retira o ultimo da lista
lista.pop()

print (lista)