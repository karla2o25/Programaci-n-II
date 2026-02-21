import time
inicio = time.time()
for i in range(64):
    print(2 ** i)
fin = time.time()
tiempo_total = fin - inicio
print(f"\nEl proceso tardó: {round(tiempo_total,6)} segundos")
