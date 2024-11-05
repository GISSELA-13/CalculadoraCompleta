# Integrantes:
# Fares Zuñiga
# Camilo Hernandez
# Andres Bravo
# Enrique Miranda
# Gissela Granados
def potencia(base, exponente):
    return 

def multiplicar(n1, n2):
    return 

def restar(num1, num2):
    return num1 - num2

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return

def sumar(a, b):
    return

def main():
    while True:
        print("\nSeleccione una operación:")
        print("1. Potencia")
        print("2. Multiplicación")
        print("3. Resta")
        print("4. División")
        print("5. Suma")
        print("6. Salir")

        opcion = input("Ingrese el número de la operación que desea realizar (1/2/3/4/5/6): ")

        if opcion == '6':
            print("¡Gracias por usar la calculadora!")
            break

        try:
            if opcion == '1':
                base = float(input("Introduce la base: "))
                exponente = float(input("Introduce el exponente: "))
                resultado = potencia(base, exponente)
                print(f"{base} elevado a la {exponente} es: {resultado}")

            elif opcion == '2':
                n1 = float(input("Ingrese el primer número: "))
                n2 = float(input("Ingrese el segundo número: "))
                resultado = multiplicar(n1, n2)
                print(f"La multiplicación es: {resultado}")

            elif opcion == '3':
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                resultado = restar(num1, num2)
                print(f"La resta es: {resultado}")

            elif opcion == '4':
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                resultado = dividir(num1, num2)
                print(f"El resultado de la división es: {resultado}")

            elif opcion == '5':
                a = float(input('Introduce el primer número: '))
                b = float(input('Introduce el segundo número: '))
                resultado = sumar(a, b)
                print(f'La suma de {a} y {b} es: {resultado}')

            else:
                print("Opción no válida. Intente de nuevo.")

        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()