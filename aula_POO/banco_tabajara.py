import pandas
from Cliente import bababu

caminho = "clientes_banco_tbj.xlsx"


print ("digite 1 para criar conta \ndigite 2 para acessar conta")
menu = int(input("digite opção desejada: "))

if (menu == 1):

    nome =          input("nome: ")
    cpf =           int(input("cpf: "))

    id_conta =      0
    agencia =       400
    extrato =       0

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
            print("NUMERO INVALIDO")

    dados_cli = bababu(id_conta, nome,  cpf, tipo_conta, agencia, extrato)

    print(dados_cli)

    excel = pandas.DataFrame(dados_cli)
    excel.to_excel(caminho, index = False)

elif (menu == 2):
    print(":()")                                                                                                         

else:
    print(":/")