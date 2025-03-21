import os
os.system ("clr || clear")

soma = 0
contador = 0

while True:
    
    nota = int(input("Qual nota você deseja inserir? "))
    soma += nota
    contador += 1
    if nota < 0:
        print("Digite apenas números positivos!")
        break
    responder = input("Deseja colocar outra nota 's' ou 'n'")
    if responder == "n":
        break
    
    
       

total = soma / contador

print()
print(f"Total: {total}")
