"""
GUÍA COMPLETA DE CLASES EN PYTHON
==================================
Este archivo explica los conceptos fundamentales de las clases con ejemplos prácticos.
"""

# ============================================================================
# 1. CLASE BÁSICA - Concepto fundamental
# ============================================================================

class Perro:
    """Una clase simple que representa un perro."""
    
    def __init__(self, nombre, edad):
        """Inicializa los atributos nombre y edad."""
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad
    
    def sentarse(self):
        """Simula que el perro se sienta."""
        print(f"{self.nombre} ahora está sentado.")
    
    def rodar(self):
        """Simula que el perro rueda."""
        print(f"{self.nombre} rodó!")


# Crear instancias (objetos) de la clase
print("=" * 60)
print("1. CLASE BÁSICA")
print("=" * 60)
mi_perro = Perro("Willie", 6)
tu_perro = Perro("Luna", 3)

print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} años.")
print(f"Tu perro se llama {tu_perro.nombre} y tiene {tu_perro.edad} años.")
mi_perro.sentarse()
tu_perro.rodar()


# ============================================================================
# 2. ATRIBUTOS DE CLASE vs ATRIBUTOS DE INSTANCIA
# ============================================================================

class Gato:
    """Demuestra la diferencia entre atributos de clase e instancia."""
    
    # Atributo de clase (compartido por todas las instancias)
    especie = "Felino"
    contador = 0
    
    def __init__(self, nombre, color):
        """Inicializa atributos de instancia."""
        self.nombre = nombre  # Atributo de instancia (único para cada objeto)
        self.color = color
        Gato.contador += 1  # Incrementa el contador de clase
    
    def maullar(self):
        """El gato maúlla."""
        print(f"{self.nombre} dice: ¡Miau!")


print("\n" + "=" * 60)
print("2. ATRIBUTOS DE CLASE vs INSTANCIA")
print("=" * 60)
gato1 = Gato("Michi", "negro")
gato2 = Gato("Pelusa", "blanco")

print(f"{gato1.nombre} es de color {gato1.color} y es un {gato1.especie}")
print(f"{gato2.nombre} es de color {gato2.color} y es un {gato2.especie}")
print(f"Total de gatos creados: {Gato.contador}")


# ============================================================================
# 3. MÉTODOS ESPECIALES (Magic Methods)
# ============================================================================

class Libro:
    """Demuestra el uso de métodos especiales."""
    
    def __init__(self, titulo, autor, paginas):
        """Constructor."""
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        """Representación legible del objeto."""
        return f"'{self.titulo}' por {self.autor}"
    
    def __repr__(self):
        """Representación técnica del objeto."""
        return f"Libro('{self.titulo}', '{self.autor}', {self.paginas})"
    
    def __len__(self):
        """Devuelve el número de páginas."""
        return self.paginas
    
    def __eq__(self, otro):
        """Compara dos libros por su título."""
        return self.titulo == otro.titulo


print("\n" + "=" * 60)
print("3. MÉTODOS ESPECIALES")
print("=" * 60)
libro1 = Libro("1984", "George Orwell", 328)
libro2 = Libro("1984", "George Orwell", 328)

print(f"str(): {libro1}")
print(f"repr(): {repr(libro1)}")
print(f"len(): {len(libro1)} páginas")
print(f"¿Son iguales? {libro1 == libro2}")


# ============================================================================
# 4. HERENCIA - Clase hija hereda de clase padre
# ============================================================================

class Vehiculo:
    """Clase padre que representa un vehículo genérico."""
    
    def __init__(self, marca, modelo, año):
        """Inicializa atributos del vehículo."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0
    
    def descripcion(self):
        """Devuelve una descripción del vehículo."""
        return f"{self.año} {self.marca} {self.modelo}"
    
    def avanzar(self, km):
        """Incrementa el kilometraje."""
        self.kilometraje += km
        print(f"Has avanzado {km} km. Total: {self.kilometraje} km")


class Auto(Vehiculo):
    """Clase hija que representa un auto específico."""
    
    def __init__(self, marca, modelo, año, puertas):
        """Inicializa atributos del padre y añade nuevos."""
        super().__init__(marca, modelo, año)  # Llama al constructor del padre
        self.puertas = puertas
    
    def tocar_claxon(self):
        """Método específico del auto."""
        print("¡Beep beep!")


class Moto(Vehiculo):
    """Clase hija que representa una motocicleta."""
    
    def __init__(self, marca, modelo, año, tipo):
        """Inicializa atributos del padre y añade nuevos."""
        super().__init__(marca, modelo, año)
        self.tipo = tipo  # deportiva, cruiser, etc.
    
    def hacer_caballito(self):
        """Método específico de la moto."""
        print("¡Haciendo un caballito! 🏍️")


print("\n" + "=" * 60)
print("4. HERENCIA")
print("=" * 60)
mi_auto = Auto("Toyota", "Corolla", 2022, 4)
mi_moto = Moto("Yamaha", "R1", 2023, "deportiva")

print(mi_auto.descripcion())
mi_auto.tocar_claxon()
mi_auto.avanzar(50)

print(f"\n{mi_moto.descripcion()} - Tipo: {mi_moto.tipo}")
mi_moto.hacer_caballito()


# ============================================================================
# 5. ENCAPSULACIÓN - Atributos privados y propiedades
# ============================================================================

class CuentaBancaria:
    """Demuestra encapsulación con atributos privados."""
    
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa la cuenta."""
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (doble guión bajo)
    
    @property
    def saldo(self):
        """Getter para el saldo (solo lectura)."""
        return self.__saldo
    
    def depositar(self, cantidad):
        """Deposita dinero en la cuenta."""
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositado: ${cantidad}. Saldo actual: ${self.__saldo}")
        else:
            print("La cantidad debe ser positiva.")
    
    def retirar(self, cantidad):
        """Retira dinero de la cuenta."""
        if cantidad > self.__saldo:
            print("Fondos insuficientes.")
        elif cantidad > 0:
            self.__saldo -= cantidad
            print(f"Retirado: ${cantidad}. Saldo actual: ${self.__saldo}")
        else:
            print("La cantidad debe ser positiva.")


