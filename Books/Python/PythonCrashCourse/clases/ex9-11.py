from user import User, Admin, privileges
admin_user = Admin('Admin', 'User', '30')
admin_user.describe_user()
privilege_instance = privileges(['can add post', 'can delete post', 'can ban user'])
privilege_instance.show_privileges()