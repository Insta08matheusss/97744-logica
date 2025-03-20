import os
os.system("clr || clear")



while True:
     nota = float(input("Digite sua nota: "))

     if nota > 10:
           print("Nota errada!") 
           print(f"Nota: {nota} \n")
     elif nota < 0:
           print("Nota errada!")
           print(f"Nota: {nota}\n")  
     else:
           break
     

print(f"Nota: {nota}")
print("Fim!")  