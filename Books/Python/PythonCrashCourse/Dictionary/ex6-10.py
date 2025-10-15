friends_numbers = {
        "Alex" : [13, 14], 
        "Andre": [10,11], 
        "Jaz":[7,8]
}

print("Favourite numbers")
for name, numbers in friends_numbers.items():
    print(f"{name}'s favourite numbers are:", end=" ")
    for number in numbers:
        print(f"{number}", end=" ")
    print() 
