# pess um numero e verifique se é o mesmo do random

import random

num_usuario = int(input("digite um numero de 1 a 2000: "))
num_random = random.randint(1,2000)
contador = 0

print(num_usuario)
print(num_random)

while True:
    if num_usuario != num_random:
        print("perdeu otario")
        num_usuario = random.randint(1,20000) #int(input("digite novamente: "))
        num_random = random.randint(1,20000)
        contador += 1
        print(num_usuario)
        print(num_random)
        print(contador)
    else:
        print("você venceu!!! aeeeee")
        break