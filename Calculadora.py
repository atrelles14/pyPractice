def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."

while True:
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = int(input("Selecciona una opción: "))
    
    if opcion == 5:
        break
    
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    if opcion == 1:
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        resultado = resta(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == 4:
        resultado = division(num1, num2)
        print("El resultado de la división es:", resultado)
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
    
    print()
