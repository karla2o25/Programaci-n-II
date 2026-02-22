#Complejidades
#Complejidad constante
print("Complejidad constante: Búsqueda en una lista")
def obtener_numero(list):
    return list[0]

list = [2,4,6,8,10,12,14,16,18,20,22]
print(*list)
print(f"{obtener_numero(list)}")
print()

#Complejidad logarítmica
print("Complejidad logarítmica: Búsqueda binaria ")
datos = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
buscar = 18

def busqueda(lista, elemento):
    inicio = 0
    final = len(lista)-1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == elemento:
            return True
        elif lista[medio] < elemento:
            inicio = medio + 1
        elif lista[medio] > elemento:
            final = medio - 1
    return False
print(f"{datos}\nNúmero a buscar 18")
print(busqueda(datos, buscar))
print()

#Complejidad lineal
print("Complejidad lineal: Suma")
def suma_total(lista):
    total = 0
    for numero in lista:
        total = total + numero
    return total
numeros = [10, 20, 30, 40, 50]
print(f"{numeros}\nLa suma es: {suma_total(numeros)}\n")

#Complejidad cuasi-lineal
print("Complejidad cuasi-lineal: ")
def ordenar(lista):
    lista.sort()
    return lista
letras = ["C", "B", "A"]
print(letras)
print(f"Ordenado: {ordenar(letras)}")
print()

#Complejidad cuadrática
print("Complejidad cuadrática: Sumar dos números de una lista que den como resultado la cantidad deseada")
cantidades = [45, 23, 60, 12, 15, 20, 10, 1, 2, 32]
numero = 55
def suma_dos(lista, valor):

    pares = []
    for i in lista:
        for j in lista:
            if i + j == valor:
                pares.append([i, j])
                print(i,j)
    return pares
print(suma_dos(cantidades, numero))
print()

#Complejidad exponencial
print("Complejidad exponencial: ")
def suma(lista, n, objetivo):
    if objetivo == 0:
        return True
    if n == 0:
        return False

    opcion_ignorar = suma(lista, n - 1, objetivo)

    opcion_incluir = False
    if lista[n - 1] <= objetivo:
        opcion_incluir = suma(lista, n - 1, objetivo - lista[n - 1])

    return opcion_ignorar or opcion_incluir

numeros = [3, 34, 4, 12]
print(f"{numeros}\n¿Usando los elementos de la lista se puede formar el 9?")
print(suma(numeros, len(numeros), 9))
print()

#Complejidad factorial
print("Complejidad factorial: Permutaciones")
def generar_permutaciones(lista):
    if len(lista) <= 1:
        return [lista]

    resultado = []
    for i in range(len(lista)):
        elemento_actual = lista[i]
        restantes = lista[:i] + lista[i + 1:]

        for l in generar_permutaciones(restantes):
            resultado.append([elemento_actual] + l)

    return resultado

mi_lista = [1, 2, 3]
print(mi_lista)
print(generar_permutaciones(mi_lista))
print()
