from losango import centralizar, linha, intervalo, text, monta_losango


def test_centralizar():
    assert centralizar("0", 5) == "..0.."
    assert centralizar("0", 3) == ".0."


def test_intervalo():
    assert intervalo(0) == (0,)
    assert intervalo(1) == (0, 1, 0)
    assert intervalo(2) == (0, 1, 2, 1, 0)
    assert intervalo(3) == (0, 1, 2, 3, 2, 1, 0)
    assert intervalo(9) == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)


def test_text():
    v = (0,)
    assert text(v) == "0"
    assert text((0, 1, 0)) == "010"


def test_linha():
    assert linha(0, 5) == "..0.."
    assert linha(1, 5) == ".010."
    assert linha(2, 5) == "01210"


def test_losango():
    assert monta_losango(2) == "..0..\n.010.\n01210\n.010.\n..0.."
