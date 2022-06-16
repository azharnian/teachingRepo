from random import randint

questions = [
"as hard as rock, but it melt in hot",
"worth more after it's broken",
"it has teeth, but cannot chew"
]

answers = [
"ice cube",
"egg",
"comb"
]

play = True
player = None
baloons = 7

number = randint(0,2)

while play:
	print(f"\n{questions[number]}")
	print("Left baloons = ", baloons)
	player = input("Answers : ").lower()

	if player == answers[number]:
		print("You Win...")
		play = False
	else:
		print("Wrong...")
		baloons -= 1
	if baloons == 0:
		print("Hangman...!!!")
		play = False
