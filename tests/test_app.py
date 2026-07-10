import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import greet, farewell

def test_greet():
    assert greet("Alice") == "Hello, Alice!"

def test_farewell():
    assert farewell("Alice") == "Goodbye, Alice!"