# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''


print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

primer_numero = int(input("Ingrese el primer numero a calcular: "))
segundo_numero = int(input("Ingrese el segundo numero a calcular: "))
print("Presione:")
print("         + Suma")
print("         - Resta")
print("         * Multiplicación")
print("         / Division")
print("         ** Exponente/Potencia")
print("         'FIN' Para cerrar la calculadora.")
operacion = str(input("Que operación que se desea ejecutar? "))
while True:

    if operacion == "+":
        print("El resultado de la suma es: ", primer_numero + segundo_numero)
    elif operacion == "-":
        print("El resultado de la resta es: ", primer_numero - segundo_numero)
    elif operacion == "*":
        print("El resultado de la multiplicación es: ", primer_numero * segundo_numero)
    elif operacion == "/":
        print("El resultado de la división es: ", primer_numero / segundo_numero)
    elif operacion == "**":
        print("El resultado de la potencia es: ", primer_numero ** segundo_numero)
    elif operacion == "FIN" or "fin":
        print("Cerrando calculadora")
    else:
        print("Operación no válida")
    break
