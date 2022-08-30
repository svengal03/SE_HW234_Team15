import pytest
from code import square

def test_zero():
    assert square(0) == 0
    
def test_two():
    assert square(2) == 4

def test_three():
    assert square(3) == 9
