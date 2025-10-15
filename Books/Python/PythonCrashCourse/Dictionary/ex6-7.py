my_friend = {
    "first_name" : "Linus", 
    "last_name" : "Torvalds",
    "city" : "Finlandia"
}


my_enemy = {
    "first_name" : "Steve", 
    "last_name" : "Jobs",
    "city" : "San Francisco"
}

my_god = {
    "first_name" : "Terry", 
    "last_name" : "Davis",
    "city" : "Wisconsin"
}

people = [my_friend, my_enemy, my_god]


for person in people:
    print(f"\nHere's what I know about {person['first_name'].title()}:")
    for key, value in person.items():
        print(f"{key.title()}: {value.title()}")