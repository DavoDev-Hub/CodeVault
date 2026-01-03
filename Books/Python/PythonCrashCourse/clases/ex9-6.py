class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant: {self.restaurant_name}')
        print(f'The cuisine type: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'The {self.restaurant_name} is now OPEN!!!')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print(f'Flavors available at {self.restaurant_name}:')
        for flavor in self.flavors:
            print(f'- {flavor}')

my_ice_cream_stand = IceCreamStand('Sweet Treats')
my_ice_cream_stand.add_flavor('Vanilla')
my_ice_cream_stand.add_flavor('Chocolate')
my_ice_cream_stand.add_flavor('Strawberry')
my_ice_cream_stand.describe_restaurant()