import os 
os.system("cls || clear")

idade = int(input("Digite sua idade: "))

while idade < 18:
    print("Não autorizado! \nSomente maior de 18 \n")
    idade = int(input("Digite sua idade: "))

print("Acesso permitido")
print("Fim!")  