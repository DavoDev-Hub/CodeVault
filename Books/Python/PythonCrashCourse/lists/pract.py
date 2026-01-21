# Ejercicio: Lista de invitados a una fiesta
# Practicar agregación, eliminación y bucles con listas

invitados = ['Ana', 'Carlos', 'María', 'Luis', 'Sofia']

print("Invitados originales:")
for invitado in invitados:
    print(f"- {invitado}")

# Alguien no puede asistir
no_puede_asistir = invitados.pop(1)
print(f"\n{no_puede_asistir} no puede asistir a la fiesta")

# Invitar a alguien más en su lugar
nuevo_invitado = 'Pedro'
invitados.insert(1, nuevo_invitado)
print(f"Invitando a {nuevo_invitado} en su lugar")

# Encontramos una mesa más grande, añadimos más invitados
invitados.insert(0, 'Elena')
invitados.insert(len(invitados)//2, 'Jorge')
invitados.append('Laura')

print("\nLista actualizada de invitados:")
for i, invitado in enumerate(invitados, 1):
    print(f"{i}. {invitado}")

# Solo podemos invitar a 2 personas (mesa pequeña de nuevo)
print("\nLo siento, solo puedo invitar a 2 personas")
while len(invitados) > 2:
    eliminado = invitados.pop()
    print(f"Lo siento {eliminado}, no puedo invitarte")

print("\nInvitados confirmados:")
for invitado in invitados:
    print(f"{invitado}, sigues invitado a la fiesta!")

# Vaciar la lista
del invitados[:]
print(f"\nLista final de invitados: {invitados}")
print(f"Número de invitados: {len(invitados)}")
