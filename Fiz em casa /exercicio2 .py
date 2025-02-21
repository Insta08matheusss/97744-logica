import os

os.system ("clear")

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite outro número: "))

maior_numero = max(primeiro_numero, segundo_numero)
menor_numero = min(primeiro_numero, segundo_numero)

if primeiro_numero ==  segundo_numero:
    print(f"Os números são iguais")
else:
    print (f"Maior número: {maior_numero}")
    print (f"Menor número: {menor_numero}")