import pytest
from src.square_root import SquareRoot


def test_sqrt():
    sq = SquareRoot()
    assert sq.run(4.0) == 2.0

def test_sqrt_negative():
    sq = SquareRoot()
    with pytest.raises(Exception):
        sq.run(-1.0)