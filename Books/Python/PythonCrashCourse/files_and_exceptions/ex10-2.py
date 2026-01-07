from pathlib import Path

path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
result = ''

for line in lines:
    result = line.replace('Python', 'C')
    print(result)