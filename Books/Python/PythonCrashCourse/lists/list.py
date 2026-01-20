"""
============================================================
GUÍA COMPLETA DE LISTAS EN PYTHON
============================================================
Las listas son colecciones ordenadas y modificables de elementos
Pueden contener cualquier tipo de dato y son muy flexibles
"""

# ============================================================
# 1. CREAR LISTAS
# ============================================================
print("=" * 60)
print("1. CREAR LISTAS")
print("=" * 60)

# Lista vacía
lista_vacia = []
otra_vacia = list()

# Lista con elementos
frutas = ['manzana', 'banana', 'naranja', 'uva']
numeros = [1, 2, 3, 4, 5]
mixta = [1, 'hola', 3.14, True, None]

print(f"Frutas: {frutas}")
print(f"Números: {numeros}")
print(f"Lista mixta: {mixta}")


# ============================================================
# 2. ACCEDER A ELEMENTOS (ÍNDICES)
# ============================================================
print("\n" + "=" * 60)
print("2. ACCEDER A ELEMENTOS")
print("=" * 60)

colores = ['rojo', 'verde', 'azul', 'amarillo', 'negro']

# Índices positivos (empiezan en 0)
print(f"Primer color: {colores[0]}")
print(f"Tercer color: {colores[2]}")

# Índices negativos (desde el final)
print(f"Último color: {colores[-1]}")
print(f"Penúltimo color: {colores[-2]}")


# ============================================================
# 3. MODIFICAR ELEMENTOS
# ============================================================
print("\n" + "=" * 60)
print("3. MODIFICAR ELEMENTOS")
print("=" * 60)

motos = ['honda', 'yamaha', 'suzuki']
print(f"Lista original: {motos}")

motos[0] = 'ducati'  # Cambiar primer elemento
print(f"Lista modificada: {motos}")

motos[-1] = 'kawasaki'  # Cambiar último elemento
print(f"Lista final: {motos}")


# ============================================================
# 4. AÑADIR ELEMENTOS
# ============================================================
print("\n" + "=" * 60)
print("4. AÑADIR ELEMENTOS")
print("=" * 60)

# append() - Añade al final
animales = ['perro', 'gato']
print(f"Lista inicial: {animales}")

animales.append('conejo')
print(f"Después de append: {animales}")

# insert() - Añade en posición específica
animales.insert(1, 'loro')  # Inserta en posición 1
print(f"Después de insert: {animales}")


# ============================================================
# 5. ELIMINAR ELEMENTOS
# ============================================================
print("\n" + "=" * 60)
print("5. ELIMINAR ELEMENTOS")
print("=" * 60)

videojuegos = ['mario', 'zelda', 'pokemon', 'sonic', 'fifa']
print(f"Lista original: {videojuegos}")

# del - Elimina por índice
del videojuegos[0]
print(f"Después de del: {videojuegos}")

# pop() - Elimina y retorna el último (o el que indiques)
ultimo = videojuegos.pop()
print(f"Elemento eliminado: {ultimo}")
print(f"Lista actual: {videojuegos}")

segundo = videojuegos.pop(1)
print(f"Segundo eliminado: {segundo}")
print(f"Lista actual: {videojuegos}")

# remove() - Elimina por valor
videojuegos.append('mario')
videojuegos.remove('mario')  # Elimina la primera ocurrencia
print(f"Después de remove: {videojuegos}")


# ============================================================
# 6. ORGANIZAR LISTAS
# ============================================================
print("\n" + "=" * 60)
print("6. ORGANIZAR LISTAS")
print("=" * 60)

# sort() - Ordena permanentemente
numeros = [5, 2, 8, 1, 9, 3]
print(f"Lista original: {numeros}")
numeros.sort()
print(f"Ordenada ascendente: {numeros}")

numeros.sort(reverse=True)
print(f"Ordenada descendente: {numeros}")

