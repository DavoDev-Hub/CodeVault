from pathlib import Path
import json

path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/username.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f'I know your favorite number ', number )
else:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
