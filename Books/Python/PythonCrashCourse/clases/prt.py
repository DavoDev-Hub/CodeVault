"""
Sistema de Gestión de Biblioteca Digital
Commit 1: Clases base con herencia, encapsulación y polimorfismo
"""

from datetime import datetime, timedelta
from typing import List, Optional


class Persona:
    """Clase base para personas en el sistema"""
    
    def __init__(self, nombre: str, apellido: str, identificacion: str, email: str):
        self._nombre = nombre
        self._apellido = apellido
        self._identificacion = identificacion
        self._email = email
        self._fecha_registro = datetime.now()
    
    @property
    def nombre_completo(self) -> str:
        """Retorna el nombre completo"""
        return f"{self._nombre} {self._apellido}"
    
    @property
    def identificacion(self) -> str:
        """Retorna la identificación (solo lectura)"""
        return self._identificacion
    
    def __str__(self) -> str:
        return f"{self.nombre_completo} ({self._identificacion})"
    
    def __repr__(self) -> str:
        return f"Persona('{self._nombre}', '{self._apellido}', '{self._identificacion}')"


class Usuario(Persona):
    """Usuario de la biblioteca con límites de préstamos"""
    
    def __init__(self, nombre: str, apellido: str, identificacion: str, 
                 email: str, tipo: str = "regular"):
        super().__init__(nombre, apellido, identificacion, email)
        self._tipo = tipo  # "regular", "premium", "estudiante"
        self._libros_prestados: List['Libro'] = []
        self._historial: List[dict] = []
        self._activo = True
        
        # Límites según tipo de usuario
        self._limite_prestamos = {
            "regular": 3,
            "premium": 10,
            "estudiante": 5
        }
    
    @property
    def limite_actual(self) -> int:
        """Retorna el límite de préstamos según el tipo de usuario"""
        return self._limite_prestamos.get(self._tipo, 3)
    
    @property
    def libros_disponibles(self) -> int:
        """Retorna cuántos libros más puede pedir prestados"""
        return self.limite_actual - len(self._libros_prestados)
    
    @property
    def tipo(self) -> str:
        return self._tipo
    
    @tipo.setter
    def tipo(self, nuevo_tipo: str):
        """Cambia el tipo de usuario"""
        if nuevo_tipo in self._limite_prestamos:
            self._tipo = nuevo_tipo
        else:
            raise ValueError(f"Tipo de usuario inválido: {nuevo_tipo}")
    
    def puede_prestar(self) -> bool:
        """Verifica si el usuario puede recibir más préstamos"""
        return self._activo and len(self._libros_prestados) < self.limite_actual
    
    def suspender(self):
        """Suspende la cuenta del usuario"""
        self._activo = False
    
    def activar(self):
        """Activa la cuenta del usuario"""
        self._activo = True
    
    def __str__(self) -> str:
        estado = "Activo" if self._activo else "Suspendido"
        return f"{self.nombre_completo} - {self._tipo.capitalize()} ({estado}) - Libros: {len(self._libros_prestados)}/{self.limite_actual}"


class MaterialBibliografico:
    """Clase base para materiales de la biblioteca"""
    
    _id_counter = 1000
    
    def __init__(self, titulo: str, autor: str, año: int, editorial: str):
        MaterialBibliografico._id_counter += 1
        self._id = MaterialBibliografico._id_counter
        self._titulo = titulo
        self._autor = autor
        self._año = año
        self._editorial = editorial
        self._disponible = True
        self._veces_prestado = 0
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def disponible(self) -> bool:
        return self._disponible
    
    def marcar_prestado(self):
        """Marca el material como prestado"""
        self._disponible = False
        self._veces_prestado += 1
    
    def marcar_devuelto(self):
        """Marca el material como devuelto"""
        self._disponible = True
    
    def get_info_basica(self) -> dict:
        """Retorna información básica del material"""
        return {
            "id": self._id,
            "titulo": self._titulo,
            "autor": self._autor,
            "año": self._año,
            "disponible": self._disponible
        }
    
    def __str__(self) -> str:
        estado = "Disponible" if self._disponible else "Prestado"
        return f"[{self._id}] {self._titulo} - {self._autor} ({estado})"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, MaterialBibliografico):
            return self._id == other._id
        return False


