import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import greet, farewell, get_version

def test_greet():
    assert greet("Alice") == "Hello, Alice! Welcome."

def test_farewell():
    assert farewell("Alice") == "Goodbye, Alice! See you soon."

def test_get_version():
    assert get_version() == "0.1.0"