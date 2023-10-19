import pytest


from firstpoetryproj import pythonpro


def test_is_even():
    assert pythonpro.is_even(2) == True
    assert pythonpro.is_even(5) == False
    assert pythonpro.is_even(0) == True