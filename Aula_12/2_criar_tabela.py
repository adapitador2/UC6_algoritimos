import pandas

nome1 = input("nome:")
idade1 = int(input("idade:"))
altura1 = int(input("altura(em cm):"))

dados = {
    "nome": [nome1],
    "idade": [idade1],
    "altura": [altura1]
}

# criar tabela excel
# se rodar denovo subistitui todos os dados da tabela anterior

excel = pandas.DataFrame(dados)
excel.to_excel("Aula_12/planilha_excel.xlsx", index = False)

print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))
