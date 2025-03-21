import os
os.system ("clr || clear")

soma = 0
contador = 0

while True:
    
    nota = float(input("Qual nota você deseja inserir? "))
    soma += nota
    contador += 1
    
    responder = input("Deseja colocar outra nota 's' ou 'n'")
    if responder == "n":
        break
       

total = soma / contador

print()
print(f"Total: {total}")