VERSION = "0.1.0"

def greet(name):
    return f"Hi there, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def get_version():
    return VERSION

if __name__ == "__main__":
    print(greet("World"))