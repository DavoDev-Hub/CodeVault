print("Initial List:")
list = ["Bill Gates", "Elon Musk", "Steve Jobs"]


print("\n")
print(list[0])
print(list[1])
print(list[2])

list.remove("Bill Gates")

print("\n")
print("Correction:")
print(list[0])
print(list[1])

print("\n")


list.insert(0, 'Linus Torlvads')
list.insert(2, 'Davodev')
list.append('ThePrimeAgen')
print(list)


print("Sorry I can't invite you ", list.pop())
print("Sorry I can't invite you ", list.pop())
print("Sorry I can't invite you ", list.pop())


print("\n")
print("using del")
del list[1]
del list[0]
print(list)
