from Validar import validarRut, contraseña


def main():

    
    '''
    Actualizacion: Tarea 2 miercoles 17-11-2021
    OK - 1. - Utilizar variables y no listas para almacenar los datos.
    OK - 2. - Contraseña de ingreso para mostrar datos (solo para mostrar datos). Utilizando funcion en el archivo validar.py
    Por hacer 3. - No permitir el registro de un usuario si el nombre es vacio y si el rut es invalido.
    OK - 4. - Validar que el nombre, rut y nacionalidad sean string y la edad un entero.
    OK - 5. - Transformar el nombre y la nacionalidad a mayusculas cuando se imprima.
    OK - 6. - Utilizar la funcion main para iniciar el programa.
    '''

    '''
    Actualizacion: Tarea 2 lunes 22
    1. - Utilizar funcion contraseña del archivo validar.
    2. - Ofrecer opcion para salir del ingreso de contrasena cuando esta no es valida. 
    3. - No permitir el registro de un usuario si el nombre es vacio y si el rut es invalido.
    4. - Agregar sexo a la definicion, pero debe ofrecerse a través de opciones y no ingresarlo a mano
    5. - Cambiar edad por año de nacimiento y calcular la edad y mostrarla. Este calculo debe hacerse en una funcion.    
    '''

    Nombre = ()
    RUT = ()
    edad = ()
    nacionalidad = ()
    contraseña = ""
    menupersona = 50000000
    while menupersona != 0:


            menupersona = int(input("Bienvenido al menu: \n 1- Ingrese sus datos \n 2- Imprimir los datos ingresados \n 0- Salir del programa \n ingrese su opcion :"))
            if menupersona == 1:
                
                contraseña = input("Cree su contraseña: ")
                contra = contraseña
                print("Ingrese Nombre:")
                Nombre = str((input("Nombre del usuario: ")))
                print("Ingrese RUT:")
                Rut = (str(input("RUT del usuario: ")))
                validaRUT = validarRut(Rut)
                if(validaRUT == True):
                    print("RUT VALIDO")
                else:
                    print("RUT Invalido")
                print("Ingrese edad:")
                edad = int(input("edad del usuario: "))
                print("Ingrese nacionalidad: ")
                nacionalidad = str(input("Nacionalidad del usuario: "))

            elif menupersona == 2:
                contra = input("ingresa la contraseña: ")
                while contra != contraseña:
                    print("La contraseña es invalida")
                    contra = input("Prueba nuevamente: ")
                print("Contraseña correcta, devuelve datos ")
                
                print("Mostrar todos los datos ingresados")
                if(Nombre == ""):
                    print("El nombre es obligatorio")
                else:
                    print(Nombre.upper(), Rut, edad, nacionalidad.upper())

            else:
                print("digite una opcion valida")


if __name__== "__main__":
  main()