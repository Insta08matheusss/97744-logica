import os

os.system("clear")

dia_da_semana = int(input("Qual dia da semana desejado?: "))


match dia_da_semana:
    case 1 :
       dia = "1"
       final = " 1 - Janeiro"
    case 2 :
       dia = "2"
       final = "Fevereiro"
    case 3:
         dia = "3"
         final = "Março"
    case 4:
        dia = "4"
        final = "Abril"
    case 5:
        dia = "5"
        final = "Maio"
    case 6:
        dia = "6"
        final = "Junho"
    case 7:
        dia = "7"
        final = "Julho"
    case 8 :
       dia = "8"
       final = "Agosto"
    case 9 :
       dia = "9"
       final = "Setembro"
    case 10:
         dia = "10"
         final = "Outubro"
    case 11:
        dia = "11"
        final = "Novembro"
    case 12:
        dia = "12"
        final = "Dezembro"
    case _:
        dia = "Invalido"
        final = 0

print()

print(f"Mês: {dia}")
print(f"Resultado: {final}")
