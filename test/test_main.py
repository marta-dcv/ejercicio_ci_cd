from src.main import elevar
from src.main import to_upper

def test_elevar_basico():
    assert elevar(2,3) == 8


def test_to_upper():
    assert to_upper("hola") == "HOLA"