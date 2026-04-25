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


