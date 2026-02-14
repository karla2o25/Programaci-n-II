#Tarea 3
A = int(input("Ingresa en primer número: "))
B = int(input("Ingresa el segundo número: "))
C = int(input("Ingresa el tercer número: "))
suma = A + B + C
prom = suma / 3
print(f"Suma = {suma}\nPromedio: {round(prom, 1)}")
if A >= B and A >= C:
    print(f"El número mayor es: {A}")
elif B >= A and B >= C:
    print(f"El número mayor es: {B}")
else:
    print(f"El número mayor es: {C}")