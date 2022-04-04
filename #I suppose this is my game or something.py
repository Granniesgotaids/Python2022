#I suppose this is my game or something
from adventurelib import *

Room.items = Bag()

#Rooms
start = Room("""You are walking down the road and you fall down a hidden
	trapdoor, a swinging axe narrowly misses your head and you see a note that
	reads "Game on".""")

room_1 = Room("""You see an empty, damp, wasteful room. It has no windows
	and mold on the ceiling. There is a hammer hanging by a nail on the wall""")

knarly_room = Room("""This room appears to be an old kitchen, windows are 
	boarded up and the place is dull and aging. The counter is made of old
	dry wood and on top is a plugged in microwave that smells like an 
	electrical fault. There is a dodgy looking burger and an unopened beer.
	A slide is visible from an opening in the wall and the door is welded shut.""")








def main():
	start()

if __name__ == '__main__':
	main()