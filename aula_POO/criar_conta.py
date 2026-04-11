from Cliente import bababu
import pandas

class bububa:
    def __init__(self, nome, cpf, tipo_conta):

        id_conta =      0
        agencia =       400
        extrato =       0


        self.cliente_objeto = bababu(id_conta, nome,  cpf, tipo_conta, agencia, extrato)




    def salvar_dados(self):

        cliente_dicionario = {
            "id_conta":         [self.cliente_objeto.id_conta],
            "nome":             [self.cliente_objeto.nome],
            "cpf":              [self.cliente_objeto.cpf],
            "tipo_conta":       [self.cliente_objeto.tipo_conta],
            "agencia":          [self.cliente_objeto.agencia],
            "extrato":          [self.cliente_objeto.extrato]
        }


        excel = pandas.DataFrame(cliente_dicionario)
        return excel