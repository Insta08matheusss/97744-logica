import os
os.system ("clr || clear")

loginn = "Matheus"
senhaa = "1234"

for i in range (3): 
    login = input("Digite o login: ").lower
    senha = input("Digite a senha: ").lower

    if loginn == login and senhaa == senha:
        print("Bem vindo!")
        break
    else:
        print("Acesso negado. \ntente novamente")

