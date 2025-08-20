# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "❌ Error: División por cero"
    return a / b

def mostrar_historial(historial):
    print("\n📜 Historial de operaciones:")
    for i, operacion in enumerate(historial, 1):
        print(f"{i}. {operacion}")
    print()

def main():
    historial = []
    while True:
        print("\nSelecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver historial")
        print("6. Salir")

        opcion = input("👉 Opción (1-6): ")

        if opcion == "6":
            print("👋 ¡Hasta luego!")
            break
        elif opcion == "5":
            mostrar_historial(historial)
            continue

        try:
            a = float(input("🔢 Ingresa el primer número: "))
            b = float(input("🔢 Ingresa el segundo número: "))
        except ValueError:
            print("⚠️ Entrada inválida. Usa números.")
            continue

        if opcion == "1":
            resultado = sumar(a, b)
            operacion = f"{a} + {b} = {resultado}"
        elif opcion == "2":
            resultado = restar(a, b)
            operacion = f"{a} - {b} = {resultado}"
        elif opcion == "3":
            resultado = multiplicar(a, b)
            operacion = f"{a} * {b} = {resultado}"
        elif opcion == "4":
            resultado = dividir(a, b)
            operacion = f"{a} / {b} = {resultado}"
        else:
            print("❌ Opción inválida.")
            continue

        print(f"✅ Resultado: {resultado}")
        historial.append(operacion)

if __name__ == "__main__":
    main()