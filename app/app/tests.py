from django.test import TestCase
from app.calc import add, sub


class CalcTests(TestCase):
    def test_add_number(self):
        """ test the two number add together """
        self.assertEqual(add(3, 8), 11)

    def test_sub_number(self):
        """ test the two number sub together """
        self.assertEqual(sub(3, 8), 5)
