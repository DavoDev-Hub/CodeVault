sandwich_orders = ['tuna', 'chicken', 'beef', 'pastrami', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

print('Sandwich orders:')
for i in sandwich_orders:
    print(i)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current = sandwich_orders.pop()
    finished_sandwiches.append(current)

print('\n')
print("We don't have more pastrami")
print('Finished Sandwiches: ')
for f in finished_sandwiches:
    print(f)
