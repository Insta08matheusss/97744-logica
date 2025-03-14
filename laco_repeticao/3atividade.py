import os
import time 
os.system("clear")

numero = int(input("Digite um número: "))

print(f"Tabuda do número desejado {numero}: ")
for i in range(1,11):
      print(f"{numero} x {i} = {numero*i} ")