from pathlib import Path
import json

'''number = input("What's your favorite number? ")
path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/username.json')

contents = json.dumps(number)
path.write_text(contents)
'''

contents = path.read_text()
number = json.loads(contents)
print(f'I know your favorite number is ', number )