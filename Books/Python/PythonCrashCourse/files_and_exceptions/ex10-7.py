numbers = []
while True:
    try:
        num = int(input('Give me a number: '))
        numbers.append(num)
    except:
        print('Only numbers')
    
    con = input('Exit? q(quit) / c(continue)')
    if con == 'q':
        break
    else:
        continue

print('The numbers are: ')
for n in numbers:
    print(n)