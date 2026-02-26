aluno = {

}

aluno["nome"] = input("nome: ")
aluno["nota1"] = int(input("nota 1: "))
aluno["nota2"] = int(input("nota 2: "))
aluno["nota3"] = int(input("nota 3: "))
aluno["nota4"] = int(input("nota 4: "))
aluno["nota5"] = int(input("nota 5: "))
aluno["media"] = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"] + aluno["nota4"] + aluno["nota5"]) / 5



for key, values in aluno.items():
    print (key, ": ", values)


# adcionar filtro de maiuscula
# while para numero invalido ou < 10
# sistema array para adição indeterminada de nota
# dividir pelo numero maximo de arrays