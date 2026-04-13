import pandas
print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))

excel = pandas.read_excel("Aula_12\planilha_excel.xlsx")

# excluir linha (apagar e salvar)

excluir = int(input("qualqer excluir?"))

excluir_excel = excel.drop(excluir) #linha da planilha tirando cabeçario

excluir_excel.to_excel("Aula_12\planilha_excel.xlsx", index = False)

print(pandas.read_excel("Aula_12\planilha_excel.xlsx"))