import sys


sys.path.append('C:\\Users\\User\\Desktop\\Univ Lille\\Refresher in Computer Science\\Part 2 Python for the braves\\firstpoetryproj\\PythonPoetryproj\\firstpoetryproj')

import pythonpro

def test_is_even():
    assert pythonpro.is_even(2) == True
    assert pythonpro.is_even(5) == False
    assert pythonpro.is_even(0) == True