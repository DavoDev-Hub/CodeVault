class User:
    def __init__(self, first_name, last_name, age, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'Name: {self.first_name} {self.last_name}, {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name} good day!!!')
    
    def increment_login_attempts(self, attempts=1):
        self.login_attempts += attempts
        print('Attempts: ', self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Attempts has already reset')
        print(f'Attempts: {self.login_attempts}')




user = User('Juan Pablo', 'Jimenez', '21')
user.describe_user()
user.greet_user()
user.increment_login_attempts(10)
user.increment_login_attempts(2)

print('\n')

user = User('Negrox', 'Rodriguez', '22')
user.describe_user()
user.greet_user()
user.increment_login_attempts(15)
user.reset_login_attempts()