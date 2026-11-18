# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

#print(f"Conocer cual es el numero mayor")

#numero_1= int(input("Ingrese el primer numero: "))
#numero_2 = int(input("Ingrese el segundo numero: "))

#if numero_1 > numero_2:
#    print(f"El numero mayor es el numero {numero_1}")
#elif numero_1 < numero_2:
#     print(f"El numero mayor es el numero {numero_2}")
#else:
#    print(f"Los numeros son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

#primer_numero = int(input("Ingrese un numero: "))
#segundo_numero = int(input("Ingrese otro numero: "))
#operacion = input("Ingrese la operacion que desea realizar \n 1.- Sumar \n 2.-Restar \n 3.-Multiplicar \n 4.-Dividir primero numero entre segundo numero \n 5.-Salir \n")

#if operacion == "1":
#    sumatoria = primer_numero + segundo_numero
#    print(f"el resultado es {sumatoria}")
#elif operacion == "2":
#    resta = primer_numero - segundo_numero
#    print(f" el resultado es {resta}")
#elif operacion == "3":
#    multiplicar = primer_numero * segundo_numero
#    print(f" el resultado es {multiplicar}")
#elif operacion == "4":
#    dividir = primer_numero / segundo_numero
#    print(f"el resultado es {dividir}")
#elif operacion == "5":
#    print("has salido de la calculadora")
#else:
#    print("no ha ingresado una opcion valida")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

#año = int(input("Introduce un año: "))

#if año % 4 == 0 or año % 400 == 0:
#    print(f"el año es bisiesto")
#elif año % 100 == 0:
#    print(f"el año no es bisiesto")
#else:
#    print(f"el año no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

#print(f"Vamos a Conocer la categoria de una persona según su edad")

#edad = int(input("Introduce la edad: "))

#if edad < 0:
#    print(f"ha introducido un valor erroneo")
#elif edad <=2:
#    print(f"Su categoria es de bebé")
#elif edad <= 12:
#    print(f"Su Categoria es de niño")
#elif edad <= 17:
#    print(f"su categoria es de adolescente")
#elif edad <= 64:
#    print(f"Su Categoria es de adulto")
#elif edad >= 65 and edad < 120:
#    print(f"Su Categoria es de adulto mayor")
#else:
#    print(f"la edad introducida es invalida")
