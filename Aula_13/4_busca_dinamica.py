import pymysql
import pymysql.cursors

conexao = pymysql.connect(
    host="localhost", #endereço do servidor local
    user="root", #usuario do mysql
    password="",# senha do mysql
    database= "bd_livrariaonline", #nome do banco ja criado
    port=3306 #porta padrão do mysql(opcional)
)

cursor = conexao.cursor(pymysql.cursors.DictCursor)

# busca dinamica
nome_cli = input("digete um nome: ") #like usado para chamar semelhantes e "%" para ignorar depois

cursor.execute("select * from clientes where nome like %s", (nome_cli),) #case sensitive e nome completo 

dados_cli = cursor.fetchall()

print(dados_cli)