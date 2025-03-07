import os
os.system ("clear")

primeiro_numero = int("Digite o primeiro número: ")
segundo_numero = int("Digite o sengundo número: ")
terceiro_numero = int("Digite o terciro numero: ")

maior_numero = max(primeiro_numero, segundo_numero, terceiro_numero)
menor_numero = min(primeiro_numero, segundo_numero, terceiro_numero)

if primeiro_numero ==  segundo_numero == terceiro_numero:
    print(f"Os números são iguais")
else:
    print (f"Maior número: {maior_numero}")
    print (f"Menor número: {menor_numero}")