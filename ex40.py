class song(object):
	def __init__(self, lyrics, another_lyrics):
		self.lyrics = lyrics
		self.another_lyrics = another_lyrics

	
	def sing_me_song(self):
		for line in self.lyrics:
			print line

	def sing_me_another_song(self):
		print self.another_lyrics

happy_bday = song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"],"Theis song is for you")	


bulls_on_parade = song(["They rally around tha family",
                        "With pockets full of shells"],"Theis song is for you")


happy_bday.sing_me_song()
happy_bday.sing_me_another_song()

bulls_on_parade.sing_me_song()        

