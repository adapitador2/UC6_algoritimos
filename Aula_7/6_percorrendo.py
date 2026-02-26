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

print (cliente)

for key in cliente:
    print(key)

for values in cliente.values():
    print(values)

for key, values in cliente.items():
    print(key, ": ", values)