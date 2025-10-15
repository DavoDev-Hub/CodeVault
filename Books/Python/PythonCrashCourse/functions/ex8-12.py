def make_sandwitch(*sandwitches):
    print("Making a sandwitch with following ingredients: ")
    for sandiwtch in sandwitches:
        print(f'- {sandiwtch}')

make_sandwitch('Bread')
make_sandwitch('Bread', 'Onion', 'Lettuce', 'Chicken')