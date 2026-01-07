from pathlib import Path

path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/guest.txt')

name = input("What's your name?: ")
contents = path.write_text(f"Hi {name} you have written to a txt from python")