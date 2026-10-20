import pytest

from calculadora import calcular_iva, precio_con_descuento, precio_final


def test_descuento_10_por_ciento():
    assert precio_con_descuento(100, 10) == 90


def test_descuento_cero():
    assert precio_con_descuento(250, 0) == 250


def test_descuento_completo():
    assert precio_con_descuento(80, 100) == 0


def test_descuento_con_decimales():
    assert precio_con_descuento(199.99, 15) == 169.99


def test_descuento_invalido():
    with pytest.raises(ValueError):
        precio_con_descuento(100, 120)


def test_precio_negativo():
    with pytest.raises(ValueError):
        precio_con_descuento(-50, 10)


def test_iva_16():
    assert calcular_iva(100) == 16


def test_iva_otra_tasa():
    assert calcular_iva(200, 8) == 16


def test_precio_final_sin_descuento():
    assert precio_final(100) == 116


def test_precio_final_con_descuento():
    assert precio_final(100, 10) == 104.4
