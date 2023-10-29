"""
Module Docstring: This module contains tests for the is_even function in the pythonpro module.
"""

from firstpoetryproj import pythonpro


def test_is_even():
    """Test the is_even function."""
    assert pythonpro.is_even(2) is True
    assert pythonpro.is_even(5) is False
    assert pythonpro.is_even(0) is True
