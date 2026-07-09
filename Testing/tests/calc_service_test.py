import pytest
from Testing.calc_service import CalcService

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (1, 1, 2),
    (-1, -1, -2)
])
def test_sum(a: int, b: int, expected: int):
    res = CalcService.sum(a, b)

    assert res == expected