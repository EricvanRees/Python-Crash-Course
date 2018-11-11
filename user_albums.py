'''
Start with your program from Exercise 8-7. Write a while loop that
allows users to enter an album's artist and title. Once you have that
information, call make_album() with the user's input and print the
dictionary that's created. Be sure to include a quit value in the while loop.
'''

def make_album(artist, album, tracks=''):
	album_made = {'artist': artist, 'album': album}
	if tracks:
		album_made['tracks'] = tracks	 
	return album_made
	
while True:
	print("please enter album's artist and title: ")
	print("enter 'q' at any time to quit.")
	artist = input("enter artist: ")
	if artist == 'q':
		break
		
	album = input("enter album: ")
	if album == 'q':
		break
		
	album = make_album(artist, album)
	print(album)
	
