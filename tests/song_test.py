import unittest

from classes.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Oasis", "Wonderwall")
        self.song2 = Song("Blur", "Song 2")
        self.song3 = Song("Killers", "Mr Brightside")
        self.song4 = Song("Abba", "Mamma Mia")

    def test_song_has_artist(self):
        self.assertEqual("Oasis", self.song1.artist)
    
    def test_song_has_name(self):
        self.assertEqual("Wonderwall", self.song1.name)

