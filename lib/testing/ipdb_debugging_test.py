# lib/testing/ipdb_debugging_test.py

from ipdb_debugging import plus_two

def test_adds_two():
    '''adds_two() adds 2 to input arg and returns sum.'''
    assert plus_two(3) == 5
