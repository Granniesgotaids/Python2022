from adventurelib import *
#I suppose this is my game or something
Room.items = Bag()

#Rooms
start_room = Room("""You are walking down the road and you fall down a hidden trapdoor, a swinging axe narrowly misses your head and you see a note that
	reads "Game on".""")

room_1 = Room("""You see an empty, damp, wasteful room. It has no windows
	and mold on the ceiling. There is a hammer hanging by a nail on the wall
	""")

knarly_room = Room("""This room appears to be an old kitchen, windows are 
	boarded up and the place is dull and aging. The counter is made of old
	dry wood and on top is a plugged in microwave that smells like an 
	electrical fault. There is a dodgy looking burger and an unopened beer.
	A slide is visible from an opening in the wall and the door is welded shut.
	""")

slide = Room("""You go down a rusty metal slide, without dying somehow.""")

dog_room = Room("""A nasty looking dog with sharp teeth appears and looks pretty dangerous. 	
You spot a brick on the ground, could cause some damage""")

key_room = Room("""You stand in what looks like an old bedroom, very dirty and run down.
A bright shiny key stands out from the run down, dirty place""")

cuboard_room = Room("""A glum room, as they all seem to be. A locked cabinet
is at the end of the room, Looks like it needs a key""")

grandma_room = Room("""An angry looking grandma with a crow bar is approaching,
Fight with whatever you can!""")

freedome = Room("""A locked door to the outside, I'm pretty sure grandma's key
would unlock that door""")


def main():
		start()

if __name__ == '__main__':
		main()