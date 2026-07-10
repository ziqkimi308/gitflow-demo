VERSION = "0.1.0"

def greet(name):
    return f"Hello, {name}! Welcome."

def farewell(name):
    return f"Goodbye, {name}! See you soon."

def get_version():
    return VERSION

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
    print(f"Version: {get_version()}")