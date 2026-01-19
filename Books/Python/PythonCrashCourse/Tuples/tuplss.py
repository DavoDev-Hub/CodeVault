"""
EJERCICIOS DE TUPLAS - Python
Las tuplas son listas inmutables (no se pueden modificar después de crearlas)
Se definen con paréntesis () en lugar de corchetes []
"""

print("=" * 50)
print("1. CREAR TUPLAS")
print("=" * 50)

# Tupla básica
dimensiones = (200, 50)
print(f"Tupla de dimensiones: {dimensiones}")
print(f"Ancho: {dimensiones[0]}")
print(f"Alto: {dimensiones[1]}")

# Tupla de varios tipos de datos
persona = ("Ana", 25, "España", True)
print(f"\nPersona: {persona}")
print(f"Nombre: {persona[0]}, Edad: {persona[1]}")

# Tupla con un solo elemento (necesita coma)
tupla_uno = (50,)
print(f"\nTupla de un elemento: {tupla_uno}")
print(f"Tipo: {type(tupla_uno)}")

print("\n" + "=" * 50)
print("2. RECORRER TUPLAS")
print("=" * 50)

# Tupla de colores
colores = ("rojo", "verde", "azul", "amarillo", "negro")
print("Colores disponibles:")
for color in colores:
    print(f"  - {color.title()}")

# Con índices
print("\nColores con índices:")
for i, color in enumerate(colores):
    print(f"  {i}: {color}")

print("\n" + "=" * 50)
print("3. TUPLAS SON INMUTABLES")
print("=" * 50)

coordenadas = (10, 20)
print(f"Coordenadas originales: {coordenadas}")

# Esto daría error (descomenta para ver):
# coordenadas[0] = 15  # ❌ TypeError: 'tuple' object does not support item assignment

# Para "modificar" una tupla, hay que crear una nueva
coordenadas = (15, 25)
print(f"Nuevas coordenadas: {coordenadas}")

print("\n" + "=" * 50)
print("4. OPERACIONES CON TUPLAS")
print("=" * 50)

# Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_completa = tupla1 + tupla2
print(f"Tupla 1: {tupla1}")
print(f"Tupla 2: {tupla2}")
print(f"Concatenadas: {tupla_completa}")

# Repetir tuplas
patron = ("X", "O")
repetido = patron * 3
print(f"\nPatrón: {patron}")
print(f"Repetido 3 veces: {repetido}")

# Contar elementos
numeros = (1, 2, 2, 3, 2, 4, 2, 5)
print(f"\nTupla: {numeros}")
print(f"El número 2 aparece {numeros.count(2)} veces")

# Encontrar índice
print(f"El número 3 está en el índice: {numeros.index(3)}")

print("\n" + "=" * 50)
print("5. DESEMPAQUETADO DE TUPLAS")
print("=" * 50)

# Desempaquetar valores
punto = (100, 200, 300)
x, y, z = punto
print(f"Punto: {punto}")
print(f"x={x}, y={y}, z={z}")

# Intercambiar variables
a = 5
b = 10
print(f"\nAntes: a={a}, b={b}")
a, b = b, a
print(f"Después: a={a}, b={b}")

print("\n" + "=" * 50)
print("6. TUPLAS VS LISTAS")
print("=" * 50)

# Tupla - inmutable, más rápida
dias_semana = ("Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom")
print(f"Tupla (inmutable): {dias_semana}")

# Lista - mutable, más flexible
tareas = ["programar", "estudiar", "ejercicio"]
print(f"Lista (mutable): {tareas}")
tareas.append("cocinar")
print(f"Lista modificada: {tareas}")

print("\n" + "=" * 50)
print("7. EJERCICIOS PRÁCTICOS")
print("=" * 50)

# Ejercicio 1: Menú de restaurante
print("\n📝 Ejercicio 1: Menú inmutable")
menu = ("pizza", "hamburguesa", "ensalada", "pasta", "sushi")
print("Menú disponible:")
for plato in menu:
    print(f"  - {plato.title()}")

# Ejercicio 2: Información de libros
print("\n📝 Ejercicio 2: Biblioteca")
libros = (
    ("1984", "George Orwell", 1949),
    ("Cien años de soledad", "Gabriel García Márquez", 1967),
    ("El Principito", "Antoine de Saint-Exupéry", 1943)
)

for libro in libros:
    titulo, autor, año = libro
    print(f"'{titulo}' por {autor} ({año})")

# Ejercicio 3: Coordenadas GPS
print("\n📝 Ejercicio 3: Ubicaciones GPS")
ubicaciones = {
    "Madrid": (40.4168, -3.7038),
    "Barcelona": (41.3851, 2.1734),
    "Valencia": (39.4699, -0.3763)
}

for ciudad, coordenadas in ubicaciones.items():
    lat, lon = coordenadas
    print(f"{ciudad}: Latitud {lat}, Longitud {lon}")

# Ejercicio 4: Estadísticas
print("\n📝 Ejercicio 4: Estadísticas de datos")
ventas = (120, 340, 280, 190, 420, 310, 250)
print(f"Ventas semanales: {ventas}")
print(f"Máximo: ${max(ventas)}")
print(f"Mínimo: ${min(ventas)}")
print(f"Total: ${sum(ventas)}")
print(f"Promedio: ${sum(ventas) / len(ventas):.2f}")

print("\n" + "=" * 50)
print("8. CUÁNDO USAR TUPLAS")
print("=" * 50)
print("""
✅ Usa TUPLAS cuando:
  - Los datos no deben cambiar (coordenadas, RGB, fechas)
  - Quieres proteger los datos de modificaciones accidentales
  - Necesitas usar como claves de diccionario
  - Quieres mejor rendimiento (son más rápidas que listas)

✅ Usa LISTAS cuando:
  - Los datos pueden cambiar
  - Necesitas agregar/eliminar elementos
  - Requieres métodos como append(), remove(), sort()
""")

print("\n🎯 ¡Práctica completada!")
