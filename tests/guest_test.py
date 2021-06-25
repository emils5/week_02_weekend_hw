import unittest

from classes.guest import *
from classes.song import *



class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Alex", 10.00, ("Oasis", "Wonderwall"))
        self.guest2 = Guest("Mark", 12.00, ("Blur", "Song 2"))
        self.guest3 = Guest("Joe", 15.00, ("Killers", "Mr Brightside"))
        self.guest4 = Guest("Jen", 18.00, ("Oasis", "Wonderwall"))
        self.guest5 = Guest("Liz", 20.00,("Oasis", "Wonderwall"))

    def test_guest_has_name(self):
        self.assertEqual("Alex", self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(10.00, self.guest1.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual(("Oasis", "Wonderwall"), self.guest1.fav_song)

