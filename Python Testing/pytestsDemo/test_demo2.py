import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi","Test failed because string do not match"


def test_Secondcreditcard():
    a = 4
    b = 6
    assert a+2 == 6,"Addition do not match"


