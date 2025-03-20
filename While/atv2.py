import os
os.system("clr || clear")



while True:
     nota = float(input("Digite sua primeira nota: "))
     
     
     if nota  > 10:
           print("Nota errada!\n") 
           
     elif nota < 0:
           print("Nota errada!\n")
            
     else:
           break
     
while True:
     notaa = float(input("Digite sua segunda nota: "))

     
     if notaa > 10:
           print("Nota errada!\n") 
           
     elif notaa < 0:
           print("Nota errada!\n")
           
     else:
           break
     
     
media = (nota + notaa) / 2

    


print(f"Primeira nota: {nota}")
print(f"Segunda nota: {notaa}")
print(f"Média: {media}")
print("Fim!")  

