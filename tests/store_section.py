import pytest

pytestmark = [pytest.mark.positive_test]
@pytest.mark.positive_test
def test_mult():
    assert 3*5 == 15

pytestmark = [pytest.mark.positive_test]
@pytest.mark.positive_test
def test_sum():
    assert 3+5 == 5

