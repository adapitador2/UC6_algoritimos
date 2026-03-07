nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))



with open("Aula_10/exercicios/texto.txt", "a") as dados:
    dados.write(f"{nome } - {idade} \n")

# CONFERIR LISTA E VER SE NAO TE NOME REPETIDO