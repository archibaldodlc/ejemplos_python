from validar import validarRut

menupersona = int(input("Bienvenido al menu: \n 1- Ingrese sus datos \n 2- Imprimir los datos ingresados \n 0- Salir del programa \n ingrese su opcion :"))

'''
Actualización
1. - Utilizar variables y no listas para almacenar los datos 
2. - Contraseña de ingreso para mostrar datos (solo para mostrar datos)
3. - No permitir el registro de un usuario si el nombre es vacío y si el rut es invalido
4. - Validar que el nombre, rut y nacionalidad sean string y la edad un entero.

And
v*v=V
v*f=F
f*v=F
f*f=F

Or
v*v=V
v*f=V
f*v=V
f*f=F

'''


Nombre = []
RUT = []
edad = []
nacionalidad = []

while menupersona != 0:


        if menupersona == 1:
            print("Ingrese Nombre:")
            Nombre.append(input("Nombre del usuario: "))
            print("Ingrese RUT:")
            Rut = (str(input("RUT del usuario: ")))
            validaRUT = validarRut(Rut)
            if(validaRUT == True):
                print("RUT VALIDO")
            else:
                print("RUT Invalido")
            print("Ingrese edad:")
            edad.append(int(input("edad del usuario: ")))
            print("Ingrese nacionalidad: ")
            nacionalidad.append(input("Nacionalidad del usuario: "))

            menupersona = int(input("Bienvenido al menu: \n 1- Ingrese sus datos \n 2- Imprimir los datos ingresados \n 0- Salir del programa \n ingrese su opcion :"))

        elif menupersona == 2:
            print("Mostrar todos los datos ingresados")
            if(Nombre == ""):
                print("El nombre es obligatorio")
            else:
                print(Nombre, Rut, edad, nacionalidad)

            menupersona = int(input("Bienvenido al menu: \n 1- Ingrese sus datos \n 2- Imprimir los datos ingresados \n 0- Salir del programa \n ingrese su opcion :"))

        else:
            print("digite una opcion valida")

            menupersona = int(input("Bienvenido al menu: \n 1- Ingrese sus datos \n 2- Imprimir los datos ingresados \n 0- Salir del programa \n ingrese su opcion :"))