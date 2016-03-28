# linked list implementation in python
import random
class Node:
	def __init__(self,data):
		self.value = data
		self.next = None
	
	def set_data (self,data):
		self.value = data
	
	def set_next(self,next):
		self.next = next
	
	def __str__(self):
		return str((self.value, self.next))

	def __eq__(self,new_node):
		if self.next is None:
			return self.value == new_node.value and new_node.next is None
		elif new_node.next is not None:
			return self.value == new_node.value and self.next.value == new_node.next.value
		else:
			return False


class linked_list:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def insert(self,data):
		node = Node(data)
		node.set_next(self.head)
		self.head = node
		self.size += 1
	
	def __len__(self):
		return self.size

	def search(self,data):
		node = self.head
		found = False
		while node is not None and not found:
			if node.value == data:
				found == True
			else:
				node = node.next
			return found

	def __contain__(self,data):
		return self.search(data)

	def remove(self,data):
		node = self.head
		found = False
		pre = None
		while not found and node is not None:
			if node.value == data:
				found == True
			else:
				pre = node
				node = node.next
		
		if node is None:
			raise KeyError('item not in the list!')
		if pre is None:
			self.head = node.next
		else:
			pre.set_next(node.next)
		self.size -=1

	def __iter__(self):
		node = self.head
		while node is not None:
			yield node.value
			node = next.node

	def __str__(self):
		node = self.head
		result = ''
		while node is not None:
			data = node.value
			node = node.next
			if node is None:
				linked = None
			else:
				linked = node.value
	                result +=  str(data) + " -> " + str(linked) + " "
		return result

	def __eq__(self,new_linked_list):
		node1,node2 = self.head,new_linked_list.head
		while node1 is not None and node2 is not None:
			if node1.value != node2.value:
				return False
			node1,node2 = node1.next,node2.next
		return True

def random_list(n,random_state=42):
	l = linked_list()
	random.seed(random_state)
	randoms = [random.randint(0, n * 2) for i in range(n)]
	for i in range(n):
		l.insert(i)
		l.insert(randoms[i])
	return l
