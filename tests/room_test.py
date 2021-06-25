import unittest

from classes.room import *
from classes.song import *
from classes.guest import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Rock", 4)
        self.room2 = Room("Pop", 6)
        self.guest1 = Guest("Alex")
        self.guest2 = Guest("Mark")
        self.song1 = Song("Oasis", "Wonderwall")


    def test_room_can__check_in_guest(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_room_can__check_out_guest(self):
        self.room1.check_in(self.guest1)
        self.room1.check_out(self.guest1)
        self.assertEqual(0, len(self.room1.guests))
    
    def test_add_song_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.songs))

    


