import pandas
# criar e adicionar itens da tabela

nome1 = input("nome:")
idade1 = int(input("idade:"))
altura1 = int(input("altura(em cm):"))

dados = {
    "nome": [nome1],
    "idade": [idade1],
    "altura": [altura1]
}


excel = pandas.read_excel("Aula_12\planilha_excel.xlsx")

# criar tabela excel
# se rodar denovo subistitui o anterior

excel = pandas.DataFrame(dados)
excel.to_excel("Aula_12/planilha_excel.xlsx", index = False)

print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))
