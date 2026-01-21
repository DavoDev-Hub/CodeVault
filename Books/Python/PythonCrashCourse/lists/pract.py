# Ejercicio: Gestión de una lista de tareas
# Crear una lista de tareas pendientes y practicar diferentes operaciones

tareas = ['estudiar python', 'hacer ejercicio', 'leer un libro', 'cocinar', 'llamar a un amigo']

print("Lista original de tareas:")
print(tareas)

# Añadir una nueva tarea al final
tareas.append('meditar')
print("\nDespués de añadir 'meditar':")
print(tareas)

# Insertar una tarea urgente al principio
tareas.insert(0, 'revisar emails')
print("\nDespués de insertar tarea urgente:")
print(tareas)

# Eliminar una tarea completada
tarea_completada = tareas.pop(2)
print(f"\nTarea completada: {tarea_completada}")
print("Tareas restantes:")
print(tareas)

# Ordenar la lista alfabéticamente
tareas.sort()
print("\nTareas ordenadas alfabéticamente:")
print(tareas)

# Mostrar el número de tareas pendientes
print(f"\nTienes {len(tareas)} tareas pendientes")

# Acceder a la primera y última tarea
print(f"Primera tarea: {tareas[0]}")
print(f"Última tarea: {tareas[-1]}")
