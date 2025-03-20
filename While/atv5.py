import os
os.system("clr || clear")

quantidade_notas = 3
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite a {i+1}° sua primeira nota: "))

        if nota < 0 or nota >10:
            print("Nota invalida, tente novamente.\n")
        else:
            soma += nota
            break


media = soma / quantidade_notas

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")
    


