usernames = ['Bill', 'Linus', 'Davo', 'John', 'Admin']


if usernames:
    for username in usernames:
        if username == 'Admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username},  thank you for loggin in again')
else:
    print('We need to found  more users')