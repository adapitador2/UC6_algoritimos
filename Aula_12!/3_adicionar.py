import pandas
print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))

excel = pandas.read_excel("Aula_12\planilha_excel.xlsx")

# criar e adicionar itens da tabela

nome1 = input("nome:")
idade1 = int(input("idade:"))
altura1 = int(input("altura(em cm):"))

dados = {
    "nome": [nome1],
    "idade": [idade1],
    "altura": [altura1]
}
# adicionar na tabela excel
# 
adicao_excel = pandas.read_excel("Aula_12\planilha_excel.xlsx")
ultima_linha = len(adicao_excel)

adicao_excel.loc[ultima_linha, "nome"] = dados["nome"]
adicao_excel.loc[ultima_linha, "idade"] = dados["idade"]
adicao_excel.loc[ultima_linha, "altura"] = dados["altura"]

adicao_excel.to_excel("Aula_12\planilha_excel.xlsx", index = False)

print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))