from funciones import suma, resta, multiplicacion, division

def main():

    while True:
        print("Que operacion desea realizar")
        print("0 - Salir del programa")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicacion")
        print("4 - Division")
        operacion = int(input("Ingrese opcion [1-4]:"))
        
        if(operacion == 0):
            break

        A = int(input("Ingrese el primer numero : "))
        B = int(input("Ingrese el segundo numero : "))

        if(operacion == 1):
            resultado = suma(A,B)
        elif(operacion == 2):
            resultado = resta(A,B)
        elif(operacion == 3):
            resultado = multiplicacion(A,B)
        elif(operacion == 4):
            resultado = division(A,B)
        
        print("El resultado es: " + str(resultado))

if __name__== "__main__":
  main()

