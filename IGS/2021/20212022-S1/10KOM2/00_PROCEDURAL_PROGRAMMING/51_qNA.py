
def get_questions():

	return [
		["What color is the daytime sky on a clear day? ", "blue"], #0 -> [0][0], [0][1]
		["What is the answer to life, the universe and everything? ", "42"], #1
		["What is a three letter word for mouse trap? ", "cat"], #2
		["",""]
	]

def check_question(row):
	q = row[0]
	a = row[1]

	user_ans = input(q)
	if user_ans == a:
		print("Correct!")
		return True
	else:
		print(f"Incorrect!, correct was : {a}")
		return False

def main(questionBank):

	if len(questionBank) == 0:
		print("No questions were given.")
		return
	
	index = 0
	right = 0
	while index < len(questionBank):
		# print(questionBank[index])

		if check_question(questionBank[index]):
			right += 1

		index += 1
	print(f"your score is {right/len(questionBank)*100}")	


main(get_questions())