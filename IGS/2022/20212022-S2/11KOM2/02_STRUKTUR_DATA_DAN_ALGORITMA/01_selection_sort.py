
numbers = [5, 3, 6, 2, 10]


def find_greatest(list):
	greatest_val = list[0]
	greatest_index = 0

	for i in range(1, len(list)):
		if list[i] > greatest_val:
			greatest_val = list[i]
			greatest_index = i

	return greatest_index



def selection_sort(list):
	new_list = []

	for i in range(len(list)):
		greatest_index = find_greatest(list)
		new_list.append(list.pop(greatest_index))

	return new_list

print(selection_sort(numbers))
# buatkan selection sort yg punya fitur, asc, desc, dan default asc.
#print(selection_sort(numbers, asc=False))