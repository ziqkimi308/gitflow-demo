VERSION = "0.1.1"

def greet(name):
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")
    return f"Hello, {name}! Welcome."

def farewell(name):
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")
    return f"Goodbye, {name}! See you soon."

def get_version():
    return VERSION

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
    print(f"Version: {get_version()}")