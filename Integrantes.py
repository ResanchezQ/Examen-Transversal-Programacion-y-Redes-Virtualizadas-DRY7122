print("#Esta es una lista de la informacion de los estudiantes#")
print("Eliga las siguientes opciones:")
while True:

    print("Marque 1 si desea ver los nombres de los estudiantes:")
    print("Marque 2 si desea ver los apellidos de los estudiantes:")
    print("Marque 3 si desea ver los rut de los estudiantes:")
    print("Marque 4 si desea ver toda la informacion de los estudiantes:")

    Opcion = int(input("Ingrese el numero de la opcion que quiera utilizar:"))


    if Opcion == 1:
        print("Renato Joaquin")
        print("Rodrigo Andres")
        print("Martin Alonso")

    elif Opcion == 2:
        print("Sanchez Quintanilla")
        print("Mardones Almarza")
        print("Ballesteros Escarate")

    elif Opcion == 3:
        print("21.291.278-6")
        print("21.173.359-4")
        print("21.173.179-6")

    elif Opcion == 4:
        print("Renato Joaquin, Sanchez Quintanilla, 21.291.278-6 ")
        print("Rodrigo Andres, Mardones Almarza, 21.173.359-4  ")
        print("Martin Alonso, Ballesteros Escarate, 21.173.179-6")

    else:
        Opcion <=6
        print("Opcion no valida")
        print("Ingrese un valor correcto")

    respuesta = input("¿Desea realizar otra consulta? (s/n): ")
    if respuesta.lower() != 's':
        print("Saliendo del Script")
        break  
    