from pathlib import Path

try:
    path = Path('Books/Python/PythonCrashCours/files_and_exceptions/dogs.txt')
    path2 = Path('Books/Python/PythonCrashCourse/files_and_exceptions/dogs.txt')
    
    content = path.read_text()
    content2 = path2.read_text()
    print('Dogs:\n', content)
    print('Cats:\n', content2)
except FileNotFoundError:
    pass
