cities = {
    'Kioto': {
        'country': 'Japan',
        'population': 1475000,
        'fact': 'It was the capital of Japan for over one thousand years.',
    },
    'Barcelona': {
        'country': 'Spain',
        'population': 5585550,
        'fact': 'It is known for its art and architecture.',
    },
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'It is known as "The Big Apple".',
    },
}


for city, descriptions in cities.items():
    print(f'{city}: ')
    country = descriptions['country']
    population = descriptions['population']
    fact = descriptions['fact']
    
    print(f'country: {country}')
    print(f'population: {population}')
    print(f'fact: {fact}')
    print('\n')