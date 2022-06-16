
questions = [
	
	["What color is the daytime sky on a clear day ?", "blue"], # [q, a]-> q[0], q[1]
	["What is the answer to life, the universe and everything?", "42"],
	["What is a three letter word for mouse trap?", "cat"]

	]

index = 0
right = 0

while index < len(questions):

	#list 2 dimensi
	user_ans = input(questions[index][0])
	if user_ans.lower() == questions[index][1]:
		right += 1

	index += 1

score = right/len(questions)*100
if score == int(score):
	score = int(score)
	print(f"Your score is {score}") #integer number
else:
	print(f"Your score is {score:.2f}") #float number


