class bababu:
    def __init__(self, id_conta, nome, cpf, tipo_conta, agencia, extrato):
        self.id_conta = id_conta
        self.nome = nome
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.agencia = agencia
        self.extrato = extrato

    def __str__(self):
        return f"id_conta: {self.id_conta} | nome: {self.nome} | cpf: {self.cpf} | tipo conta: {self.tipo_conta} | agencia: {self.agencia} | extrato: {self.extrato}"