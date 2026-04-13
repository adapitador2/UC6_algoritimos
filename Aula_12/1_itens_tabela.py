import pandas
# criar e adicionar itens da tabela
"""
nome1 = input("nome:")
idade1 = int(input("idade:"))
altura1 = int(input("altura(em cm):"))

dados = {
    "nome": [nome1],
    "idade": [idade1],
    "altura": [altura1]
}
"""

excel = pandas.read_excel("Aula_12\planilha_excel.xlsx")

# criar tabela excel
# se rodar denovo subistitui o anterior
"""
excel = pandas.DataFrame(dados)
excel.to_excel("Aula_12/planilha_excel.xlsx", index = False)

print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))
"""

# adicionar na tabela excel
"""
adicao_excel = pandas.read_excel("Aula_12\planilha_excel.xlsx")
ultima_linha = len(adicao_excel)

adicao_excel.loc[ultima_linha, "nome"] = dados["nome"]
adicao_excel.loc[ultima_linha, "idade"] = dados["idade"]
adicao_excel.loc[ultima_linha, "altura"] = dados["altura"]

adicao_excel.to_excel("Aula_12\planilha_excel.xlsx", index = False)

print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))
"""

# excluir linha (apagar e salvar)
"""
excel = excel.drop(0) #linha da planilha tirando cabeçario

excel.to_excel("Aula_12\planilha_excel.xlsx", index = False)

print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))
"""

# alterar linha (altera e salva)
"""
print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))

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
"""
print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))