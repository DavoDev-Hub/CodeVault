from pathlib import Path

path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/learning_python.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
lst = []

for line in lines:
    lst.append(line.lstrip())

for l in lst:
    print(l)