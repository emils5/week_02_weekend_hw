class Room:
    def __init__(self, genre, capacity):
        
        self.genre = genre
        self.capacity = capacity
        self.guests = []
        self.playlist = []
        self.entry_fee = 10.00

    def check_in(self, guest):
        self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.playlist.append(song)

    def entry(self, guest):
        if len(self.guests) <= self.capacity and guest.wallet >= self.entry_fee:
            self.check_in(guest)
            return "Welcome to Karaoke"
        elif len(self.guests) <= self.capacity and guest.wallet < self.entry_fee:
            return "Card declined"
        else: 
            return "Room is full"

    def playlist_reaction(self, guest):
        if  guest.fav_song in self.playlist:
            return "Wohoo!"
        else: 
            return "Oh no, Oh no"
        
