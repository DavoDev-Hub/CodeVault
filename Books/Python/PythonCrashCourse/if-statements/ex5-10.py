current_users = ['Bill', 'LINUS', 'Davo', 'John', 'Admin']
current_lower = []

new_users = ['Linus', 'Bill', 'mUSk', 'R2R2']



for current_user in current_users:
    current_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_lower:
        print(f'Enter another  user name, {new_user} is unavailibale')
    else:
        print(f'User name availible {new_user}')