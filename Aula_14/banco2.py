import pandas
import os


try:
    pandas.read_excel("Aula_14/banco2.xlsx")
except:
    dados = {
    "id_conta":     [""],
    "nome":         [""],
    "cpf":          [""],
    "tipo_conta":   [""],
    "agencia":      [""],
    "extrato":      [""]
    }

    excel = pandas.DataFrame(dados)
    excel.to_excel("Aula_14/banco2.xlsx", index = False)

while True:
    try:
        print ("digite 1 para criar conta \ndigite 2 para acessar conta")
        menu = int(input("digite opção desejada: "))
        break
    except ValueError:                                                                  # or (menu > 2) or (menu < 1):
        print("numero invalido")

if (menu == 1):                                                                         # criar conta

    excel = pandas.read_excel("Aula_14/banco2.xlsx")
    ul = len(excel)

    id_conta =      ul + 1
    agencia =       ul + 401
    extrato =       0

    print("para criar sua conta precisamos de: ")
    nome =          input("nome: ")
    cpf =           int(input("cpf: "))
    print("digite o numero para indicar o tipo de conta:\n1 para conta corrente\n2 para conta poupança\n3 para conta salario")

    while True:
        tipo_conta = int(input("tipo de conta: "))

        if (tipo_conta == 1):
            tipo_conta = "corrente"
            break
        
        elif (tipo_conta == 2):
            tipo_conta = "poupança"
            break

        elif (tipo_conta == 3):
            tipo_conta = "salario"
            break

        else:
            ("NUMERO INVALIDO")                                                          # nao vai sapoha



    dados = {
        "id_conta":     id_conta,
        "nome":         nome,
        "cpf":          cpf,
        "tipo_conta":   tipo_conta,
        "agencia":      agencia,
        "extrato":      extrato
    }

    excel.loc[ul, "id_conta"] =     dados["id_conta"]
    excel.loc[ul, "nome"] =         dados["nome"]
    excel.loc[ul, "cpf"] =          dados["cpf"]
    excel.loc[ul, "tipo_conta"] =   dados["tipo_conta"]
    excel.loc[ul, "agencia"] =      dados["agencia"]
    excel.loc[ul, "extrato"] =      dados["extrato"]

    excel.to_excel("Aula_14/banco2.xlsx", index = False)

elif (menu == 2):
    print("digite os dados para acessar a sua conta")
    cpf = int(input("cpf: "))
    id_conta = int(input("numero da conta: "))

    excel = pandas.read_excel("Aula_14/banco2.xlsx")

    login = excel[(excel['cpf'] == cpf) & (excel['id_conta'] == id_conta)]

    if login.empty:
        print("conta não encontrada")

    else:
        print("conta acessada")
        for d in login:
            print(d, ": ", login[f"{d}"].values[0])
        

        
        print("digite:\n1 para consultar saldo\ndigite 2 para saque\n3 para deposito")
        menu2 = int(input("digite o numero desejado"))

        if (menu2 == 1):
            print("seu saldo atual é: ", login["extrato"].values[0])



