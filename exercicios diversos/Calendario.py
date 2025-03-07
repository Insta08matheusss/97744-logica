import os

os.system ("clear")

print("""
========== CALENDARIO ================
codigo                Dias da Semana
1                         Domingo
2                         Segunda
3                         Terça
4                         Quarta
5                         Quinta
6                         Sexta
7                         Sabado
""")

dia_da_semana = int(input("Qual dia da semana desejado?: "))


match dia_da_semana:
    case 1 :
       dia = "Domingo"
       final = "Final de semana"
    case 2 :
       dia = "Segunda"
       final = "Útil"
    case 3:
         dia = "Terça"
         final = "Útil"
    case 4:
        dia = "Quarta"
        final = "Útil"
    case 5:
        dia = "Quinta"
        final = "Útil"
    case 6:
        dia = "Sexta"
        final = "Útil"
    case 7:
        dia = "Sabado"
        final = "Final de semana"
    case _:
        dia = "Invalido"
        resultado = 0

print()
print(f"Dia da semana: {dia}")
print(f"Resultado: {final}")
print(f"Invalido {resultado}")


