import pytest
from code.__init__ import inc

def test_answer():
    assert inc(3) == 4
