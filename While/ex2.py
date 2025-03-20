import os
os.system("clr || clear")

while True:
     idade = int(input("Digite sua idade: "))

     if idade < 18:
           print("Não autorizado! \nSomente maior de 18 \n")
     else:
           break
     

print("Acesso permitido")
print("Fim!")  