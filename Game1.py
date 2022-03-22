from adventurelib import *
carpark = Room("""You are in an empty parking lot, seems a bit dodgy
but mostly alright. The lights glow dimmly""")
@when("drink juice")
def juice():
	print("You die")
@when("shoot rabbit")
def shoot_bunny():
	say("""You shoot the rabbit and he explodes""")

@when("drive")
@when("drive home")
@when("crash in a ditch")
def crash():
	say("""You crash into a ditch and die,
	 congratulations for completting this game""")
def elevator():
	global current_room
current_room
#check if door can be opened
if current_room is not carppark:
	say("No elevator to enter")
def main():
	start()

if __name__ == '__main__':
	main()