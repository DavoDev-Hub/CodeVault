'''
Escribe un código que te pida un nombre válido, hasta que lo ingreses.
En este problema un nombre se considera válido cuando solo contiene letras 
del abecedario y espacios en blanco, la primera letra en cada palabra es mayúscula
y las demás son minúsculas.
'''
'''

'''


'''
Realizar dos códigos uno que devuelva la suma de dos números ingresados por el usuario. 
Sin embargo, el primero sume los números cuando todavía son tipo str, y el segundo código 
que los sume después de haberlos convertido a tipo int.  
'''

'''
num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))
print(num1+num2)
'''

'''
num1 = input('Ingresa el primer numero: ')
num2 = input('Ingresa el segundo numero: ')
print(num1+num2)
'''

'''
Programa un código que reciba dos números y depués imprima si el primer número es menor, igual o mayor al segundo número
'''
'''
num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))

if num1 > num2 : print('Primer numero es mayor')
elif num1 == num2 : print('Son iguales')
else: print('El segundo numero es mayor')
'''

'''
Dado un numero entero, determina si es par o impar
'''
'''
while True:
    num = int(input('Ingresa un numero par: '))
    if num % 2 == 0: 
        print('Par')
        break 
    else:
        print('Impar')
'''

'''
Escribe un código que pregunte la fecha de tu cumpleaños (día y mes) y 
la fecha de hoy (día y mes). Si ambas fechas coinciden imprime "Feliz Cumpleaños", 
si no, imprime "Feliz no Cumpleaños"
'''
'''
diaCum = int(input('ingresa el dia de tu cumpleaños: '))
mesCum = input('Ingresa el mes de tu cumpleaños: ').lower()

diaHoy = int(input('Ingresa el dia de hoy: '))
mesHoy = input('Ingresa el mes de hoy: ').lower()

if (diaCum == diaHoy) and (mesCum == mesHoy): print('Feliz cumpleaños')
else: print('Feliz no cumpleaños')
'''


'''
Escribe un programa que reciba 3 numeros enteros. Determina si al 
realizar una operación aritmetica en los dos primeros números (esta operacion puede ser adicion,
substracción o multiplicación) es posible obtener el tercer número
'''
'''
num1  = int(input('Ingresa el primer numero: '))
num2  = int(input('Ingresa el segundo numero: '))
resultado  = int(input('Ingresa el tercer numero: '))

contador = 0
if num1 + num2 == resultado : contador += 1
if num1 * num2 == resultado : contador += 1
if num1 - num2 == resultado : contador += 1
if num2 - num1 == resultado : contador += 1

print(f'Hay {contador} forma de llegar a {resultado} a partir de {num1} y {num2}')
'''


'''
Escribe un código que pida un número hasta que introduzcas un número negativo.
Al final, imprime la suma de todos los numeros introducidos (excepto el numero negativo del final)
'''
'''
sum = 0
while True:
    num = int(input('ingresa un numero'))
    if num > 0:
        print(num)
    else:
        print(num)
        print('-----')
        print(sum)
'''

'''
Escribe un código que pida un número entero. Después, imprime cada uno de 
los digitos de este número separados por comas
'''
'''
num = input('Ingrese un numero: ')
print('Numero ingresado: ', num)


if num.startswith('-'):
    num = num[1::]
    num = ','.join(num[::-1])
    print(num)
else:
    num = ','.join(num[::-1])
    print(num)
'''

'''
Escribe un código que pida un número entero n, y luego imprima los primeros n elementos de la sucesión de Fibonacci
'''
'''
n = int(input('ingresa un numero: '))
fib = [0,1]

for f in range(n-2):
    fib.append(fib[-1] + fib[-2])

print(", ".join(map(str, fib)))
'''


'''
Escribe un código que te pregunte un numero entero y a continuación escriba 
desde el numero 1 hasta el número que se preguntó en forma de escalera como se muestra en el ejemplo:
'''
'''
n = int(input('Dame un numero: '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print(" ")
'''