import os
os.system ("clear")

nome = input("Qual produto você deseja? ")
quantidade = int(input("Qual quantidade do produto? "))
preco = float(input("Qual valor do produto? "))

total = quantidade * preco
desconto = total -