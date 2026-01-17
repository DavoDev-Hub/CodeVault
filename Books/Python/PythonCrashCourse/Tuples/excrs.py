# Ejercicio de Tuplas - Restaurante

# Definir una tupla con los platillos del menú
menu_items = ('pizza', 'hamburguesa', 'ensalada', 'pasta', 'tacos')

print("Menú original del restaurante:")
for item in menu_items:
    print(f"- {item.title()}")

# Intentar modificar un elemento (esto causará error si se descomenta)
# menu_items[0] = 'sushi'  # TypeError: 'tuple' object does not support item assignment

# Modificar el menú (crear nueva tupla)
print("\n¡El restaurante ha cambiado su menú!")
menu_items = ('pizza', 'hamburguesa', 'sushi', 'ramen', 'tacos')

print("\nNuevo menú del restaurante:")
for item in menu_items:
    print(f"- {item.title()}")

# Ejercicio adicional: Información de coordenadas
print("\n" + "="*50)
print("Ejercicio 2: Coordenadas de ciudades")
print("="*50)

# Tupla con coordenadas de ciudades (latitud, longitud)
ciudades = {
    'Madrid': (40.4168, -3.7038),
    'Barcelona': (41.3851, 2.1734),
    'París': (48.8566, 2.3522),
    'Londres': (51.5074, -0.1278),
    'Nueva York': (40.7128, -74.0060)
}

for ciudad, coordenadas in ciudades.items():
    lat, lon = coordenadas
    print(f"{ciudad}: Latitud {lat}, Longitud {lon}")

# Ejercicio 3: Información de productos
print("\n" + "="*50)
print("Ejercicio 3: Inventario de productos")
print("="*50)

productos = [
    ('Laptop', 999.99, 5),
    ('Mouse', 29.99, 25),
    ('Teclado', 79.99, 15),
    ('Monitor', 299.99, 8),
    ('Auriculares', 149.99, 12)
]

print(f"{'Producto':<15} {'Precio':<10} {'Stock':<10} {'Total':<10}")
print("-" * 45)
for nombre, precio, cantidad in productos:
    total = precio * cantidad
    print(f"{nombre:<15} ${precio:<9.2f} {cantidad:<10} ${total:<9.2f}")

# Calcular el valor total del inventario
valor_total = sum(precio * cantidad for _, precio, cantidad in productos)
print("-" * 45)
print(f"Valor total del inventario: ${valor_total:.2f}")
