def suma(a, b):
    return a + b

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def resta(a, b):
    return a - b

def test_resta():
    assert resta(2, 3) == -1
    assert resta(-1, 1) == -2

def multiplicar(a, b):
    return a * b

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1

def dividir(a, b):
    return a / b

def test_dividir():
    assert dividir(4, 2) == 2
    assert dividir(-1, 1) == -1
