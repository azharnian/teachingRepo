
class Node:

	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = Node()

	def append(self, data):
		new = Node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new

	def display(self): #< 23 34 24 >
		cur = self.head
		print("<", end=" ")
		while cur.next != None:
			cur = cur.next
			print(cur.data, end=" ")
		print(">")

my_list = LinkedList()

my_list.display()
my_list.append(23)
my_list.append(34)
my_list.append(24)
my_list.display()