class Libro(MaterialBibliografico):
    """Clase específica para libros"""
    
    def __init__(self, titulo: str, autor: str, año: int, editorial: str,
                 isbn: str, paginas: int, genero: str = "General"):
        super().__init__(titulo, autor, año, editorial)
        self._isbn = isbn
        self._paginas = paginas
        self._genero = genero
        self._calificaciones: List[int] = []
    
    @property
    def isbn(self) -> str:
        return self._isbn
    
    @property
    def genero(self) -> str:
        return self._genero
    
    @property
    def calificacion_promedio(self) -> float:
        """Calcula la calificación promedio del libro"""
        if not self._calificaciones:
            return 0.0
        return sum(self._calificaciones) / len(self._calificaciones)
    
    def agregar_calificacion(self, calificacion: int):
        """Agrega una calificación (1-5)"""
        if 1 <= calificacion <= 5:
            self._calificaciones.append(calificacion)
        else:
            raise ValueError("La calificación debe estar entre 1 y 5")
    
    def get_info_completa(self) -> dict:
        """Retorna información completa del libro"""
        info = self.get_info_basica()
        info.update({
            "isbn": self._isbn,
            "paginas": self._paginas,
            "genero": self._genero,
            "veces_prestado": self._veces_prestado,
            "calificacion": round(self.calificacion_promedio, 2)
        })
        return info
    
    def __str__(self) -> str:
        estado = "✓" if self._disponible else "✗"
        estrellas = "★" * int(self.calificacion_promedio)
        return f"{estado} [{self._id}] {self._titulo} - {self._autor} | {self._genero} | {estrellas}"


class Revista(MaterialBibliografico):
    """Clase específica para revistas"""
    
    def __init__(self, titulo: str, autor: str, año: int, editorial: str,
                 numero: int, mes: str, issn: str):
        super().__init__(titulo, autor, año, editorial)
        self._numero = numero
        self._mes = mes
        self._issn = issn
    
    @property
    def numero(self) -> int:
        return self._numero
    
    def __str__(self) -> str:
        estado = "✓" if self._disponible else "✗"
        return f"{estado} [{self._id}] {self._titulo} - Nº{self._numero} ({self._mes}/{self._año})"


class Biblioteca:
    """Sistema de gestión de la biblioteca"""
    
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion
        self._catalogo: List[MaterialBibliografico] = []
        self._usuarios: List[Usuario] = []
        self._fecha_creacion = datetime.now()
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def total_materiales(self) -> int:
        return len(self._catalogo)
    
    @property
    def total_usuarios(self) -> int:
        return len(self._usuarios)
    
    def agregar_material(self, material: MaterialBibliografico):
        """Agrega un material al catálogo"""
        self._catalogo.append(material)
        print(f"✓ Material agregado: {material.titulo} (ID: {material.id})")
    
    def registrar_usuario(self, usuario: Usuario):
        """Registra un nuevo usuario"""
        if usuario not in self._usuarios:
            self._usuarios.append(usuario)
            print(f"✓ Usuario registrado: {usuario.nombre_completo}")
        else:
            print(f"✗ El usuario ya está registrado")
    
    def buscar_material_por_id(self, material_id: int) -> Optional[MaterialBibliografico]:
        """Busca un material por su ID"""
        for material in self._catalogo:
            if material.id == material_id:
                return material
        return None
    
    def buscar_materiales_por_titulo(self, titulo: str) -> List[MaterialBibliografico]:
        """Busca materiales por título (búsqueda parcial)"""
        titulo_lower = titulo.lower()
        return [m for m in self._catalogo if titulo_lower in m.titulo.lower()]
    
    def buscar_libros_por_genero(self, genero: str) -> List[Libro]:
        """Busca libros por género"""
        genero_lower = genero.lower()
        return [m for m in self._catalogo 
                if isinstance(m, Libro) and genero_lower in m.genero.lower()]
    
    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su identificación"""
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None
    
    def listar_materiales_disponibles(self) -> List[MaterialBibliografico]:
        """Lista todos los materiales disponibles"""
        return [m for m in self._catalogo if m.disponible]
    
    def generar_reporte(self) -> str:
        """Genera un reporte del estado de la biblioteca"""
        disponibles = len(self.listar_materiales_disponibles())
        prestados = self.total_materiales - disponibles
        
        reporte = f"""
{'='*60}
BIBLIOTECA: {self._nombre}
Dirección: {self._direccion}
{'='*60}
ESTADÍSTICAS:
- Total de materiales: {self.total_materiales}
  ✓ Disponibles: {disponibles}
  ✗ Prestados: {prestados}
