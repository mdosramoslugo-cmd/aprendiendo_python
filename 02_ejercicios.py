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



###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

#mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

#print(mensaje[7:])

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

#numeros = [10, 20, 30, 40, 50]

#numeros[0] = 50
#numeros[-1] = 10
#print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

#pan = ["pan arriba"]
#ingredientes = ["jamón", "queso", "tomate"]
#pan_abajo = ["pan abajo"]

#sandwich = [pan,ingredientes,pan_abajo]
#print(sandwich)


# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

#lista = [1, 2, 3]
#copia_lista =lista + lista
#print(copia_lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

#lista = [10, 20, 30, 40, 50]
#print(lista[2])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6]
lista_1 = lista[2::-1] + lista[3:]
print(lista_1)