import os

os.system ("clear")

valor = float(input("Qual valor da sua compra?: "))

print("""
=========== MENU ==========
Código   \tForma de Pagamento        
1                Debito  
2                Crédito      
""")

pagamento = int(input("Debito ou Crédito?: "))

match pagamento:

    case 1:
        codigo = 1
        resultado = "Debito"
        debito = (valor * 0.10)
        print (f"Valor : {debito}")
        print (f"Valor : {debito}")

    case 2:
        codigo = 2
        resultado = "Crédito"
        parcelas = int(input("Digite a quantidade de parcelas em até 6 vezes: "))
        credito = (valor / parcelas)
        print (f"Valor : {credito}")

    case _:
        resultado = "Invalido!"











