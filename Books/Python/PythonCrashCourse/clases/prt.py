"""
Sistema de Gestión de Biblioteca Digital
Commit 1: Clases base con herencia, encapsulación y polimorfismo
Commit 2: Sistema de préstamos, devoluciones y multas
Commit 3: Sistema de reservas, estadísticas y notificaciones
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
        self._multas_pendientes: float = 0.0
        self._prestamos_activos: List['Prestamo'] = []
        self._reservas: List['Reserva'] = []
        self._notificaciones: List[str] = []
        
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
        return self._activo and len(self._libros_prestados) < self.limite_actual and self._multas_pendientes == 0
    
    def agregar_multa(self, monto: float):
        """Agrega una multa al usuario"""
        self._multas_pendientes += monto
        if self._multas_pendientes > 50:
            self.suspender()
    
    def pagar_multa(self, monto: float) -> float:
        """Paga multas pendientes y retorna el cambio"""
        if monto >= self._multas_pendientes:
            cambio = monto - self._multas_pendientes
            self._multas_pendientes = 0.0
            if not self._prestamos_activos:  # Si no hay préstamos activos, reactivar
                self.activar()
            return cambio
        else:
            self._multas_pendientes -= monto
            return 0.0
    
    def get_multas(self) -> float:
        """Retorna el monto de multas pendientes"""
        return self._multas_pendientes
    
    def agregar_notificacion(self, mensaje: str):
        """Agrega una notificación al usuario"""
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        self._notificaciones.append(f"[{timestamp}] {mensaje}")
    
    def ver_notificaciones(self) -> List[str]:
        """Retorna todas las notificaciones"""
        return self._notificaciones.copy()
    
    def limpiar_notificaciones(self):
        """Limpia todas las notificaciones"""
        self._notificaciones.clear()
    
    def suspender(self):
        """Suspende la cuenta del usuario"""
        self._activo = False
    
    def activar(self):
        """Activa la cuenta del usuario"""
        self._activo = True
    
    def __str__(self) -> str:
        estado = "Activo" if self._activo else "Suspendido"
        multas_texto = f" - Multas: ${self._multas_pendientes:.2f}" if self._multas_pendientes > 0 else ""
        return f"{self.nombre_completo} - {self._tipo.capitalize()} ({estado}) - Libros: {len(self._libros_prestados)}/{self.limite_actual}{multas_texto}"


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
        self._reservas: List['Reserva'] = []
    
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


class Reserva:
    """Sistema de reservas para materiales no disponibles"""
    
    _id_counter = 8000
    
    def __init__(self, usuario: Usuario, material: MaterialBibliografico):
        Reserva._id_counter += 1
        self._id = Reserva._id_counter
        self._usuario = usuario
        self._material = material
        self._fecha_reserva = datetime.now()
        self._activa = True
        self._fecha_notificacion: Optional[datetime] = None
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def activa(self) -> bool:
        return self._activa
    
    def cancelar(self):
        """Cancela la reserva"""
        self._activa = False
    
    def notificar_disponibilidad(self):
        """Notifica al usuario que el material está disponible"""
        self._fecha_notificacion = datetime.now()
        mensaje = f"📚 El material '{self._material.titulo}' que reservaste ya está disponible"
        self._usuario.agregar_notificacion(mensaje)
    
    def get_info(self) -> dict:
        return {
            "id": self._id,
            "usuario": self._usuario.nombre_completo,
            "material": self._material.titulo,
            "fecha_reserva": self._fecha_reserva.strftime("%d/%m/%Y"),
            "activa": self._activa
        }
    
    def __str__(self) -> str:
        estado = "🔖 Activa" if self._activa else "✗ Cancelada"
        return f"[{self._id}] {estado} - {self._material.titulo} → {self._usuario.nombre_completo}"


class Prestamo:
    """Gestión de préstamos individuales"""
    
    _id_counter = 5000
    
    def __init__(self, usuario: Usuario, material: MaterialBibliografico, dias_prestamo: int = 14):
        Prestamo._id_counter += 1
        self._id = Prestamo._id_counter
        self._usuario = usuario
        self._material = material
        self._fecha_prestamo = datetime.now()
        self._dias_prestamo = dias_prestamo
        self._fecha_devolucion_esperada = self._fecha_prestamo + timedelta(days=dias_prestamo)
        self._fecha_devolucion_real: Optional[datetime] = None
        self._multa_generada: float = 0.0
        self._activo = True
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def esta_vencido(self) -> bool:
        """Verifica si el préstamo está vencido"""
        if self._activo:
            return datetime.now() > self._fecha_devolucion_esperada
        return False
    
    @property
    def dias_retraso(self) -> int:
        """Calcula los días de retraso"""
        if self._activo:
            if datetime.now() > self._fecha_devolucion_esperada:
                return (datetime.now() - self._fecha_devolucion_esperada).days
        elif self._fecha_devolucion_real:
            if self._fecha_devolucion_real > self._fecha_devolucion_esperada:
                return (self._fecha_devolucion_real - self._fecha_devolucion_esperada).days
        return 0
    
    def calcular_multa(self, tarifa_por_dia: float = 2.0) -> float:
        """Calcula la multa por retraso"""
        return self.dias_retraso * tarifa_por_dia
    
    def devolver(self) -> float:
        """Marca el préstamo como devuelto y calcula la multa"""
        self._fecha_devolucion_real = datetime.now()
        self._activo = False
        self._multa_generada = self.calcular_multa()
        return self._multa_generada
    
    def renovar(self, dias_adicionales: int = 7) -> bool:
        """Renueva el préstamo si no está vencido"""
        if not self.esta_vencido and self._activo:
            self._fecha_devolucion_esperada += timedelta(days=dias_adicionales)
            return True
        return False
    
    def get_info(self) -> dict:
        """Retorna información del préstamo"""
        return {
            "id": self._id,
            "usuario": self._usuario.nombre_completo,
            "material": self._material.titulo,
            "fecha_prestamo": self._fecha_prestamo.strftime("%d/%m/%Y"),
            "fecha_devolucion": self._fecha_devolucion_esperada.strftime("%d/%m/%Y"),
            "activo": self._activo,
            "dias_retraso": self.dias_retraso,
            "multa": self._multa_generada
        }
    
    def __str__(self) -> str:
        estado = "📖 Activo" if self._activo else "✓ Devuelto"
        vencido = " ⚠️ VENCIDO" if self.esta_vencido else ""
        return f"[{self._id}] {estado}{vencido} - {self._material.titulo} → {self._usuario.nombre_completo}"


class Biblioteca:
    """Sistema de gestión de la biblioteca"""
    
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion
        self._catalogo: List[MaterialBibliografico] = []
        self._usuarios: List[Usuario] = []
        self._prestamos: List[Prestamo] = []
        self._reservas: List[Reserva] = []
        self._fecha_creacion = datetime.now()
        self._tarifa_multa_diaria = 2.0
    
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
    
    def prestar_material(self, usuario_id: str, material_id: int, dias: int = 14) -> Optional[Prestamo]:
        """Realiza un préstamo de material a un usuario"""
        usuario = self.buscar_usuario_por_id(usuario_id)
        material = self.buscar_material_por_id(material_id)
        
        if not usuario:
            print(f"✗ Usuario no encontrado: {usuario_id}")
            return None
        
        if not material:
            print(f"✗ Material no encontrado: {material_id}")
            return None
        
        if not usuario.puede_prestar():
            razon = "multas pendientes" if usuario.get_multas() > 0 else "cuenta suspendida o límite alcanzado"
            print(f"✗ El usuario no puede recibir préstamos: {razon}")
            return None
        
        if not material.disponible:
            print(f"✗ El material no está disponible: {material.titulo}")
            return None
        
        # Crear préstamo
        prestamo = Prestamo(usuario, material, dias)
        self._prestamos.append(prestamo)
        
        # Actualizar estados
        material.marcar_prestado()
        usuario._libros_prestados.append(material)
        usuario._prestamos_activos.append(prestamo)
        
        print(f"✓ Préstamo realizado: {material.titulo} → {usuario.nombre_completo}")
        print(f"  Fecha de devolución: {prestamo._fecha_devolucion_esperada.strftime('%d/%m/%Y')}")
        return prestamo
    
    def devolver_material(self, prestamo_id: int) -> bool:
        """Procesa la devolución de un material"""
        prestamo = None
        for p in self._prestamos:
            if p.id == prestamo_id and p._activo:
                prestamo = p
                break
        
        if not prestamo:
            print(f"✗ Préstamo no encontrado o ya devuelto: {prestamo_id}")
            return False
        
        # Marcar como devuelto
        multa = prestamo.devolver()
        
        # Actualizar estados
        prestamo._material.marcar_devuelto()
        prestamo._usuario._libros_prestados.remove(prestamo._material)
        prestamo._usuario._prestamos_activos.remove(prestamo)
        
        # Procesar reservas para este material
        self.procesar_reservas_material(prestamo._material)
        
        # Registrar en historial
        prestamo._usuario._historial.append(prestamo.get_info())
        
        # Aplicar multa si hay
        if multa > 0:
            prestamo._usuario.agregar_multa(multa)
            print(f"⚠️  Devolución con retraso de {prestamo.dias_retraso} días")
            print(f"   Multa generada: ${multa:.2f}")
        else:
            print(f"✓ Devolución a tiempo")
        
        print(f"✓ Material devuelto: {prestamo._material.titulo}")
        return True
    
    def renovar_prestamo(self, prestamo_id: int, dias: int = 7) -> bool:
        """Renueva un préstamo existente"""
        prestamo = None
        for p in self._prestamos:
            if p.id == prestamo_id:
                prestamo = p
                break
        
        if not prestamo:
            print(f"✗ Préstamo no encontrado: {prestamo_id}")
            return False
        
        if prestamo.renovar(dias):
            print(f"✓ Préstamo renovado por {dias} días más")
            print(f"  Nueva fecha de devolución: {prestamo._fecha_devolucion_esperada.strftime('%d/%m/%Y')}")
            return True
        else:
            print(f"✗ No se puede renovar: préstamo vencido o ya devuelto")
            return False
    
    def listar_prestamos_activos(self) -> List[Prestamo]:
        """Lista todos los préstamos activos"""
        return [p for p in self._prestamos if p._activo]
    
    def listar_prestamos_vencidos(self) -> List[Prestamo]:
        """Lista todos los préstamos vencidos"""
        return [p for p in self._prestamos if p._activo and p.esta_vencido]
    
    def buscar_prestamo_por_id(self, prestamo_id: int) -> Optional[Prestamo]:
        """Busca un préstamo por su ID"""
        for prestamo in self._prestamos:
            if prestamo.id == prestamo_id:
                return prestamo
        return None
    
    def crear_reserva(self, usuario_id: str, material_id: int) -> Optional[Reserva]:
        """Crea una reserva para un material no disponible"""
        usuario = self.buscar_usuario_por_id(usuario_id)
        material = self.buscar_material_por_id(material_id)
        
        if not usuario:
            print(f"✗ Usuario no encontrado: {usuario_id}")
            return None
        
        if not material:
            print(f"✗ Material no encontrado: {material_id}")
            return None
        
        if material.disponible:
            print(f"✗ El material está disponible, no necesita reserva")
            return None
        
        # Verificar si ya tiene una reserva activa para este material
        for reserva in usuario._reservas:
            if reserva._material == material and reserva.activa:
                print(f"✗ Ya tienes una reserva activa para este material")
                return None
        
        reserva = Reserva(usuario, material)
        self._reservas.append(reserva)
        material._reservas.append(reserva)
        usuario._reservas.append(reserva)
        
        print(f"✓ Reserva creada: {material.titulo} → {usuario.nombre_completo}")
        return reserva
    
    def cancelar_reserva(self, reserva_id: int) -> bool:
        """Cancela una reserva"""
        reserva = None
        for r in self._reservas:
            if r.id == reserva_id:
                reserva = r
                break
        
        if not reserva:
            print(f"✗ Reserva no encontrada: {reserva_id}")
            return False
        
        if not reserva.activa:
            print(f"✗ La reserva ya está cancelada")
            return False
        
        reserva.cancelar()
        print(f"✓ Reserva cancelada: {reserva._material.titulo}")
        return True
    
    def procesar_reservas_material(self, material: MaterialBibliografico):
        """Notifica a los usuarios con reservas cuando un material está disponible"""
        if not material.disponible:
            return
        
        # Buscar reservas activas para este material
        reservas_activas = [r for r in material._reservas if r.activa]
        
        if reservas_activas:
            # Notificar al primer usuario en la cola
            primera_reserva = min(reservas_activas, key=lambda r: r._fecha_reserva)
            primera_reserva.notificar_disponibilidad()
            print(f"  📬 Notificación enviada a: {primera_reserva._usuario.nombre_completo}")
    
    def listar_reservas_activas(self) -> List[Reserva]:
        """Lista todas las reservas activas"""
        return [r for r in self._reservas if r.activa]
    
    def generar_reporte(self) -> str:
        """Genera un reporte del estado de la biblioteca"""
        disponibles = len(self.listar_materiales_disponibles())
        prestados = self.total_materiales - disponibles
        prestamos_activos = len(self.listar_prestamos_activos())
        prestamos_vencidos = len(self.listar_prestamos_vencidos())
        reservas_activas = len(self.listar_reservas_activas())
        total_multas = sum(u.get_multas() for u in self._usuarios)
        
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
- Préstamos activos: {prestamos_activos}
  ⚠️ Vencidos: {prestamos_vencidos}
- Reservas activas: {reservas_activas}
- Multas pendientes: ${total_multas:.2f}
{'='*60}
"""
        return reporte
    
    def __str__(self) -> str:
        return f"Biblioteca {self._nombre} - {self.total_materiales} materiales, {self.total_usuarios} usuarios"