print("\n" + "=" * 60)
print("5. ENCAPSULACIÓN")
print("=" * 60)
cuenta = CuentaBancaria("Juan", 1000)
print(f"Saldo inicial: ${cuenta.saldo}")
cuenta.depositar(500)
cuenta.retirar(300)
# cuenta.__saldo = 999999  # Esto NO funciona (está protegido)
print(f"Saldo final: ${cuenta.saldo}")


# ============================================================================
# 6. MÉTODOS DE CLASE Y MÉTODOS ESTÁTICOS
# ============================================================================

class Empleado:
    """Demuestra métodos de clase y estáticos."""
    
    aumento_anual = 1.04  # Atributo de clase
    
    def __init__(self, nombre, salario):
        """Inicializa el empleado."""
        self.nombre = nombre
        self.salario = salario
    
    def aplicar_aumento(self):
        """Aplica el aumento anual al salario."""
        self.salario = int(self.salario * self.aumento_anual)
    
    @classmethod
    def cambiar_aumento(cls, nuevo_aumento):
        """Método de clase: modifica el atributo de clase."""
        cls.aumento_anual = nuevo_aumento
    
    @staticmethod
    def es_dia_laboral(dia):
        """Método estático: no necesita acceso a la instancia ni a la clase."""
        return dia not in ['sábado', 'domingo']


print("\n" + "=" * 60)
print("6. MÉTODOS DE CLASE Y ESTÁTICOS")
print("=" * 60)
emp1 = Empleado("Ana", 50000)
emp2 = Empleado("Carlos", 60000)

print(f"{emp1.nombre}: ${emp1.salario}")
emp1.aplicar_aumento()
print(f"Después del aumento: ${emp1.salario}")

Empleado.cambiar_aumento(1.05)  # Cambia para todos los empleados
emp2.aplicar_aumento()
print(f"{emp2.nombre} después del aumento: ${emp2.salario}")

print(f"¿Lunes es día laboral? {Empleado.es_dia_laboral('lunes')}")


# ============================================================================
# 7. COMPOSICIÓN - Una clase contiene otras clases
# ============================================================================

class Motor:
    """Representa el motor de un vehículo."""
    
    def __init__(self, tipo, caballos):
        self.tipo = tipo
        self.caballos = caballos
    
    def arrancar(self):
        print(f"Motor {self.tipo} de {self.caballos} HP arrancado.")


class Coche:
    """Un coche que contiene un motor (composición)."""
    
    def __init__(self, marca, modelo, tipo_motor, caballos):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor, caballos)  # Composición
    
    def encender(self):
        print(f"Encendiendo {self.marca} {self.modelo}...")
        self.motor.arrancar()


print("\n" + "=" * 60)
print("7. COMPOSICIÓN")
print("=" * 60)
mi_coche = Coche("Ford", "Mustang", "V8", 450)
mi_coche.encender()


# ============================================================================
# 8. EJEMPLO PRÁCTICO COMPLETO - Sistema de Estudiantes
# ============================================================================

class Persona:
    """Clase base para una persona."""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


class Estudiante(Persona):
    """Un estudiante que hereda de Persona."""
    
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.__calificaciones = []  # Lista privada
    
    def agregar_calificacion(self, materia, nota):
        """Agrega una calificación."""
        self.__calificaciones.append({'materia': materia, 'nota': nota})
    
    @property
    def promedio(self):
        """Calcula el promedio de calificaciones."""
        if not self.__calificaciones:
            return 0
        suma = sum(cal['nota'] for cal in self.__calificaciones)
        return suma / len(self.__calificaciones)
    
    def mostrar_calificaciones(self):
        """Muestra todas las calificaciones."""
        print(f"\nCalificaciones de {self.nombre} ({self.matricula}):")
        for cal in self.__calificaciones:
            print(f"  - {cal['materia']}: {cal['nota']}")
        print(f"  Promedio: {self.promedio:.2f}")


print("\n" + "=" * 60)
print("8. EJEMPLO PRÁCTICO - SISTEMA DE ESTUDIANTES")
print("=" * 60)
estudiante = Estudiante("María García", 20, "A12345")
print(estudiante.presentarse())
estudiante.agregar_calificacion("Matemáticas", 95)
estudiante.agregar_calificacion("Física", 88)
estudiante.agregar_calificacion("Programación", 100)
estudiante.mostrar_calificaciones()


print("\n" + "=" * 60)
print("¡GUÍA COMPLETA!")
print("=" * 60)
print("""
RESUMEN DE CONCEPTOS:
1. Clase básica con __init__ y métodos
2. Atributos de clase vs instancia
3. Métodos especiales (__str__, __repr__, __len__, etc.)
4. Herencia (super())
5. Encapsulación (atributos privados con __)
6. Métodos de clase (@classmethod) y estáticos (@staticmethod)
7. Composición (una clase contiene otra)
8. Ejemplo práctico completo
""")
