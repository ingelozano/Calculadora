import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def exponente(a, b):
    return a ** b

def raiz_cuadrada(a):
    return math.sqrt(a)

# Función principal para realizar operaciones
def calcular():
    print("Calculadora básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponente")
    print("6. Raíz cuadrada")
    print("7. Valor de π")
    
    opcion = input("Elije una operación (1/2/3/4/5/6/7): ")
    
    if opcion not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Opción inválida")
        return
    
    num1 = float(input("Ingresa el primer número: "))
    
    if opcion == '6':
        resultado = raiz_cuadrada(num1)
    elif opcion == '7':
        resultado = math.pi
    else:
        num2 = float(input("Ingresa el segundo número: "))
        if opcion == '1':
            resultado = sumar(num1, num2)
        elif opcion == '2':
            resultado = restar(num1, num2)
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
        elif opcion == '4':
            resultado = dividir(num1, num2)
        else:
            resultado = exponente(num1, num2)
        
    print("El resultado es:", resultado)

# Llamamos a la función principal
calcular()
