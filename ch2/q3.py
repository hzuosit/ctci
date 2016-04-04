#Delete Middle Node
from linked_list import *
def delete_middle_node(n,ll):
	node = ll.head
	while node.next is not None:
		if node.next.value == n:
			node = node.next.next
		else:
			node = node.next
	        print '->' + str(node.value) 

def main():
	n = input('Enter the node value need to be deleted:'+ '\n')
	ll = random_list(10)
	print ll
	print delete_middle_node(n,ll)
			
if __name__ == '__main__':
	main()
	
