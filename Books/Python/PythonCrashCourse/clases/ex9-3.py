class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'Name: {self.first_name} {self.last_name}, {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name} good day!!!')
    

user = User('Juan Pablo', 'Jimenez', '21')

user.describe_user()
user.greet_user()

user = User('Negrox', 'Rodriguez', '22')
user.describe_user()
user.greet_user()