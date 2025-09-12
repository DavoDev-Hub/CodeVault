'''
green 5
yellow 10
red 15
'''
alien_color = 'yellow'
points = 0

if alien_color == 'green':
    points += 5
    print(f'You earned 5 point for shooting the green alien, your points: {points}')
elif alien_color == 'yellow':
    points += 10
    print(f'You earned 10 point for shooting the yellow alien, your points: {points}')
else:
    points += 15
    print(f'You earned 15 point for shooting the red alien, your points: {points}')
