from pathlib import Path

path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/users.txt')

content = ''

while True:
    name = input('Name: ')
    if name == '':
        break
    content += name + '\n'

path.write_text(content)



''' Mi solucion
from pathlib import Path

path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/users.txt')

content = ''
name = input('Name: ')
content = name + '\n'


while name != '':
    name = input('Name: ')
    content += name + '\n'

text = path.write_text(content)
'''