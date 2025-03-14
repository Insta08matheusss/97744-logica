import os
import time 
os.system("clear")

print("Números impares de 1 a 20")
for i in range(1, 21):
   if i % 2 == 1:
      time.sleep(0.5)
      print(f"Número: {i}")