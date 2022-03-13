#Exercise 6.3
#1-5
"""
presskey = input("Press any key")
if presskey == "a":
	print("Thanks")
else: 
	print("Thanks")

name = input("Enter your name\n")
age = input("Enter your age\n")
#6-11
movie = input("What is your favourite movie\n")
book = input("Give me a name of a book\n")
adjective = input("What even is an adjective\n")
noun = input("Give me a noun\n")
verb = input("Verb? Whats that?\n")
print(f"Hi {name} I think you should GET OUT")
print(f"You've been wasting oxygen for {age} year(s)")
print(f"Lol, your favourite movie is {movie}? Lmao")
#this doesn't even fall into a catagory (except pissing around lol)
strikes = int(input("How many stikes do you have?"))
if strikes > 2:
	print("Get out mate")
else:
	print("Hmmmmmmm, ok you can stay")
#12-17
agee = int(input("How old are you\n"))
agee = agee + 10
print(f"You will be {agee} in 10 years, you old lol\n")
agee = agee - 10
agee = 2021 - agee
print(f"You were born in {agee}")
apples = int(input("How many apples do you have?\n"))
friends = int(input("How many friends do you have\n"))
if friends == 0:
	print("You sad sack")
else:
	print(f"Each person gets {apples//friends}")
	print(f"You have {apples%friends} left over")
#18-23
"""
pizza = int(input("How many pizzas do u want?\n"))
fatties = int(input("How many peoples are you feeding?\n"))
print(f"Each person gets {pizza//fatties}")
print(f"There will be {pizza%fatties} left\n")
ohgod = pizza//fatties
if ohgod > 5:
	print("Calling the cardiac unit....")
money = int(input("How much money do you have\n"))
tv = int(input("How much does a tv cost\n"))
if tv < 500:
	print("Nahhhhhhhhh")
money = money - tv
print(f"You have ${money} left")
#24-31
tv = tv // 1.2
print(f"If you wait for a 20% off sale the tv will cost {tv}")