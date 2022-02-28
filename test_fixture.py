import pytest 

@pytest.fixture
def numbers():
    a = 10
    b = 20 
    c = 25
    return [a,b,c]

def test_method1(numbers):
    x = 15

    assert numbers[0] == x

def test_method2(numbers):
    x = 20
    assert numbers[1] == x

def test_method3(numbers):
    x = 25
    assert numbers[2] == x