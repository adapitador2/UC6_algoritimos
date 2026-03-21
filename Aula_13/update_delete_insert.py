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



try:
    # # insert
    sql_insert = "insert into clientes (nome, email) values(%s,%s)"
    cursor.execute(sql_insert, ("genovevo", "joao_paulo24@hotmart.net"))
    conexao.commit()
    print("inserido", cursor.lastrowid)

    # # update
    sql_update = "update clientes set email = %s where id_cliente = %s"#aasasasasASAAASASAAAASASAASSASSASSAAASSSASASSSASSASASSAASSASSASASSSSSSSlijliijlikijlkljikkijljkiiljlljjkjiiijljlijlijlijlijllijijliijljkkjiijljlijlijiljljijlijkknmmmmmmmmmmmmmmmmmmmmmmmmmmmommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmimmmmmmmmmmmmmmmmmmmmnmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmSSSSASDAWDWAWADADWDSDWDWDWWAADWDWWWDWDWWDWDWDSADDSAASSSAAASSDWWWAAAWWWDSDSDDDWASDSDADADWWDAWADWDWDASSDSSSDWWAADAAADSDADAWsdadwasdawawwaddawdwawadawdadwawdwadasadadsllijkjjljiljkjlijijijlkjljijkjjljiiijlkjiji
    cursor.execute(sql_update, ("genovevo@gostosinho.hotmart.com", 130))
    conexao.commit()
    print("linha alterada", cursor.rowcount) #quantidade de linha alteradas

    # delete
    cursor.execute("delete from clientes where id_cliente >= %s", (131))
    conexao.commit()

except Exception as erro: # caso de erro
    conexao.rollback()
    print("erro", erro)

finally: # executa idependente do resultado do try
    cursor.close()
    conexao.close() # fecha conexao com banco de dados