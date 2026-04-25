
def test_valid_number():
    number = int("5")
    assert number == 5

def test_negative_number():
    number = int("-3")
    assert number == -3

def test_invalid_input():
    try:
        int("abc")
        assert False
    except ValueError:
        assert True

import pytest

# fixture
@pytest.fixture
def sample_number():
    return 5

def test_with_fixture(sample_number):
    assert sample_number == 5

def test_invalid_input():
    with pytest.raises(ValueError):
        int("abc")

@pytest.mark.skip(reason="Функція ще не реалізована")
def test_skip_example():
    assert int("5") == 5

# parametrize
@pytest.mark.parametrize("value, expected", [
    ("5", 5),
    ("-3", -3),
    ("10", 10)
])
def test_parametrize(value, expected):
    assert int(value) == expected

@pytest.mark.xfail(reason="Очікувана помилка")
def test_expected_fail():
    assert int("5") == 10

def test_fail_example():
    assert int("5") == 100
