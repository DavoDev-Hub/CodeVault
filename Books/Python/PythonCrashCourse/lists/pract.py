# Ejercicio: Top 5 de películas favoritas
# Practicar slicing, reversión y modificación de listas

peliculas = ['Inception', 'The Matrix', 'Interstellar', 'Pulp Fiction', 'The Shawshank Redemption', 'Fight Club', 'The Dark Knight']

print("Lista completa de películas:")
print(peliculas)

# Mostrar las tres primeras películas
print("\nTop 3 películas:")
print(peliculas[:3])

# Mostrar las tres últimas películas
print("\nÚltimas 3 películas:")
print(peliculas[-3:])

# Mostrar películas del medio (índices 2 a 5)
print("\nPelículas del medio:")
print(peliculas[2:5])

# Crear una copia de la lista y ordenarla
peliculas_ordenadas = peliculas.copy()
peliculas_ordenadas.sort()
print("\nPelículas ordenadas alfabéticamente:")
print(peliculas_ordenadas)

# Invertir el orden de la lista original
peliculas.reverse()
print("\nLista invertida:")
print(peliculas)

# Modificar una película específica
peliculas[0] = 'The Godfather'
print("\nDespués de cambiar la primera película:")
print(peliculas)

# Contar cuántas películas hay
print(f"\nTotal de películas en la lista: {len(peliculas)}")

# Verificar si una película está en la lista
pelicula_buscar = 'Inception'
if pelicula_buscar in peliculas:
    print(f"\n'{pelicula_buscar}' está en la lista")
else:
    print(f"\n'{pelicula_buscar}' no está en la lista")
