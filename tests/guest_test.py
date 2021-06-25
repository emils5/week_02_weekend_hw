import unittest

from classes.guest import *


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Alex", 10.00)
        self.guest2 = Guest("Mark", 12.00)
        self.guest3 = Guest("Joe", 15.00)
        self.guest4 = Guest("Jen", 18.00)
        self.guest5 = Guest("Liz", 20.00)

    def test_guest_has_name(self):
        self.assertEqual("Alex", self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(10.00, self.guest1.wallet)

