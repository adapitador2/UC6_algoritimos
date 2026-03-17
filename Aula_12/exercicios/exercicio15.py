import pandas

while True:
    print("digite 1 para criar\ndigite 2 para adicionar\ndigite 3 para excluir\ndigite 4 para alterar")
    menu = int(input(""))

    if menu == 1:
        nome_planilha = input("digite o nome da planilha")

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

        excel = pandas.DataFrame(dicionario)
        excel.to_excel(f"Aula_12/exercicios/{nome_planilha}.xlsx")