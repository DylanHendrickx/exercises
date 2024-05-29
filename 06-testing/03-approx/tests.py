import pytest
from mystatistics import average


@pytest.mark.parametrize('ns, expected',[
    ([8,4], 6),
    ([0.1,0.1,0.1],0.1),
])
def test_average(ns, expected):
    assert pytest.approx(expected) == average(ns)
