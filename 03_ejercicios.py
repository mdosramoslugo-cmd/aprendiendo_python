# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

#numero = 10
#while numero <= 10 and numero >= 0:
#    print(numero)
#    numero = numero - 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

#numeros_pares = 2
#suma_numeros_pares = 0

#while numeros_pares <= 20 and numeros_pares >= 0:
#    suma_numeros_pares = suma_numeros_pares + numeros_pares
#    numeros_pares = numeros_pares+2
#    print(suma_numeros_pares)



#Intenta modificar el ejercicio para calcular la suma de todos los números impares entre 1 y 20, utilizando while.

#numeros_impares = 1
#suma_numeros_impares = 0

#while numeros_impares <= 20:
#    suma_numeros_impares = suma_numeros_impares + numeros_impares
#    numeros_impares = numeros_impares + 2
#   print(suma_numeros_impares)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

#numero = int(input("Ingrese un numero entero positivo: "))
#factorial_numero = 1

#while numero > 0:
#    factorial_numero = factorial_numero * numero
#    numero = numero - 1

#print(factorial_numero)


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

#contrasena = input("Introduce la contraseña:")

#while len(contrasena) < 8:
#    print(f"la contraseña debe tener al menos 8 caracteres")
#    contrasena = input("Introduce la contraseña:")
#print(f"contraseña valida")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

#numero = int(input("Ingrese un numero: "))
#multiplicador = 0

#while multiplicador < 10:
#    multiplicador = multiplicador + 1
#    tabla_multiplcador = numero * multiplicador
#    print(f"{numero}*{multiplicador}={tabla_multiplcador}")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

#numero = int(input("Ingrese un numero entero positivo: "))
#contador = 2

#while contador <= numero:
#    divisor = 2
#    es_primo = True

#    while divisor < contador:
#        if contador % divisor == 0:
#            es_primo = False
#            break

#        divisor += 1
#    if es_primo:
#        print(f"El numero {contador} es primo")
#    contador += 1

