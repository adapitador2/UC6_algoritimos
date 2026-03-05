nome = input("digite seu nome: ")
idade = input("digite sua idade: ")



with open("Aula_10/exercicios/texto.txt", "a") as dados:
    dados.write(nome + idade + "\n")