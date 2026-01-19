"""
EJERCICIOS DE DICCIONARIOS - Python
Los diccionarios almacenan pares clave-valor
Se definen con llaves {} y permiten acceso rápido por clave
"""

print("=" * 60)
print("1. CREAR Y ACCEDER A DICCIONARIOS")
print("=" * 60)

# Diccionario básico
persona = {
    'nombre': 'Carlos',
    'edad': 28,
    'ciudad': 'Madrid',
    'profesion': 'Ingeniero'
}

print(f"Persona: {persona}")
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']} años")
print(f"Vive en: {persona['ciudad']}")

# Acceso seguro con get()
print(f"\nProfesión: {persona.get('profesion')}")
print(f"País: {persona.get('pais', 'No especificado')}")  # valor por defecto

print("\n" + "=" * 60)
print("2. MODIFICAR DICCIONARIOS")
print("=" * 60)

usuario = {'nombre': 'Ana', 'puntos': 0}
print(f"Usuario inicial: {usuario}")

# Agregar nuevas claves
usuario['nivel'] = 1
usuario['activo'] = True
print(f"Después de agregar: {usuario}")

# Modificar valores
usuario['puntos'] = 100
usuario['nivel'] = 2
print(f"Después de modificar: {usuario}")

# Eliminar claves
del usuario['activo']
print(f"Después de eliminar 'activo': {usuario}")

# Eliminar y obtener valor
puntos = usuario.pop('puntos')
print(f"Puntos obtenidos: {puntos}")
print(f"Usuario final: {usuario}")

print("\n" + "=" * 60)
print("3. RECORRER DICCIONARIOS")
print("=" * 60)

lenguajes = {
    'python': 'Guido van Rossum',
    'javascript': 'Brendan Eich',
    'ruby': 'Yukihiro Matsumoto',
    'java': 'James Gosling'
}

# Recorrer claves y valores
print("Lenguajes y sus creadores:")
for lenguaje, creador in lenguajes.items():
    print(f"  {lenguaje.title()} fue creado por {creador}")

# Solo claves
print("\nLenguajes disponibles:")
for lenguaje in lenguajes.keys():
    print(f"  - {lenguaje.upper()}")

# Solo valores
print("\nCreadores:")
for creador in lenguajes.values():
    print(f"  • {creador}")

print("\n" + "=" * 60)
print("4. DICCIONARIOS ANIDADOS")
print("=" * 60)

# Lista de diccionarios
estudiantes = [
    {'nombre': 'Laura', 'edad': 22, 'nota': 9.5},
    {'nombre': 'Pedro', 'edad': 23, 'nota': 8.7},
    {'nombre': 'María', 'edad': 21, 'nota': 9.2}
]

print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(f"  {estudiante['nombre']} ({estudiante['edad']} años): {estudiante['nota']}")

# Diccionario de diccionarios
usuarios = {
    'aeinstein': {
        'nombre': 'Albert',
        'apellido': 'Einstein',
        'pais': 'Alemania'
    },
    'mcurie': {
        'nombre': 'Marie',
        'apellido': 'Curie',
        'pais': 'Polonia'
    }
}

print("\nUsuarios registrados:")
for username, info in usuarios.items():
    print(f"\n  Usuario: {username}")
    print(f"  Nombre completo: {info['nombre']} {info['apellido']}")
    print(f"  País: {info['pais']}")

print("\n" + "=" * 60)
print("5. MÉTODOS ÚTILES DE DICCIONARIOS")
print("=" * 60)

inventario = {
    'manzanas': 50,
    'naranjas': 30,
    'plátanos': 45
}

print(f"Inventario: {inventario}")

# keys(), values(), items()
print(f"\nProductos: {list(inventario.keys())}")
print(f"Cantidades: {list(inventario.values())}")
print(f"Total de items: {sum(inventario.values())}")

# update() - combinar diccionarios
nuevo_stock = {'peras': 25, 'uvas': 60}
inventario.update(nuevo_stock)
print(f"Inventario actualizado: {inventario}")

# setdefault() - obtener o crear valor
inventario.setdefault('kiwis', 0)
print(f"Con setdefault: {inventario}")

# clear() - vaciar diccionario
temporal = {'a': 1, 'b': 2}
print(f"\nTemporal antes: {temporal}")
temporal.clear()
print(f"Temporal después de clear(): {temporal}")

print("\n" + "=" * 60)
print("6. EJERCICIO PRÁCTICO: TIENDA ONLINE")
print("=" * 60)

# Catálogo de productos
catalogo = {
    'laptop': {'precio': 899.99, 'stock': 15},
    'mouse': {'precio': 29.99, 'stock': 50},
    'teclado': {'precio': 79.99, 'stock': 30},
    'monitor': {'precio': 299.99, 'stock': 20}
}

# Carrito de compras
carrito = {}

def agregar_al_carrito(producto, cantidad):
    """Agrega productos al carrito"""
    if producto in catalogo:
        if catalogo[producto]['stock'] >= cantidad:
            carrito[producto] = carrito.get(producto, 0) + cantidad
            print(f"✅ {cantidad} {producto}(s) agregado(s) al carrito")
        else:
            print(f"❌ Stock insuficiente de {producto}")
    else:
        print(f"❌ Producto {producto} no encontrado")

