import io
import sys
import main

def test_anchoLargoTerminal_ancho():
    valor = main.anchoLargoTerminal('ancho')
    assert isinstance(valor, int)
    assert valor in [70, 90, 100]

def test_anchoLargoTerminal_bordes():
    valor = main.anchoLargoTerminal('bordes')
    assert isinstance(valor, int)
    assert valor > 0

def test_formatearOpciones_basico():
    texto = "A - Caminar B - Correr C - Saltar"
    resultado = main.formatearOpciones(texto)
    assert isinstance(resultado, str)
    assert "A -" in resultado and "B -" in resultado and "C -" in resultado


def test_imprimirSeparador():
    resultado = main.imprimirSeparador()
    assert resultado is None
