import os
os.system ("clr || clear")

loguinn = "Matheus"
senhaa = "1234"

while True:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if loguinn == login and senhaa == senha:
        print("Bem vindo!")
        break
    else:
        print("Acesso negado. \ntente novamente")