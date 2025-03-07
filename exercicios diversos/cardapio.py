import os

os.system("clear")
print("""

=========== MENU ==========
Código   \tPrato        \tValor
1         \tFeijoada      \t50,00
2          \tLasanha      \t70,00
3           \tStrogonoff   \t15,00
4            \tLasanha  \t 15,00
6             \tEscondidinho  \t30,00

""")
opcao = int(input("Digete sua opção desejada: "))

match opcao:
    case 1 :
       prato = "Feijoada"
       valor = "50,00"
    case 2 :
       prato = "Lasanha"
       valor = "70"
    case 3:
         prato = "Strogonoff"
         valor = "15,00"
    case 4:
        prato = "Lasanha"
        valor = "15,00"
    case 5:
        prato = "Escondidinho"
        valor = "30,00"
        
print()
print(f"Prato: {prato}")
print(f"Valor: R$ {valor}")

    


    



 