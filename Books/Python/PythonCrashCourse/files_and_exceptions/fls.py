"""
Ejercicios de Archivos y Excepciones en Python
"""

from pathlib import Path
import json

# ========== EJERCICIO 1: Lectura básica de archivos ==========
print("=" * 50)
print("EJERCICIO 1: Lectura de archivos")
print("=" * 50)

def ejercicio1():
    """Leer y mostrar el contenido de un archivo"""
    try:
        path = Path('learning_python.txt')
        contents = path.read_text(encoding='utf-8')
        print(contents)
    except FileNotFoundError:
        print("El archivo no existe")

# ejercicio1()


# ========== EJERCICIO 2: Lectura línea por línea ==========
print("\n" + "=" * 50)
print("EJERCICIO 2: Lectura línea por línea")
print("=" * 50)

def ejercicio2():
    """Leer un archivo línea por línea"""
    try:
        path = Path('learning_python.txt')
        contents = path.read_text(encoding='utf-8')
        for line in contents.splitlines():
            print(f"-> {line}")
    except FileNotFoundError:
        print("Archivo no encontrado")

# ejercicio2()


# ========== EJERCICIO 3: Escritura de archivos ==========
print("\n" + "=" * 50)
print("EJERCICIO 3: Escritura de archivos")
print("=" * 50)

def ejercicio3():
    """Escribir texto en un archivo"""
    path = Path('mi_archivo.txt')
    
    contenido = "Estoy aprendiendo Python.\n"
    contenido += "Python es genial para trabajar con archivos.\n"
    contenido += "Me encanta programar en Python.\n"
    
    path.write_text(contenido, encoding='utf-8')
    print("Archivo creado exitosamente!")
    
    # Leer para verificar
    print("\nContenido del archivo:")
    print(path.read_text(encoding='utf-8'))

# ejercicio3()


# ========== EJERCICIO 4: Try-Except básico ==========
print("\n" + "=" * 50)
print("EJERCICIO 4: Manejo de excepciones")
print("=" * 50)

def ejercicio4():
    """División con manejo de excepciones"""
    print("Calculadora de división")
    print("Escribe 'q' para salir\n")
    
    while True:
        numerador = input("Dame el primer número: ")
        if numerador == 'q':
            break
        
        denominador = input("Dame el segundo número: ")
        if denominador == 'q':
            break
        
        try:
            resultado = int(numerador) / int(denominador)
            print(f"Resultado: {resultado}\n")
        except ZeroDivisionError:
            print("¡Error! No puedes dividir entre 0.\n")
        except ValueError:
            print("¡Error! Por favor ingresa solo números.\n")

# ejercicio4()


# ========== EJERCICIO 5: Trabajar con múltiples archivos ==========
print("\n" + "=" * 50)
print("EJERCICIO 5: Contar palabras en archivos")
print("=" * 50)

def contar_palabras(path):
    """Cuenta las palabras en un archivo"""
    try:
        contents = path.read_text(encoding='utf-8')
        palabras = contents.split()
        num_palabras = len(palabras)
        print(f"{path.name} tiene aproximadamente {num_palabras} palabras.")
    except FileNotFoundError:
        print(f"El archivo {path.name} no existe.")

def ejercicio5():
    """Contar palabras en varios archivos"""
    archivos = ['cats.txt', 'dogs.txt', 'learning_python.txt']
    
    for archivo in archivos:
        path = Path(archivo)
        contar_palabras(path)

# ejercicio5()


# ========== EJERCICIO 6: JSON - Guardar datos ==========
print("\n" + "=" * 50)
print("EJERCICIO 6: Trabajar con JSON")
print("=" * 50)

