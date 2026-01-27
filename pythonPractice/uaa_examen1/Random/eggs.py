colors = ['R', 'O', 'Y', 'G', 'R', 'B', 'I', 'V']
n = int(input())
c = 0

for color in colors:
    if n != c:
        print(color, end='')
    else:
        break

