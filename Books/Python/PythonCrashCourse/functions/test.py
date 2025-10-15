def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

def car_rent(car):
    print(f'Let me see if I can find you a {car}')

car = input('Type the car you would like to rent: ')
car_rent(car)