class Room:
    def __init__(self, genre, capacity):
        
        self.genre = genre
        self.capacity = 4
        self.guests = []
        self.songs = []

    def check_in(self, guest):
        self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)
