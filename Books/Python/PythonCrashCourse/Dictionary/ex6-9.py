favorite_places = {
    'Steve': ['Spain', 'Mexico', 'Japan'],
    'Mark Zuckerberg': ['Italy', 'Greece', 'Turkey'],
    'Bill Gates': ['France', 'Germany', 'Switzerland'],
    'Elon Musk': ['Canada', 'Australia', 'New Zealand'],
}


print("Favourite places")
for name, places in favorite_places.items():
    print(f"{name}'s favourite places are:", end=" ")
    for place in places:
        print(f"{place}", end=" ")
    print() 