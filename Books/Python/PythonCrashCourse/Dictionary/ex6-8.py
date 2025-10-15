dog = {
    'name': 'willie',
    'type': 'terrier',
    'owner': 'linus',
}

cat = {
    'name': 'kitty',
    'type': 'siamese',
    'owner': 'steve',
}

duck = {
    'name': 'howard',
    'type': 'mallard',
    'owner': 'terry',
}

pets = [dog, cat, duck]

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")