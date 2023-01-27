""" Tests for entry package """
import pytest
from main.entry import my_sum

@pytest.mark.parametrize("var_x, var_y, result",
    ([1, 2, 3],))
def test_my_sum(var_x: int, var_y: int, result: int):
    """ tets my_sum function """
    assert my_sum(var_x, var_y) == result
