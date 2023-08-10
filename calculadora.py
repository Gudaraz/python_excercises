print(" --- Calculadora --- ")

print("Escoja la operación a realizar: ")

opcion = input("1- Sumar.\n2- Restar.\n3- Multiplicar.\n4- Dividir.\n")
opcion = None

if(opcion == "1"):
    print("Ha escogido realizar una suma")
    numero1 = int(input("Introduzca el primer número.\n"))
    numero2 = int(input("Introduzca el segundo número.\n"))
    print(f"El resultado de sumar {numero1} y {numero2} es la cantidad de: {numero1 + numero2}")
    
elif(opcion == "2"):
    numero1 = int(input("Introduzca el primer número.\n"))
    numero2 = int(input("Introduzca el segundo número.\n"))
    print(f"El resultado de la resta es: {numero1 - numero2}")
    
elif(opcion == "3"):
    numero1 = int(input("Introduzca el primer número.\n"))
    numero2 = int(input("Introduzca el segundo número.\n"))
    print(f"El resultado de la multiplicación es: {numero1 * numero2}")
    
elif(opcion == "4"):
    numero1 = int(input("Introduzca el primer número.\n"))
    numero2 = int(input("Introduzca el segundo número.\n"))
    print(f"El resultado de la división es: {numero1 / numero2}")
    
else:
    print("Ha escogido una opción invalida. Inténtelo nuevamente.")