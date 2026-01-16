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


