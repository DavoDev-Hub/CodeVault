sandwich_orders = ['tuna', 'chicken', 'beef', 'pastrami', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f'{current} is finished')
    finished_sandwiches.append(current)

print('\n')
print('Finished Sandwiches')
for f in finished_sandwiches:
    print(f)