import unittest

from classes.room import *
from classes.song import *
from classes.guest import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Rock", 4)
        self.room2 = Room("Pop", 6)

        self.song1 = Song("Oasis", "Wonderwall")
        self.song2 = Song("Blur", "Song 2")
        self.song3 = Song("Killers", "Mr Brightside")
        self.song4 = Song("Abba", "Mamma Mia")

        self.guest1 = Guest("Alex", 10.00, self.song1)
        self.guest2 = Guest("Mark", 12.00, self.song2)
        self.guest3 = Guest("Joe", 15.00, ("Killers", "Mr Brightside"))
        self.guest4 = Guest("Jen", 18.00, ("Abba", "Mamma Mia"))
        self.guest5 = Guest("Liz", 20.00, ("Oasis", "Wonderwall"))
        self.guest6 = Guest("Emma", 8.00, ("Abba", "Mamma Mia"))
        

    def test_room_can__check_in_guest(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_room_can__check_out_guest(self):
        self.room1.check_in(self.guest1)
        self.room1.check_out(self.guest1)
        self.assertEqual(0, len(self.room1.guests))
    
    def test_add_song_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.playlist))

    def test_entry_allowed(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        self.room1.check_in(self.guest4)
        self.assertEqual("Welcome to Karaoke", self.room1.entry(self.guest4))

    def test_entry_denied_room_full(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        self.room1.check_in(self.guest4)
        self.room1.check_in(self.guest5)
        self.assertEqual("Room is full", self.room1.entry(self.guest5))
    

    def test_entry_denied_card_declined(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest6)
        self.assertEqual("Card declined", self.room1.entry(self.guest6))
    
    def test_room_has_fav_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual("Wohoo!", self.room1.playlist_reaction(self.guest1))

    def test_room_doesnt_have_fav_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual("Oh no, Oh no", self.room1.playlist_reaction(self.guest2))

       





    

    


