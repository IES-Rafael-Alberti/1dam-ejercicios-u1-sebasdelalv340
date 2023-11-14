import pytest

from src.ej1_01_def import obtenerSaludo

@pytest.mark.parametrize(
    "input_nombre, expected",
    [
      (sebas, sebas),
      (Sebas, Sebas),
    ]
)