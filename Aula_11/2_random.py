import random
alunos = []
new_aluno = input("nome alunos")

while True:
    if new_aluno == "bah":
        aluno_aleatorio = random.choice(alunos)
        print(aluno_aleatorio)
        break
    else:
        new_aluno = input("nome alunos")
        alunos.append(new_aluno)