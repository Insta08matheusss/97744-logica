import os
import time
os.system ("clear")

print("Apenas números pares.")
for i in range(100, 121, 2):
   time.sleep(0.5)
   print(f"Número {i}")

# outra maneira
os.system("clear")

print("Pares de 100 até 120")
for i in range(100, 121):
   if i % 2 == 0:
      time.sleep(0.5)
      print(f"Número: {i}")
