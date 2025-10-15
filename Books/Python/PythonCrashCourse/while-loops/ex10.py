dream_vacation = []

prompt = "If you could visit one place in the world, where would you go? "
prompt += 'Type "quit" to end the program. '

while True:
    place = input(prompt)
    if place == 'quit':
        break
    else:
        dream_vacation.append(place)
        print(f'I would love to go to {place.title()}!')

print('\nYour dream vacation places are:')
for p in dream_vacation:
    print(f'- {p.title()}')    