toppings = []
prompt = 'Writte your age and I will tell you the cost of your ticket:'

while True:
    ticket = int(input(prompt))
    if ticket <= 3: print('Free')
    elif ticket > 3 and ticket <= 12: print('$10')
    else: print('$15')

    quit = input('Continue 1. Yes, 2. No?')
    if quit == 1:
        continue
    else:
        break