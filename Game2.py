from adventurelib import *
space = Room("""You are drifting in space, kinda boring ngl.
	You see a slate-blue spaceship sitting completly silently
	to your left its airlock open and waiting.""")

spaceship = Room("""The bridge of the spaceship is shiny
	and white, with thousands of small, red, blinking lights.
	""")

current_room = space

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	#check if action can be done
	if current_room is not space:
		say("There is no airlock here")
		return
	else:
		current_room = spaceship
		print("""You heave yourself into the spaceship and slam 
			     your hand shut on the button to close the 
	             door.""")
		print(current_room)

hallway = Room("""Hallway""")
quarters = Room("""Hostages held here""")
bridge = Room("""Walk across it lol""")
cargo = Room("""Storing drugs""")

spaceship.east = hallway
spaceship.south = quarters
hallway.east == bridge
hallway.north = cargo

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)

def main():
	start()

if __name__ == '__main__':
	main()
