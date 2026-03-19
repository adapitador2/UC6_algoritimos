import pandas

print("digite 1 para criar uma nova planilha\ndigite 2 para interagir com planilha ja existente")
menu1 = int(input("digite a opção desejada: "))

if menu1 == 1:
    nome_planilha = input("digite o nome da planilha: ")
    quantidade_colunas = int(input("digite quantas colunas deseja: "))
    dicionario = {
        "id": [""] #gambiarra: não da pra criar planilha sem item nativo do dicionario, apagar coluna?
    }

    for i in range(quantidade_colunas): #tipo do arquivo
        nome_coluna = input(f"nome da coluna {i + 1}: ")
        dicionario[f"{nome_coluna}"] = ""



    excel = pandas.DataFrame(dicionario)
    excel.to_excel(f"Aula_12/exercicios/{nome_planilha}.xlsx")


    # criar_excel = pandas.DataFrame(dicionario)
    # criar_excel.to_excel(f"Aula_12/exercicios/{nome_planilha}.xlsx")











'''
while True:
    print("digite 1 para criar\ndigite 2 para adicionar\ndigite 3 para excluir\ndigite 4 para alterar")
    menu = int(input(""))

    if menu == 1:
        nome_planilha = input("digite o nome da planilha: ")

        print("digite o primeiro cadastro")
        
        nome = input("nome: ")
        idade = int(input("idade: "))
        altura = int(input("altura: "))
        cpf = int(input("cpf: "))

        dicionario = {
            "nome": [nome],
            "idade": [idade],
            "altura": [altura],
            "cpf": [cpf]
        }

        print(dicionario)
        # excel = pandas.DataFrame(dicionario)
        # excel.to_excel(f"Aula_12/exercicios/{nome_planilha}.xlsx")
    
    elif menu == 2:
        print("blublublu")

'''
# pedir se quer modigficar ou criar uma lista antes do lupin de repetição

# criar a lista com variaveis nulas para criar o excel vazio