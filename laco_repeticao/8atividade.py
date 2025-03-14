import os
os.system("clear")

media = 0

for i in range(0,3):
  nota = float(input("Digite sua nota: "))
  media += nota / 3

if media >= 7:
    print("Aprovado!")
elif media < 4:
     print("Reprovado!")
else:
    print("Recuperação!")     

print(f"Média: {media}")