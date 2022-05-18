#-----------------------------------------------------------------------------
#Proceso de Validacion de datos ingresados en longitud y ancho MODELO 2 presentaedo en el informe
#-----------------------------------------------------------------------------
def validacionLongitudAncho():
    while True:
        #--------------------------------------------------------------------------
        #Sentencia/bloque try que avisará al bloque except si la opción ingresada no es valida
        #--------------------------------------------------------------------------
        try:
            #--------------------------------------------------------------------------
            #                      INGRESO DE DATOS
            #--------------------------------------------------------------------------
            longitud=int(input("Ingrese su longitud en cm: "))
            ancho=int(input("Ingrese su ancho en cm: "))
            #--------------------------------------------------------------------------
            #Condicion para saber si la longitud y ancho ingresados son mayores a 0 si se cumplen las condiciones la función perimetro será llamada
            #--------------------------------------------------------------------------
            if longitud>0 and ancho>0:
                #--------------------------------------------------------------------------
                #Llamada a la funcion perimetro
                #--------------------------------------------------------------------------
                perimetro(longitud,ancho)
                break
            else:
            #--------------------------------------------------------------------------
            #Si la longitud y ancho ingresados no son mayores a 0 se mostrará un mensaje de error
            #--------------------------------------------------------------------------
                print("POR FAVOR INGRESE VALORES POSITIVOS")
        #--------------------------------------------------------------------------
        #Sentencia/bloque except que resivirá un error de tipo ValueError si el bloque try no se cumple
        #--------------------------------------------------------------------------
        except ValueError:
            print("-----ERROR FATAL USTED INGRESÓ UNA LETRA O SIGNO, INGRESE SOLO NÚMEROS ENTEROS-------")
#--------------------------------------------------------------------------
#Función para sacar el perímetro de un rectangulo(MODELO 2 DE ALGORITMO) presentado en el informe
#--------------------------------------------------------------------------
def perimetro(longitud, ancho):
    #--------------------------------------------------------------------------
    #Fórmula para calcular el perímetro(MODELO 2 ALGEBRAICO)
    #--------------------------------------------------------------------------
    perimetro=2*(longitud+ancho)
    print("El perimetro del rectangulo es: ",perimetro)
#--------------------------------------------------------------------------
#                   Proceso donde guardará mi carátula
#--------------------------------------------------------------------------
def caratula():
    print("==========================================================")
    print("     Universidad de las fuerzas armadas ESPE-SD ") 
    print("Carrera: Ingenieria en las tecnologias de la informacion")
    print("          Luis Eduardo Guachilema Sánchez")
    print("    NRC_8161--Programación Orientada a Objetos")
    print("          Laboratorio 2 - Ejercicio 13")
    print("==========================================================")
#--------------------------------------------------------------------------
#         Proceso para el menu principal, que tendrá 3 opcines validadas
#--------------------------------------------------------------------------
def menu():
    print("==========================================================")
    print("1. Mostrar carátula----------------------------Presione 1")
    print("2. Calcular perímetro----------------------------Presione 2")
    print("3. Salir del menú------------------------------Presione 3")
    print("==========================================================")
    #--------------------------------------------------------------------------
    #Ciclo para validadar las opciones del menu
    #--------------------------------------------------------------------------
    while True:
        #--------------------------------------------------------------------------
        #Sentencia/bloque try que avisará si la opción ingresada no es valida
         #--------------------------------------------------------------------------
        try:
            opcion=int(input("Ingrese una opción: "))
            #--------------------------------------------------------------------------
            #Al precionar 1 se mostrará la carátula
            #--------------------------------------------------------------------------
            if opcion==1:
                caratula()#llamar funcion caratula
                break
            #--------------------------------------------------------------------------
            #Al precionar 2 se mostrará el perímetro
            #--------------------------------------------------------------------------
            elif opcion==2:
                validacionLongitudAncho ()#llamar funcion validacionLongitudAncho
                break
            #--------------------------------------------------------------------------
            #Al precionar 3 se terminará el programa
            #--------------------------------------------------------------------------
            elif opcion==3:
                print("Gracias por usar el programa")
                break
            else:
                print("Opción no valida")
        #--------------------------------------------------------------------------
        #Sentencia/bloque except que resivirá un error de tipo ValueError si el bloque try no se cumple
        #--------------------------------------------------------------------------
        except ValueError:
            #--------------------------------------------------------------------------
            #Mensaje de error si ingresa un dato distinto a un número entero
            #--------------------------------------------------------------------------
            print("==========================================================")
            print("      Error de excepción tipo --ValueError--")
            print("             Vuelva a intentarlo")
            print("==========================================================")    

#--------------------------------------------------------------------------
#         Llamado a la funcion menu
#--------------------------------------------------------------------------
menu()