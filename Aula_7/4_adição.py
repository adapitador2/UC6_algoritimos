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

cliente["celular"] = 202020202020

print (cliente)

# # acesso array, chama por ordem numerica
# print (cliente["array"])

# cliente["array"][10] = ":("

# print (cliente["array"][10])


print (cliente["endereco"])

cliente["endereco"]["cep"] = 40028922

print (cliente["endereco"]["cep"])