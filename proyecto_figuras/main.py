#menú
from cuadrado import Cuadrado
from triangulo import Triangulo
from circulo import Circulo

def menu():

    while True:
        print("\n--- MENÚ DE FIGURAS ---")
        print("1. Cuadrado")
        print("2. Círculo")
        print("3. Triángulo")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            l = float(input("Ingresa el lado: "))
            fig = Cuadrado(l)

        elif opcion == "2":
            r = float(input("Radio del círculo: "))
            fig = Circulo(r)

        elif opcion == "3":
            b = float(input("Ingresa la base: "))
            h = float(input("Ingresa la altura: "))
            l1 = float(input("Ingresa del lado 1: "))
            l2 = float(input("Ingresa del lado 2: "))
            l3 = float(input("Ingresa el lado 3: "))
            fig = Triangulo(b, h, l1, l2, l3)
        
        elif opcion == "4":
            print("Programa finalizado")
            break

        else:
            print("Opción inválida, intenta de nuevo")
            continue

        print(f"\nResultados: ")
        print(f"El área es: {fig.CalcularArea():.2f}")
        print(f"El perímetro es: {fig.CalcularPerimetro():.2f}")

if __name__ == "__main__":
    menu()
    