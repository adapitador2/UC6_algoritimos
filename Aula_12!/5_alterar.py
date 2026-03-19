import pandas
print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))

excel = pandas.read_excel("Aula_12\planilha_excel.xlsx")

# alterar linha (altera e salva)

alterar = int(input("qual deseja alterar?"))

nome1 = input("nome:")
idade1 = int(input("idade:"))
altura1 = int(input("altura(em cm):"))

dados = {
    "nome": [nome1],
    "idade": [idade1],
    "altura": [altura1]
}


excel.loc[alterar, "nome"] = dados["nome"]
excel.loc[alterar, "idade"] = dados["idade"]
excel.loc[alterar, "altura"] = dados["altura"]

excel.to_excel("Aula_12\planilha_excel.xlsx", index = False)

print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))