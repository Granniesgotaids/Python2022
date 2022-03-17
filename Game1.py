from adventurelib import *

@when("drink juice")
def juice():
	print("You die")
@when("shoot rabbit")
def shoot_mitchell():
	say("""You shoot the rabbit and he explodes""")
@when("drive")
@when("drive home")
@when("crash in a ditch")
def crash():
	say("""You crash into a ditch and die,
	 congratulations for completting this game""")
def main():
	start()

if __name__ == '__main__':
	main()