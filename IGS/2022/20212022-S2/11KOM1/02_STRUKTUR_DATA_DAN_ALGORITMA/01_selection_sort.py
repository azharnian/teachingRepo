

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


numbers = [10, 3, 4, 1, 0, 1, 2, 9]

print(selection_sort(numbers))

#buat selection sort yg punya fitur
# asc, desc, default asc - > selection_sort(list)