def ejercicio6_guardar():
    """Guardar datos en JSON"""
    # Crear datos
    estudiantes = {
        "Juan": {"edad": 20, "calificacion": 9.5},
        "María": {"edad": 22, "calificacion": 9.8},
        "Pedro": {"edad": 21, "calificacion": 8.7}
    }
    
    # Guardar en JSON
    path = Path('estudiantes.json')
    contenido_json = json.dumps(estudiantes, indent=4, ensure_ascii=False)
    path.write_text(contenido_json, encoding='utf-8')
    
    print("Datos guardados en estudiantes.json")

def ejercicio6_leer():
    """Leer datos desde JSON"""
    path = Path('estudiantes.json')
    
    try:
        contenido = path.read_text(encoding='utf-8')
        estudiantes = json.loads(contenido)
        
        print("\nDatos de estudiantes:")
        for nombre, datos in estudiantes.items():
            print(f"{nombre}: {datos['edad']} años, calificación: {datos['calificacion']}")
    except FileNotFoundError:
        print("El archivo no existe. Ejecuta primero ejercicio6_guardar()")

# ejercicio6_guardar()
# ejercicio6_leer()


# ========== EJERCICIO 7: Pass en excepciones ==========
print("\n" + "=" * 50)
print("EJERCICIO 7: Pass - Fallar silenciosamente")
print("=" * 50)

def ejercicio7():
    """Intentar leer archivos que pueden no existir"""
    archivos = ['archivo1.txt', 'archivo2.txt', 'archivo3.txt']
    
    for archivo in archivos:
        path = Path(archivo)
        try:
            contents = path.read_text(encoding='utf-8')
            print(f"Contenido de {archivo}:")
            print(contents)
        except FileNotFoundError:
            # Falla silenciosamente
            pass

# ejercicio7()


# ========== EJERCICIO 8: Append - Añadir a un archivo ==========
print("\n" + "=" * 50)
print("EJERCICIO 8: Añadir texto a un archivo existente")
print("=" * 50)

def ejercicio8():
    """Añadir líneas a un archivo"""
    path = Path('notas.txt')
    
    # Crear archivo inicial
    if not path.exists():
        path.write_text("Mis notas de Python:\n", encoding='utf-8')
    
    # Añadir nuevas líneas
    contenido_actual = path.read_text(encoding='utf-8')
    nueva_nota = "- Los archivos son fáciles de manejar en Python\n"
    path.write_text(contenido_actual + nueva_nota, encoding='utf-8')
    
    # Mostrar resultado
    print("Contenido del archivo:")
    print(path.read_text(encoding='utf-8'))

# ejercicio8()


# ========== EJERCICIO 9: Else en Try-Except ==========
print("\n" + "=" * 50)
print("EJERCICIO 9: Usar Else con Try-Except")
print("=" * 50)

def ejercicio9():
    """Sumar dos números con manejo de excepciones"""
    try:
        num1 = int(input("Primer número: "))
        num2 = int(input("Segundo número: "))
    except ValueError:
        print("¡Error! Debes ingresar números válidos.")
    else:
        # Solo se ejecuta si no hubo excepciones
        resultado = num1 + num2
        print(f"La suma es: {resultado}")

# ejercicio9()


# ========== EJERCICIO 10: Finally ==========
print("\n" + "=" * 50)
print("EJERCICIO 10: Usar Finally")
print("=" * 50)

def ejercicio10():
    """Demostrar el uso de finally"""
    archivo = None
    try:
        path = Path('datos.txt')
        archivo = path.read_text(encoding='utf-8')
        print("Archivo leído exitosamente")
    except FileNotFoundError:
        print("El archivo no existe")
    finally:
        # Esto siempre se ejecuta
        print("Operación de lectura finalizada")

# ejercicio10()


# ========== INSTRUCCIONES ==========
print("\n\n" + "=" * 50)
print("INSTRUCCIONES:")
print("=" * 50)
print("""
Para ejecutar los ejercicios, descomenta las líneas que llaman
a cada función (quita el # al inicio).

Por ejemplo:
    ejercicio1()  # en lugar de # ejercicio1()

¡Practica cada ejercicio y experimenta con el código!
""")
