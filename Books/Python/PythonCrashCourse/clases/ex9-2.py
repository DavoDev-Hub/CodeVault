class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant: {self.restaurant_name}')
        print(f'The cuisine type: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'The {self.restaurant_name} is now OPEN!!!')
    

print('\nMy favorite restaurant')
my_favorite_restaurant = Restaurant('Lagisob', 'Italian')
my_favorite_restaurant.describe_restaurant()
my_favorite_restaurant.open_restaurant()

print('\nThe worst restaurant')
my_favorite_restaurant = Restaurant('Mamamia', 'Italian')
my_favorite_restaurant.describe_restaurant()
my_favorite_restaurant.open_restaurant()

print("\nFavorites friend's restaurant")
my_favorite_restaurant = Restaurant('Burgers', 'American')
my_favorite_restaurant.describe_restaurant()
my_favorite_restaurant.open_restaurant()