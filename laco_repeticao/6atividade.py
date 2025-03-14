import os
os.system("clear")

pares = 0
impares = 0

for i in range(0,5):
    input("Digite um número: ")
    if i % 2 == 0:
       pares += 1
    else:
        impares+= 1
     


print(f"Imparares: {impares}")
print(f"Pares: {pares}")
    