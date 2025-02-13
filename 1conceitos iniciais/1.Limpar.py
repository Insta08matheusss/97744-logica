import os 

#   limpa o terminal
os.system("clear")

print("olá Mundo!!")

# Solicitar dados para o usuario 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

# Exibindo dados
print()
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"altura: {altura}")