# sorted() - Ordena temporalmente (no modifica original)
letras = ['z', 'a', 'm', 'b', 'p']
print(f"\nLetras originales: {letras}")
print(f"Ordenadas temporalmente: {sorted(letras)}")
print(f"Letras siguen igual: {letras}")

# reverse() - Invierte el orden
letras.reverse()
print(f"Letras invertidas: {letras}")


# ============================================================
# 7. LONGITUD DE UNA LISTA
# ============================================================
print("\n" + "=" * 60)
print("7. LONGITUD DE UNA LISTA")
print("=" * 60)

ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
print(f"Ciudades: {ciudades}")
print(f"Número de ciudades: {len(ciudades)}")


# ============================================================
# 8. SLICING (REBANADO)
# ============================================================
print("\n" + "=" * 60)
print("8. SLICING - EXTRAER PARTES DE LA LISTA")
print("=" * 60)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [inicio:fin] - fin no se incluye
print(f"Elementos 2 al 5: {numeros[2:6]}")
print(f"Primeros 3: {numeros[:3]}")
print(f"Desde índice 6: {numeros[6:]}")
print(f"Últimos 3: {numeros[-3:]}")

# [inicio:fin:paso]
print(f"Cada 2 elementos: {numeros[::2]}")
print(f"Invertir lista: {numeros[::-1]}")


# ============================================================
# 9. COPIAR LISTAS
# ============================================================
print("\n" + "=" * 60)
print("9. COPIAR LISTAS")
print("=" * 60)

original = ['a', 'b', 'c']

# Forma incorrecta (crea una referencia)
referencia = original
referencia.append('d')
print(f"Original: {original}")  # También cambia!

# Forma correcta 1: Slicing
original = ['a', 'b', 'c']
copia1 = original[:]
copia1.append('d')
print(f"Original: {original}")  # No cambia
print(f"Copia: {copia1}")

# Forma correcta 2: copy()
copia2 = original.copy()


# ============================================================
# 10. RECORRER LISTAS
# ============================================================
print("\n" + "=" * 60)
print("10. RECORRER LISTAS")
print("=" * 60)

mascotas = ['perro', 'gato', 'pez', 'hamster']

# For básico
print("Mis mascotas:")
for mascota in mascotas:
    print(f"  - {mascota.title()}")

# For con enumerate() - obtener índice y valor
print("\nCon índices:")
for indice, mascota in enumerate(mascotas):
    print(f"{indice}: {mascota}")


# ============================================================
# 11. LISTAS NUMÉRICAS
# ============================================================
print("\n" + "=" * 60)
print("11. LISTAS NUMÉRICAS")
print("=" * 60)

# range() - generar secuencias
numeros = list(range(1, 6))  # 1 al 5
print(f"Range 1-5: {numeros}")

pares = list(range(0, 11, 2))  # 0 al 10 de 2 en 2
print(f"Pares: {pares}")

# Estadísticas
valores = [3, 8, 1, 9, 2, 7]
print(f"\nValores: {valores}")
print(f"Mínimo: {min(valores)}")
print(f"Máximo: {max(valores)}")
print(f"Suma: {sum(valores)}")


# ============================================================
# 12. COMPRENSIÓN DE LISTAS
# ============================================================
print("\n" + "=" * 60)
print("12. COMPRENSIÓN DE LISTAS (List Comprehension)")
print("=" * 60)

# Forma tradicional
cuadrados = []
for x in range(1, 6):
    cuadrados.append(x**2)
print(f"Cuadrados (tradicional): {cuadrados}")

# Comprensión de lista - más conciso
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados (comprensión): {cuadrados}")

# Con condición
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Solo pares: {pares}")


# ============================================================
# 13. MÉTODOS ÚTILES
# ============================================================
print("\n" + "=" * 60)
print("13. MÉTODOS ÚTILES DE LISTAS")
print("=" * 60)

numeros = [1, 2, 3, 2, 4, 2, 5]

