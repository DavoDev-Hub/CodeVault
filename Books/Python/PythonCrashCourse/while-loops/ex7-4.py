toppings = []
ask = 'Writte the toppings that you whant on your pizza'
ask += 'Writte "quit" if you want to quit the programm:'

while True:
    topping = input(ask)
    if topping == 'quit':
        print('Thank you, This will be your pizza: ')
        for t in toppings:
            print(t)
        break
    else:
        toppings.append(topping)
        print(f'Adding {topping} to your pizza')