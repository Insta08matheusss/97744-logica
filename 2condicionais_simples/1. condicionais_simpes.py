import os

os.system("Clear") # Limpra o terminal

#solicitando dados (Entrada)
idade = int(input("Digite sua idade: "))

# Verificando (processamento)
# se idade < 18 entao
#       escreval("Acesso negado!")
# fimse

if idade < 18: 
    print("Acesso Negado")

if idade >=18:
     print("Acesso Permitido")

# Exibindo dados (Saída)
print("--FIM--")
