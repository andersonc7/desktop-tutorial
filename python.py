def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Solo se pueden ingresar números.")

def sumar():
    a = obtener_numero("Ingresa el primer número: ")
    b = obtener_numero("Ingresa el segundo número: ")
    print(f"✅ Resultado: {a} + {b} = {a + b}")

def restar():
    a = obtener_numero("Ingresa el primer número: ")
    b = obtener_numero("Ingresa el segundo número: ")
    print(f"✅ Resultado: {a} - {b} = {a - b}")

def multiplicar():
    a = obtener_numero("Ingresa el primer número: ")
    b = obtener_numero("Ingresa el segundo número: ")
    print(f"✅ Resultado: {a} × {b} = {a * b}")

def dividir():
    a = obtener_numero("Ingresa el primer número: ")
    b = obtener_numero("Ingresa el segundo número: ")
    if b == 0:
        print("❌ Error: No se puede dividir sobre cero.")
    else:
        print(f"✅ Resultado: {a} / {b} = {a / b}")

def cuadrado():
    a = obtener_numero("Ingresa el número: ")
    print(f"✅ Resultado: {a}² = {a ** 2}")

def cubo():
    a = obtener_numero("Ingresa el número: ")
    print(f"✅ Resultado: {a}³ = {a ** 3}")

def menu():
    while True:
        print("\n========== CALCULADORA ==========")
        print("1. Sumar         (2 números)")
        print("2. Restar        (2 números)")
        print("3. Multiplicar   (2 números)")
        print("4. Dividir       (2 números)")
        print("5. Cuadrado      (1 número)")
        print("6. Cubo          (1 número)")
        print("7. Salir")
        print("=================================")

        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            dividir()
        elif opcion == "5":
            cuadrado()
        elif opcion == "6":
            cubo()
        elif opcion == "7":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Elige entre 1 y 7.")

if __name__ == "__main__":
    menu()
