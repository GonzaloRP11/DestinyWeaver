from main import cargarDatos, obtenerMapa, validarNombre




def test_cargarDatos():
    datos = cargarDatos("historias.json")
    assert isinstance(datos, dict)
    assert "historias" in datos



def test_validarNombre_valido():
    assert validarNombre("Nicolas") == True

def test_validarNombre_corto():
    assert validarNombre("ab") == False

def test_validarNombre_largo():
    assert validarNombre("abcdefghijklmnop") == False

def test_validarNombre_con_numeros():
    assert validarNombre("nico123") == False



def test_obtenerMapa_aventura():
    matriz = obtenerMapa("aventura_clasica")
    assert matriz == [
        ["bosque", "sendero"],
        ["cueva"]
    ]


def test_obtenerMapa_estacion():
    matriz = obtenerMapa("estacion_espacial")
    assert matriz == [
        ["laboratorio", "pasillo"],
        ["sala"]
    ]


def test_obtenerMapa_mazmorra():
    matriz = obtenerMapa("mazmorra_magica")
    assert matriz == [
        ["celda", "pasillo"],
        ["pared", "camara"]
    ]


def test_obtenerMapa_invalido():
    matriz = obtenerMapa("no_existe")
    assert matriz is None
