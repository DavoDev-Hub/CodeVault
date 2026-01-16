"""
Ejercicio de Clases: Sistema de Biblioteca
Este ejercicio crea un sistema simple de gestión de biblioteca
"""

class Libro:
    """Representa un libro en la biblioteca"""
    
    def __init__(self, titulo, autor, isbn, disponible=True):
        """Inicializa los atributos del libro"""
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    
    def prestar(self):
        """Marca el libro como prestado"""
        if self.disponible:
            self.disponible = False
            print(f"'{self.titulo}' ha sido prestado.")
        else:
            print(f"'{self.titulo}' no está disponible.")
    
    def devolver(self):
        """Marca el libro como devuelto"""
        if not self.disponible:
            self.disponible = True
            print(f"'{self.titulo}' ha sido devuelto.")
        else:
            print(f"'{self.titulo}' ya estaba disponible.")
    
    def mostrar_info(self):
        """Muestra la información del libro"""
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"\nTítulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Estado: {estado}")


class Biblioteca:
    """Representa una biblioteca que contiene libros"""
    
    def __init__(self, nombre):
        """Inicializa la biblioteca"""
        self.nombre = nombre
        self.libros = []
    
    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca"""
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a {self.nombre}.")
    
    def mostrar_catalogo(self):
        """Muestra todos los libros en la biblioteca"""
        print(f"\n{'='*50}")
        print(f"Catálogo de {self.nombre}")
        print(f"{'='*50}")
        if self.libros:
            for i, libro in enumerate(self.libros, 1):
                estado = "✓ Disponible" if libro.disponible else "✗ Prestado"
                print(f"{i}. {libro.titulo} - {libro.autor} [{estado}]")
        else:
            print("No hay libros en la biblioteca.")
    
    def buscar_libro(self, titulo):
        """Busca un libro por título"""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    
    def libros_disponibles(self):
        """Retorna la cantidad de libros disponibles"""
        return sum(1 for libro in self.libros if libro.disponible)


# Programa principal
if __name__ == "__main__":
    # Crear una biblioteca
    mi_biblioteca = Biblioteca("Biblioteca Municipal")
    
    # Crear algunos libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728")
    libro2 = Libro("1984", "George Orwell", "978-0451524935")
    libro3 = Libro("El Quijote", "Miguel de Cervantes", "978-8491050636")
    libro4 = Libro("Python Crash Course", "Eric Matthes", "978-1593279288")
    
    # Agregar libros a la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)
    mi_biblioteca.agregar_libro(libro4)
    
    # Mostrar catálogo completo
    mi_biblioteca.mostrar_catalogo()
    
    # Realizar algunas operaciones
    print("\n" + "="*50)
    print("Operaciones de préstamo")
    print("="*50)
    
    libro1.prestar()
    libro2.prestar()
    
    # Mostrar catálogo actualizado
    mi_biblioteca.mostrar_catalogo()
    
    # Mostrar información detallada de un libro
    libro1.mostrar_info()
    
    # Devolver un libro
    print("\n" + "="*50)
    print("Operaciones de devolución")
    print("="*50)
    libro1.devolver()
    
    # Mostrar estadísticas
    print(f"\nLibros disponibles: {mi_biblioteca.libros_disponibles()}/{len(mi_biblioteca.libros)}")
    
    # Buscar un libro
    print("\n" + "="*50)
    print("Búsqueda de libro")
    print("="*50)
    libro_buscado = mi_biblioteca.buscar_libro("1984")
    if libro_buscado:
        libro_buscado.mostrar_info()
    else:
        print("Libro no encontrado.")
