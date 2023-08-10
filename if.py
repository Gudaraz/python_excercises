edad = int(input("Introduzca su edad. \n"))

respuesta = None

if edad > 18:
    print("Ud. es mayor de edad, puede comprar alcohol. Elija que licor desea comprar")
    respuesta = input("1- Ginebra.\n2- Ron.\n3- Whisky.\n")
    
    if(respuesta == "1"):
        print("Ud. escogió una botella de Ginebra")
    elif(respuesta == "2"):
        print("Ud. escogió una botella de Ron")
    elif(respuesta == "3"):
        print("Ud. escogió una botella de Whisky")
    else:
        print("Opción INVALIDA")
        
else:
    print("Ud. No tiene edad para comprar, regrese cuando la cumpla, o jamás beba alcohol")
    
    