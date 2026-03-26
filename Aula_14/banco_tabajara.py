import pandas
import os

print("1 - criar conta")
print("2 - Acessar conta")
menu = int(input("digite um numero: "))

if (os.path.exists("Aula_14/banco_tabajara.xlsx") == False): 
    dados = {
    "id_conta":     [""],
    "nome_cli":     [""],
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
        extrato =       0

        dados = {
            "id_conta":     id_conta,
            "nome_cli":     nome,
            "cpf":          cpf,
            "tipo_conta":   tipo_conta,
            "agencia":      agencia,
            "extrato":      extrato
        }

        excel.loc[ul, "id_conta"] =     dados["id_conta"]
        excel.loc[ul, "nome_cli"] =     dados["nome_cli"]
        excel.loc[ul, "cpf"] =          dados["cpf"]
        excel.loc[ul, "tipo_conta"] =   dados["tipo_conta"]
        excel.loc[ul, "agencia"] =      dados["agencia"]
        excel.loc[ul, "extrato"] =      dados["extrato"]

        excel.to_excel("Aula_14/banco_tabajara.xlsx", index = False)

        print(pandas.read_excel("Aula_14/banco_tabajara.xlsx"))




    elif (menu == 2):
        print("dit=gte os dados para acessar a sua conta")
        # num = int(input("numro da linha da cont(teste): "))
        cpf = int(input("cpf: "))
        id_conta = int(input("numero da conta: "))

        excel = pandas.read_excel("Aula_14/banco_tabajara.xlsx")

        login = excel[(excel['cpf'] == cpf) & (excel['id_conta'] == id_conta)]
        
        print(login)
        








"""
        cpft = excel.loc[cpf:"cpf", "cpf"]
        id_contat = excel.loc[cpf:"cpf", "id_conta"]

        if (id_conta == id_contat and cpf == cpft):
        #     print(excel.loc[cpf:"cpf",])

            print("1 para sacar\n2 para depositar\n3paara consultar")
            menu2 = int(input("gigite o umeor desejado"))


            if (menu2 ==1):
                valor_saque = float(input("digite quanto deseja sacar"))
                extrato = excel.loc[extratoconta]

                if (valor_saque >= 0):
                    if (valor_saque <= extrato):
                        print("saque concluido")
                        # subitrair valor saque do extrato

                    else:
                        print("pobre")

                else:
                    print("numero invalido")

            elif (menu2 ==2):
                valor_deposito = float(input("digite o valor depositado"))
                extrato = excel.loc[extratoconta]






        
        else:
            print("errado / conta nao existe")
"""

