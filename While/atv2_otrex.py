import os
os.system ("clr || clear")

soma = 0 

for i in range(2):
    while True:
        nota = float(input(f"Digite a {i+1}° sua primeira nota: "))

        if nota < 0 or nota > 10:
            print("Nota invalida, tente novamente\n")
        else:
            soma += nota
        break

media = soma / 2

print(f"Média {media}")
