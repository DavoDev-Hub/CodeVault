from pathlib import Path

path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)