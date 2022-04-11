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

freedom = Room("""You are free!""")

#Directions
start_room.north = room_1
start_room.south = dog_room
room_1.east = knarly_room
dog_room.east = key_room
knarly_room.south = key_room
key_room.south = cuboard_room
cuboard_room.south = grandma_room
grandma_room.west = freedom

#Define items
Item.description = "" #This adds a blank description to each item

brick = Item("brick")
brick.description = "the brick is heavy and fairly strong, quite destructive when used in that manner"

hammer = Item("hammer")
hammer.description = "the hammer is rusty but still quite strong"

burger = Item("burger")
burger.description = "Edible, I think? Looks a bit dodgy"

beer = Item("beer")
beer.description = "unopened perfectly good beer, wouldve been better in a fridge"

key = Item("key")
key.description = "should unlock something, it is a key after all"

bow = Item("bow")
bow.description = "a powerful compound bow with several arrows attached to the side"

#add items to bags
dog_room.items.add(brick)
room_1.items.add(hammer)
knarly_room.items.add(burger)
knarly_room.items.add(beer)
key_room.items.add(key)
cuboard_room.items.add(bow)

#defines variables
current_room = start_room


@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
		print(current_room.exits())
	else:
		print("You can't go that way")


@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0: #if there are some items in the room
		print("You also see:")
		for item in current_room.items:
			print(item)#print out each item

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:#check if item is in room
		t = current_room.items.take(item)#take it out of room
		inventory.add(t)#put into inventory
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")#otherwise tell user there is no item

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")




def main():
		start()

if __name__ == '__main__':
		main()