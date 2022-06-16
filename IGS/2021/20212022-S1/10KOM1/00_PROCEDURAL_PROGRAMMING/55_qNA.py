
def get_questions():

	return [
		["What color is the daytime sky on a clear day? ", "blue"], # [0][0], [0][1]
		["What is the answer to life, the universe and everything? ", "42"], # [1][0]
		["What is a three letter word for mouse trap? ", "cat"]
	]

def check_question(row):
	q = row[0]
	a = row[1]

	user_ans = input(q)
	if a == user_ans:
		print("Correct!")
		return True
	else:
		print("Incorrect!")
		return False

#refactoring -> 10 = 2(5), 20 = 2^2(5)
def run(questions):
	if len(questions) == 0:
		print("No questions were given.")
	else:
		index = 0
		right = 0

		while index < len(questions):
			
			# print(questions[index])

			if check_question(questions[index]):
				right += 1

			index += 1
		print(f"Your score is {right/len(questions) * 100}")	

run(get_questions())