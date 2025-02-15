import os 

os.system("clear")

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
terceira_nota = float(input("Digite sua terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) /3

print()
print ("Sua média é: ", media)

if media == 7:
    print("Aprovado")
elif media > 7:
    print("Aprovado")
else:
    print("Reprovado")


    