def mostrar_carrito():
    """Muestra el contenido del carrito"""
    if not carrito:
        print("🛒 Carrito vacío")
        return
    
    print("\n🛒 TU CARRITO:")
    total = 0
    for producto, cantidad in carrito.items():
        precio = catalogo[producto]['precio']
        subtotal = precio * cantidad
        total += subtotal
        print(f"  {producto.title()}: {cantidad} x ${precio} = ${subtotal:.2f}")
    print(f"  {'─' * 40}")
    print(f"  TOTAL: ${total:.2f}")

# Simulación de compra
print("\n🏪 Bienvenido a la Tienda Online")
print("\nCatálogo:")
for producto, info in catalogo.items():
    print(f"  {producto.title()}: ${info['precio']} (Stock: {info['stock']})")

print("\n--- Agregando productos ---")
agregar_al_carrito('laptop', 1)
agregar_al_carrito('mouse', 2)
agregar_al_carrito('teclado', 1)
agregar_al_carrito('webcam', 1)  # No existe

mostrar_carrito()

print("\n" + "=" * 60)
print("7. EJERCICIO: CONTADOR DE PALABRAS")
print("=" * 60)

texto = "python es genial python es poderoso y python es fácil de aprender"
palabras = texto.split()

# Contar frecuencia
contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print(f"Texto: '{texto}'")
print("\nFrecuencia de palabras:")
for palabra, veces in sorted(contador.items()):
    print(f"  '{palabra}': {veces} vez/veces")

print("\n" + "=" * 60)
print("8. EJERCICIO: AGENDA DE CONTACTOS")
print("=" * 60)

agenda = {
    'Juan': {
        'telefono': '555-1234',
        'email': 'juan@email.com',
        'ciudad': 'Barcelona'
    },
    'Ana': {
        'telefono': '555-5678',
        'email': 'ana@email.com',
        'ciudad': 'Madrid'
    },
    'Luis': {
        'telefono': '555-9012',
        'email': 'luis@email.com',
        'ciudad': 'Valencia'
    }
}

print("📱 AGENDA DE CONTACTOS\n")
for nombre, datos in agenda.items():
    print(f"Contacto: {nombre}")
    for clave, valor in datos.items():
        print(f"  {clave.title()}: {valor}")
    print()

# Buscar contactos por ciudad
ciudad_buscar = 'Madrid'
print(f"Contactos en {ciudad_buscar}:")
for nombre, datos in agenda.items():
    if datos['ciudad'] == ciudad_buscar:
        print(f"  • {nombre}: {datos['telefono']}")

print("\n" + "=" * 60)
print("9. EJERCICIO: VOTACIÓN")
print("=" * 60)

votos = ['python', 'javascript', 'python', 'java', 'python', 
         'javascript', 'ruby', 'python', 'java', 'javascript']

# Contar votos
resultados = {}
for voto in votos:
    resultados[voto] = resultados.get(voto, 0) + 1

print("🗳️  RESULTADOS DE LA VOTACIÓN:")
print(f"Total de votos: {len(votos)}\n")

# Ordenar por número de votos (descendente)
for lenguaje, cantidad in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
    porcentaje = (cantidad / len(votos)) * 100
    barra = '█' * cantidad
    print(f"{lenguaje.ljust(12)}: {barra} {cantidad} votos ({porcentaje:.1f}%)")

ganador = max(resultados, key=resultados.get)
print(f"\n🏆 Ganador: {ganador.upper()} con {resultados[ganador]} votos!")

print("\n" + "=" * 60)
print("10. COMPRENSIÓN DE DICCIONARIOS")
print("=" * 60)

# Crear diccionario con comprensión
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados}")

# Filtrar diccionario
numeros = {'a': 10, 'b': 25, 'c': 15, 'd': 30, 'e': 5}
mayores_15 = {k: v for k, v in numeros.items() if v > 15}
print(f"\nNúmeros originales: {numeros}")
print(f"Mayores a 15: {mayores_15}")

# Transformar valores
precios_euros = {'laptop': 800, 'mouse': 25, 'teclado': 65}
tasa_cambio = 1.1
precios_dolares = {prod: precio * tasa_cambio for prod, precio in precios_euros.items()}
print(f"\nPrecios en euros: {precios_euros}")
print(f"Precios en dólares: {precios_dolares}")

print("\n" + "=" * 60)
print("🎯 RESUMEN - CUÁNDO USAR DICCIONARIOS")
print("=" * 60)
print("""
✅ Usa DICCIONARIOS cuando:
  • Necesites asociar claves con valores (nombre → edad)
  • Quieras acceso rápido por clave
  • Los datos tengan relaciones clave-valor
  • Necesites buscar/actualizar valores frecuentemente

📝 Métodos importantes:
  • get(key, default) - acceso seguro
  • keys() - obtener claves
  • values() - obtener valores
  • items() - obtener pares clave-valor
  • update() - combinar diccionarios
  • pop(key) - eliminar y obtener valor

🎓 ¡Sigue practicando con estos ejercicios!
""")
