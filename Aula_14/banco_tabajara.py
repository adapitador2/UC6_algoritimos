import pandas
import os

print("1 - criar conta")
print("2 - Acessar conta")
menu = int(input("digite um numero: "))

if (os.path.exists("Aula_14/banco_tabajara.xlsx") == False): 
    dados = {
    "id_conta":     [""],
    "nome":     [""],
    "cpf":          [""],
    "tipo_conta":   [""],
    "agencia":      [""],
    "extrato":      [""]
}
# criação excel
    excel = pandas.DataFrame(dados)
    excel.to_excel("Aula_14/banco_tabajara.xlsx", index = False)

else:

    if (menu == 1): # criar conta

        excel = pandas.read_excel("Aula_14/banco_tabajara.xlsx")
        ul = len(excel)
        print("para criar sua conta precisamos de: ")

        id_conta =      ul + 1
        nome =          input("nome: ")
        cpf =           int(input("cpf: "))
        tipo_conta =    input("tipo de conta: ")    # if else para opções de conta
        agencia =       ul + 401
        extrato =       20

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

        excel.to_excel("Aula_14/banco_tabajara.xlsx", index = False)

        print(pandas.read_excel("Aula_14/banco_tabajara.xlsx"))




    elif (menu == 2):
        print("digite os dados para acessar a sua conta")
        cpf = int(input("cpf: "))
        id_conta = int(input("numero da conta: "))

        excel = pandas.read_excel("Aula_14/banco_tabajara.xlsx")

        login = excel[(excel['cpf'] == cpf) & (excel['id_conta'] == id_conta)]
        

        if login.empty:
            print("login invalido/inexistente")
        
        else:

            print(login)

            print("menu 2\n digite 1 parra saqque\n2para deposito\n3 para saldo")
            menu2 = int(input("numearo"))

            if (menu2 == 1):
                saque = float(input("quanto deseja sacara?"))

                if(saque < 0):
                    print("numero invalido")

                else:

                    extrato = login["extrato"].values[0]

                    if(saque < extrato):
                        extrato -= saque
                        
                        excel.loc[login.index[0], "extrato"] = extrato

                        excel.to_excel("Aula_14/banco_tabajara.xlsx", index = False)

                        print(login)