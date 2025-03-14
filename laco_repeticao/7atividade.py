import os
os.system("clear")

media = 0

for i in range(0,4):
  nota = float(input("Digite sua nota: "))
  media += nota / 4

print(f"Média: {media}")


