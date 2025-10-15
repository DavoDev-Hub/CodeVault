class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'The restaurant: {self.restaurant_name}')
        print(f'The cuisine type: {self.cuisine_type}')
        print(f'Number of customers served: {self.number_served}')

    def open_restaurant(self):
        print(f'The {self.restaurant_name} is now OPEN!!!')

    def set_number_served(self, number):
        self.number_served = number
        print(f'Number of customers served updated to: {self.number_served}')

    def increment_number_served(self, increment=1):
        self.number_served += increment
        print(f'Number of customers served incremented by {increment}. Total: {self.number_served}')

my_favorite_restaurant = Restaurant('Lagisob', 'Italian')
my_favorite_restaurant.describe_restaurant()
my_favorite_restaurant.open_restaurant()
my_favorite_restaurant.set_number_served(20)
my_favorite_restaurant.describe_restaurant()
my_favorite_restaurant.increment_number_served(5)

my_favorite_restaurant = Restaurant('Pasta Palace', 'Italian')
my_favorite_restaurant.describe_restaurant()
my_favorite_restaurant.open_restaurant()
my_favorite_restaurant.set_number_served(20)
my_favorite_restaurant.increment_number_served(5)