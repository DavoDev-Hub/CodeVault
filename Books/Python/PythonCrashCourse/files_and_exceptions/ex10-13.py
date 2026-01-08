from pathlib import Path
import json

def get_stored_data(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        data = json.loads(contents)
        return data
    else:
        return None

def get_new_data(path):
    data = {}
    username = input("What is yout name? ")
    age = input("What's your age? ")

    data["username"] = username
    data["age"] = age

    contents = json.dumps(data)
    path.write_text(contents)
    return contents

def greet_user():
    """ Greet the user by name """
    path = Path('Books/Python/PythonCrashCourse/files_and_exceptions/  .json')
    data = get_stored_data(path)
    if data:
        print(f"Welcome back, {data}")
    else:
        data = get_new_data(path)
        print(f"We'll remember you when you come back, {data}!")

greet_user()