import os

os.system("clear")

primeira_nota = int(input("Digite seu primeiro número: "))
segunda_nota = int(input("Digite seu sengundo número: "))

media =  (primeira_nota + segunda_nota) /2
2
soma = (primeira_nota + segunda_nota)
produto = (primeira_nota * segunda_nota)
maior_numero = max(primeira_nota, segunda_nota)
menor_numero = min(primeira_nota, segunda_nota)
numeros_iguais = (primeira_nota == segunda_nota)

print()
print ("A média é: ", media)
print ("A soma é: ", soma)
print ("O produto é: ", produto)

if maior_numero ==  menor_numero:
    print(f"Os números são iguais")
else:
    print (f"Maior número: {maior_numero}")
    print (f"Menor número: {menor_numero}")


