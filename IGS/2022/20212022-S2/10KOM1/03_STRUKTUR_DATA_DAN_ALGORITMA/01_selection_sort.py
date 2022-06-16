

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


daftar_angka = [10, 4, 10, 3, 1, 0, 8, 9]

print(selection_sort(daftar_angka))

#selection_sort(list, "asc")
#punya fitur asc dan desc, dan punya default asc