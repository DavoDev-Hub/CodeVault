class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'Name: {self.first_name} {self.last_name}, {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name} good day!!!')
    
class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = []

    def add_privilege(self, privilege):
        self.privileges.append(privilege)

    def show_privileges(self):
        print(f'Admin Privileges for {self.first_name}:')
        for privilege in self.privileges:
            print(f'- {privilege}')


class privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print('Admin Privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')

admin_user = Admin('Admin', 'User', '30')
admin_user.describe_user()
privilege_instance = privileges(['can add post', 'can delete post', 'can ban user'])
privilege_instance.show_privileges()