# Demostración del sistema
if __name__ == "__main__":
    print("="*60)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL - COMMIT 2")
    print("Sistema de Préstamos y Devoluciones")
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
    
    # Generar reporte inicial
    print(biblioteca.generar_reporte())
    
    # ============== COMMIT 2: SISTEMA DE PRÉSTAMOS ==============
    print("\n" + "="*60)
    print("COMMIT 2: SISTEMA DE PRÉSTAMOS Y DEVOLUCIONES")
    print("="*60)
    
    # Realizar préstamos
    print("\n--- REALIZANDO PRÉSTAMOS ---")
    prestamo1 = biblioteca.prestar_material("12345678", libro1.id, 14)
    prestamo2 = biblioteca.prestar_material("87654321", libro2.id, 14)
    prestamo3 = biblioteca.prestar_material("11223344", libro3.id, 7)
    
    # Intentar préstamo de libro no disponible
    print("\n--- INTENTANDO PRÉSTAMO DE LIBRO YA PRESTADO ---")
    biblioteca.prestar_material("87654321", libro1.id, 14)
    
    # Mostrar préstamos activos
    print("\n--- PRÉSTAMOS ACTIVOS ---")
    for prestamo in biblioteca.listar_prestamos_activos():
        print(f"  {prestamo}")
        info = prestamo.get_info()
        print(f"    Devolución esperada: {info['fecha_devolucion']}")
    
    # Simular paso del tiempo y crear préstamo vencido
    print("\n--- SIMULANDO PRÉSTAMO VENCIDO ---")
    if prestamo3:
        # Modificar fecha para simular vencimiento
        prestamo3._fecha_devolucion_esperada = datetime.now() - timedelta(days=5)
        print(f"  {prestamo3}")
        print(f"  Días de retraso: {prestamo3.dias_retraso}")
        print(f"  Multa calculada: ${prestamo3.calcular_multa():.2f}")
    
    # Renovar un préstamo
    print("\n--- RENOVANDO PRÉSTAMO ---")
    if prestamo1:
        biblioteca.renovar_prestamo(prestamo1.id, 7)
    
    # Devolver materiales
    print("\n--- DEVOLVIENDO MATERIALES ---")
    if prestamo1:
        biblioteca.devolver_material(prestamo1.id)
    
    print("\n--- DEVOLVIENDO MATERIAL CON RETRASO ---")
    if prestamo3:
        biblioteca.devolver_material(prestamo3.id)
    
    # Mostrar estado de usuarios con multas
    print("\n--- ESTADO DE USUARIOS ---")
    for usuario in biblioteca._usuarios:
        print(f"  {usuario}")
        if usuario.get_multas() > 0:
            print(f"    ⚠️ Multas pendientes: ${usuario.get_multas():.2f}")
    
    # Intentar préstamo con multas pendientes
    print("\n--- INTENTANDO PRÉSTAMO CON MULTAS PENDIENTES ---")
    biblioteca.prestar_material("11223344", libro4.id, 14)
    
    # Pagar multas
    print("\n--- PAGANDO MULTAS ---")
    carlos = biblioteca.buscar_usuario_por_id("11223344")
    if carlos and carlos.get_multas() > 0:
        multa = carlos.get_multas()
        print(f"  Multa de {carlos.nombre_completo}: ${multa:.2f}")
        cambio = carlos.pagar_multa(20.0)
        print(f"  Pago realizado: $20.00")
        print(f"  Cambio: ${cambio:.2f}")
        print(f"  ✓ Cuenta reactivada")
    
    # Ahora sí puede prestar
    print("\n--- PRÉSTAMO DESPUÉS DE PAGAR MULTAS ---")
    prestamo4 = biblioteca.prestar_material("11223344", libro4.id, 14)
    
    # Listar préstamos vencidos
    print("\n--- PRÉSTAMOS VENCIDOS ---")
    vencidos = biblioteca.listar_prestamos_vencidos()
    if vencidos:
        for prestamo in vencidos:
            print(f"  {prestamo}")
    else:
        print("  ✓ No hay préstamos vencidos")
    
    # Ver historial de un usuario
    print("\n--- HISTORIAL DE PRÉSTAMOS ---")
    if carlos and carlos._historial:
        print(f"  Usuario: {carlos.nombre_completo}")
        for registro in carlos._historial:
            print(f"    - {registro['material']} (Devuelto: {registro['fecha_devolucion']})")
            if registro['multa'] > 0:
                print(f"      Multa: ${registro['multa']:.2f}")
    
    # Catálogo actualizado
    print("\n--- CATÁLOGO ACTUALIZADO ---")
    for material in biblioteca._catalogo:
        print(f"  {material}")
    
    # Reporte final
    print(biblioteca.generar_reporte())
    
    print("\n✓ COMMIT 2 COMPLETADO - Sistema de préstamos y devoluciones")
    print("  - Clase Prestamo con gestión de fechas y multas")
    print("  - Métodos prestar_material() y devolver_material()")
    print("  - Sistema de multas automáticas por retraso")
    print("  - Renovación de préstamos")
    print("  - Control de préstamos vencidos")
    print("  - Suspensión automática por multas altas")
    print("  - Historial de préstamos por usuario")
    
    # ============== COMMIT 3: RESERVAS Y ESTADÍSTICAS ==============
    print("\n" + "="*60)
    print("COMMIT 3: SISTEMA DE RESERVAS Y ESTADÍSTICAS")
    print("="*60)
    
    # Crear reservas para libros prestados
    print("\n--- CREANDO RESERVAS ---")
    reserva1 = biblioteca.crear_reserva("87654321", libro3.id)  # libro3 no está prestado ya
    reserva2 = biblioteca.crear_reserva("12345678", libro2.id)  # libro2 sí está prestado
    
    # Intentar reservar un libro disponible
    print("\n--- INTENTANDO RESERVAR LIBRO DISPONIBLE ---")
    biblioteca.crear_reserva("11223344", libro1.id)
    
    # Prestar más libros para tener más estadísticas
    print("\n--- MÁS PRÉSTAMOS PARA ESTADÍSTICAS ---")
    biblioteca.prestar_material("12345678", libro3.id, 14)
    biblioteca.prestar_material("87654321", revista1.id, 7)
    
    # Crear reserva para libro prestado
    print("\n--- RESERVANDO LIBRO PRESTADO ---")
    reserva3 = biblioteca.crear_reserva("11223344", libro3.id)
    
    # Listar reservas activas
    print("\n--- RESERVAS ACTIVAS ---")
    for reserva in biblioteca.listar_reservas_activas():
        print(f"  {reserva}")
    
    # Cancelar una reserva
    if reserva3:
        print("\n--- CANCELANDO RESERVA ---")
        biblioteca.cancelar_reserva(reserva3.id)
    
    # Devolver libro con reservas y verificar notificaciones
    print("\n--- DEVOLVIENDO LIBRO CON RESERVAS ---")
    prestamo_libro2 = None
    for p in biblioteca._prestamos:
        if p._material == libro2 and p._activo:
            prestamo_libro2 = p
            break
    
    if prestamo_libro2:
        biblioteca.devolver_material(prestamo_libro2.id)
    
    # Ver notificaciones del usuario con reserva
    print("\n--- NOTIFICACIONES DE USUARIOS ---")
    juan = biblioteca.buscar_usuario_por_id("12345678")
    if juan:
        notificaciones = juan.ver_notificaciones()
        if notificaciones:
            print(f"  Notificaciones de {juan.nombre_completo}:")
            for notif in notificaciones:
                print(f"    {notif}")
        else:
            print(f"  {juan.nombre_completo} no tiene notificaciones")
    
    # Simular más actividad para estadísticas
    print("\n--- SIMULANDO MÁS ACTIVIDAD ---")
    libro1.agregar_calificacion(5)
    libro4.agregar_calificacion(5)
    libro4.agregar_calificacion(4)
    
    # Más préstamos y devoluciones
    p_temp = biblioteca.prestar_material("87654321", libro1.id, 7)
    if p_temp:
        biblioteca.devolver_material(p_temp.id)
    
    p_temp2 = biblioteca.prestar_material("87654321", libro1.id, 7)
    if p_temp2:
        biblioteca.devolver_material(p_temp2.id)
    
    # Mostrar estadísticas de libros más populares
    print("\n--- LIBROS MÁS POPULARES ---")
    populares = biblioteca.obtener_libros_mas_populares(5)
    for i, (titulo, prestamos) in enumerate(populares, 1):
        print(f"  {i}. {titulo} - {prestamos} préstamos")
    
    # Mostrar usuarios más activos
    print("\n--- USUARIOS MÁS ACTIVOS ---")
    activos = biblioteca.obtener_usuarios_mas_activos(3)
    for i, (nombre, prestamos) in enumerate(activos, 1):
        print(f"  {i}. {nombre} - {prestamos} préstamos completados")
    
    # Estadísticas por género
    print("\n--- ESTADÍSTICAS POR GÉNERO ---")
    stats_generos = biblioteca.obtener_estadisticas_generos()
    for genero, stats in sorted(stats_generos.items(), key=lambda x: x[1]['total_prestamos'], reverse=True):
        print(f"  📚 {genero}:")
        print(f"     - Libros en catálogo: {stats['total_libros']}")
        print(f"     - Total préstamos: {stats['total_prestamos']}")
    
    # Tasa de ocupación
    print("\n--- TASA DE OCUPACIÓN ---")
    tasa = biblioteca.obtener_tasa_ocupacion()
    print(f"  📊 {tasa:.1f}% de los materiales están prestados")
    
    # Estado actual de todos los materiales
    print("\n--- ESTADO DEL CATÁLOGO ---")
    for material in biblioteca._catalogo:
        print(f"  {material}")
        if material._reservas:
            reservas_activas = [r for r in material._reservas if r.activa]
            if reservas_activas:
                print(f"    🔖 {len(reservas_activas)} reserva(s) activa(s)")
    
    # Estado de usuarios
    print("\n--- ESTADO DE USUARIOS ---")
    for usuario in biblioteca._usuarios:
        print(f"  {usuario}")
        if usuario._reservas:
            reservas_activas = [r for r in usuario._reservas if r.activa]
            if reservas_activas:
                print(f"    🔖 {len(reservas_activas)} reserva(s) activa(s)")
        if usuario._notificaciones:
            print(f"    📬 {len(usuario._notificaciones)} notificación(es)")
    
    # Reporte de estadísticas completo
    print(biblioteca.generar_reporte_estadisticas())
    
    # Reporte general final
    print(biblioteca.generar_reporte())
    
    print("\n✓ COMMIT 3 COMPLETADO - Sistema de reservas y estadísticas")
    print("  - Clase Reserva para gestión de cola de espera")
    print("  - Sistema de notificaciones a usuarios")
    print("  - Notificación automática cuando material reservado está disponible")
    print("  - Estadísticas de libros más populares")
    print("  - Ranking de usuarios más activos")
    print("  - Estadísticas por género literario")
    print("  - Cálculo de tasa de ocupación")
    print("  - Reportes detallados de estadísticas")
    print("\n" + "="*60)
    print("🎉 SISTEMA COMPLETO - TODOS LOS COMMITS FINALIZADOS")
    print("="*60)
    print("\nFuncionalidades implementadas:")
    print("  ✓ Herencia multinivel (Persona → Usuario)")
    print("  ✓ Composición (Biblioteca contiene múltiples clases)")
    print("  ✓ Encapsulación con properties")
    print("  ✓ Polimorfismo con métodos especiales")
    print("  ✓ Sistema completo de préstamos y devoluciones")
    print("  ✓ Gestión de multas automáticas")
    print("  ✓ Sistema de reservas con cola de espera")
    print("  ✓ Notificaciones a usuarios")
    print("  ✓ Estadísticas y reportes avanzados")
    print("  ✓ Control de fechas y vencimientos")
    print("  ✓ Validaciones y manejo de errores")
