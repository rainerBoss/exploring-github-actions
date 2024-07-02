import pytest
from main import greet

def test_greet():
    name = "rainers"
    assert greet(name) == f"Hello, {name}"