# count() - cuenta ocurrencias
print(f"Lista: {numeros}")
print(f"Veces que aparece el 2: {numeros.count(2)}")

# index() - encuentra la posición
print(f"Posición del primer 3: {numeros.index(3)}")

# extend() - añade varios elementos
numeros.extend([6, 7, 8])
print(f"Después de extend: {numeros}")

# clear() - vacía la lista
copia = numeros.copy()
copia.clear()
print(f"Lista vaciada: {copia}")


# ============================================================
# 14. COMPROBAR PERTENENCIA
# ============================================================
print("\n" + "=" * 60)
print("14. COMPROBAR SI UN ELEMENTO ESTÁ EN LA LISTA")
print("=" * 60)

frutas = ['manzana', 'pera', 'uva']

if 'manzana' in frutas:
    print("✓ Hay manzanas disponibles")

if 'sandía' not in frutas:
    print("✗ No hay sandía")


# ============================================================
# 15. LISTAS ANIDADAS (MATRICES)
# ============================================================
print("\n" + "=" * 60)
print("15. LISTAS ANIDADAS")
print("=" * 60)

# Lista de listas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for fila in matriz:
    print(fila)

print(f"\nElemento [1][2]: {matriz[1][2]}")  # 6


# ============================================================
# 16. DESEMPAQUETAR LISTAS
# ============================================================
print("\n" + "=" * 60)
print("16. DESEMPAQUETAR LISTAS")
print("=" * 60)

coordenadas = [10, 20, 30]

# Desempaquetar en variables
x, y, z = coordenadas
print(f"x={x}, y={y}, z={z}")

# Desempaquetar con *
primero, *resto = [1, 2, 3, 4, 5]
print(f"Primero: {primero}")
print(f"Resto: {resto}")


# ============================================================
# 17. EJERCICIOS PRÁCTICOS
# ============================================================
print("\n" + "=" * 60)
print("17. EJERCICIOS PRÁCTICOS")
print("=" * 60)

# Crear una lista de tareas
tareas = []
tareas.append("Estudiar Python")
tareas.append("Hacer ejercicio")
tareas.append("Leer un libro")

print("MIS TAREAS:")
for i, tarea in enumerate(tareas, 1):
    print(f"{i}. {tarea}")

# Filtrar números mayores a 5
numeros = [2, 7, 3, 9, 1, 8, 4]
mayores = [n for n in numeros if n > 5]
print(f"\nNúmeros mayores a 5: {mayores}")

# Crear tabla de multiplicar
numero = 5
tabla = [numero * i for i in range(1, 11)]
print(f"\nTabla del {numero}: {tabla}")


# ============================================================
# RESUMEN DE MÉTODOS IMPORTANTES
# ============================================================
print("\n" + "=" * 60)
print("RESUMEN DE MÉTODOS DE LISTAS")
print("=" * 60)
print("""
AÑADIR:
  • append(x)      - Añade x al final
  • insert(i, x)   - Inserta x en posición i
  • extend(lista)  - Añade múltiples elementos

ELIMINAR:
  • remove(x)      - Elimina primera ocurrencia de x
  • pop()          - Elimina y retorna último elemento
  • pop(i)         - Elimina y retorna elemento en i
  • clear()        - Vacía la lista
  • del lista[i]   - Elimina elemento en i

ORGANIZAR:
  • sort()         - Ordena la lista permanentemente
  • sort(reverse=True) - Ordena descendente
  • reverse()      - Invierte el orden
  • sorted(lista)  - Retorna copia ordenada

BUSCAR:
  • index(x)       - Retorna posición de x
  • count(x)       - Cuenta ocurrencias de x
  • x in lista     - Verifica si x está en lista

OTROS:
  • len(lista)     - Longitud
  • copy()         - Copia la lista
  • min(lista)     - Valor mínimo
  • max(lista)     - Valor máximo
  • sum(lista)     - Suma de elementos
""")

print("\n¡Practica estos conceptos para dominar las listas en Python!")
