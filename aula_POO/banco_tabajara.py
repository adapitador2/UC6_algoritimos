import pandas
import os
from Cliente import bababu
from criar_conta import bububa

caminho = "clientes_banco_tbj.xlsx"


print ("digite 1 para criar conta \ndigite 2 para acessar conta")
menu = int(input("digite opção desejada: "))

if (menu == 1):

    nome =          input("nome: ")
    cpf =           int(input("cpf: "))

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



    # try:
    #     leitura_excel = pandas.read_excel(caminho)
    # except:
    #     leitura_excel = pandas.DataFrame()

    #     conta = bububa(nome, cpf, tipo_conta)

    #     salvar = conta.salvar_dados()


    if os.path.exists (caminho):
        print("ebaaa")
        leitura_excel = pandas.read_excel(caminho)

    else:
        print("bah")

        leitura_excel = pandas.DataFrame()

        conta = bububa(nome, cpf, tipo_conta)

        novo_dado = conta.salvar_dados()
        leitura_excel = pandas.concat([leitura_excel, novo_dado], ignore_index=True)


    leitura_excel.to_excel(caminho, index = 0)





elif (menu == 2):
    print(":()")                                                                                                         

else:
    print(":/")