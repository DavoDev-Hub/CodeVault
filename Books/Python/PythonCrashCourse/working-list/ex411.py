pizzas = ["Peperoni", "Salchicha", "Carnes", "Queso"]
friends_pizzas = pizzas[:]
pizzas.append("Mexicana")
friends_pizzas.append("Hawaiana")

print("My favorite pizzas: ")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas")
for fp in friends_pizzas:
    print(fp)
