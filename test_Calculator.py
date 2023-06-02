import sys
from UserDefinedFunctions import squared

def test_squared():

    assert squared(3) == 9
    assert squared(4) == 16
    assert squared(-3) == 9
    assert squared(-4) == 16
    assert squared(0) == 0

test_squared()
