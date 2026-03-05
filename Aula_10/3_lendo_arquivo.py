with open("Aula_10/texto.txt", "w") as teste:
    teste.write(input("blublublu: "))


with open("Aula_10/texto.txt", "r") as teste:
    conteudo = teste.read()
    print(conteudo)

# "r" le o arquivo