- Total de usuarios: {self.total_usuarios}
{'='*60}
"""
        return reporte
    
    def __str__(self) -> str:
        return f"Biblioteca {self._nombre} - {self.total_materiales} materiales, {self.total_usuarios} usuarios"


# Demostración del sistema (Commit 1)
if __name__ == "__main__":
    print("="*60)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL - COMMIT 1")
    print("="*60)
    
    # Crear biblioteca
    biblioteca = Biblioteca("Biblioteca Central", "Av. Principal 123")
    print(f"\n📚 {biblioteca}")
    
    # Agregar libros al catálogo
    print("\n--- AGREGANDO LIBROS AL CATÁLOGO ---")
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967,
                   "Editorial Sudamericana", "978-0307474728", 417, "Realismo Mágico")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605,
                   "Francisco de Robles", "978-8424936471", 863, "Clásico")
    libro3 = Libro("1984", "George Orwell", 1949,
                   "Secker & Warburg", "978-0451524935", 328, "Ciencia Ficción")
    libro4 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943,
                   "Reynal & Hitchcock", "978-0156012195", 96, "Infantil")
    
    biblioteca.agregar_material(libro1)
    biblioteca.agregar_material(libro2)
    biblioteca.agregar_material(libro3)
    biblioteca.agregar_material(libro4)
    
    # Agregar revistas
    revista1 = Revista("National Geographic", "Varios Autores", 2026,
                      "National Geographic Society", 1, "Enero", "0027-9358")
    biblioteca.agregar_material(revista1)
    
    # Registrar usuarios
    print("\n--- REGISTRANDO USUARIOS ---")
    usuario1 = Usuario("Juan", "Pérez", "12345678", "juan@email.com", "regular")
    usuario2 = Usuario("María", "González", "87654321", "maria@email.com", "premium")
    usuario3 = Usuario("Carlos", "Rodríguez", "11223344", "carlos@email.com", "estudiante")
    
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    biblioteca.registrar_usuario(usuario3)
    
    # Mostrar usuarios
    print("\n--- USUARIOS REGISTRADOS ---")
    for usuario in biblioteca._usuarios:
        print(f"  {usuario}")
    
    # Agregar calificaciones a los libros
    print("\n--- AGREGANDO CALIFICACIONES ---")
    libro1.agregar_calificacion(5)
    libro1.agregar_calificacion(5)
    libro1.agregar_calificacion(4)
    libro2.agregar_calificacion(5)
    libro2.agregar_calificacion(5)
    libro3.agregar_calificacion(4)
    libro3.agregar_calificacion(5)
    libro3.agregar_calificacion(4)
    print("✓ Calificaciones agregadas")
    
    # Listar catálogo
    print("\n--- CATÁLOGO COMPLETO ---")
    for material in biblioteca._catalogo:
        print(f"  {material}")
    
    # Buscar libros por género
    print("\n--- BÚSQUEDA POR GÉNERO: 'Ciencia Ficción' ---")
    libros_cf = biblioteca.buscar_libros_por_genero("Ciencia Ficción")
    for libro in libros_cf:
        print(f"  {libro}")
    
    # Buscar por título
    print("\n--- BÚSQUEDA POR TÍTULO: 'el' ---")
    resultados = biblioteca.buscar_materiales_por_titulo("el")
    for material in resultados:
        print(f"  {material}")
    
    # Cambiar tipo de usuario
    print("\n--- CAMBIO DE TIPO DE USUARIO ---")
    print(f"Antes: {usuario1}")
    usuario1.tipo = "premium"
    print(f"Después: {usuario1}")
    
    # Generar reporte
    print(biblioteca.generar_reporte())
    
    print("\n✓ COMMIT 1 COMPLETADO - Clases base implementadas")
    print("  - Herencia: Persona → Usuario, MaterialBibliografico → Libro/Revista")
    print("  - Encapsulación: Atributos privados con properties")
    print("  - Polimorfismo: Métodos __str__ personalizados")
    print("  - Composición: Biblioteca contiene Materiales y Usuarios")
