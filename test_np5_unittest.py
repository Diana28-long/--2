import unittest


class TestInputValidation(unittest.TestCase):

    def test_valid_number(self):
        number = int("10")
        self.assertEqual(number, 10)

    def test_negative_number(self):
        number = int("-7")
        self.assertEqual(number, -7)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            int("hello")


if __name__ == "__main__":
    unittest.main()
