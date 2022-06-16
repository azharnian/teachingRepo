class Node:

	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = Node()


	def append(self, data):
		new_node = Node(data)
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next
		current_node.next = new_node

	def length(self):
		current_node = self.head
		total = 0
		while current_node.next != None:
			total += 1
			current_node = current_node.next

		return total

	# def remove(self, data):
	# 	pass


	def display(self):
		current_node = self.head
		print("<", end=" ")
		while current_node.next != None:
			current_node = current_node.next
			print(current_node.data, end=" ")
		print(">")


my_linked_list = LinkedList()
my_linked_list.display()
my_linked_list.append(5)
my_linked_list.append(10)
my_linked_list.append(11)
my_linked_list.display()
print(my_linked_list.length())

