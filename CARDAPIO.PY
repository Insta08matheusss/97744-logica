import os 
os.system("clr || clear")

valor_total = 0
print("""

=========== MENU ==========
Código   \tPrato        \tValor
1         \tFeijoada      \t50,00
2          \tLasanha      \t70,00
3           \tStrogonoff   \t15,00
4            \tPizza     \t 80,00
5             \tEscondidinho  \t30,00

""")

while True:
    codigo = int(input("Qual comida você deseja? "))

    match codigo:
        case 1:
            prato = "feijoada"
            valor = 50.00
        case 2:
            prato = "lasanha"
            valor = 70.00
        case 3:
            prato = "strogonoff"
            valor = 15.00
        case 4:
            prato = "pizza"
            valor = 80.00
        case 5:
            prato = "Escondidinho"
            valor = 30.00
        
    print()
    print(f"Prato: {prato}")
    print(f"Valor: {valor}")

    break

valor_total += valor