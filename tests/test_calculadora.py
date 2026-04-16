import pytest
from calculadora.calculadora import calculadora

calc = calculadora()

def test_sumar():
    assert calc.sumar(2, 3) == 5
    assert calc.sumar(-1, 1) == 0
    assert calc.sumar(0, 0) == 0

def test_restar():
    assert calc.restar(10, 4) == 6
    assert calc.restar(0, 5) == -5

def test_multiplicar():
    assert calc.multiplicar(3, 5) == 15
    assert calc.multiplicar(0, 100) == 0

def test_dividir():
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(9, 3) == 3

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        calc.dividir(5, 0)

def test_potencia():
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1


def test_fallo_intencional():
    assert sumar(2, 2) == 2