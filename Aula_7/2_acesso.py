cliente = {
    "cpf": 12312312399,
    "nome": "robson",
    "data": 11042008,

# informação compactada
    "array": [2, "lbuybkbukbu", True, 3, 4, 5, 6, 7, 8, 9],

# dicionario dentro de dicionario
    "endereco": {
        "cidade": "bumbum",
        "estado": "bundinha"
    }
}

# acesso dicionairo padrão
print (cliente)
print (cliente["cpf"])

# acesso array, chama por ordem numerica
print (cliente["array"])
print (cliente["array"][7])


print (cliente["endereco"])
print (cliente["endereco"]["cidade"])