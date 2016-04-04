#Return Kth to Last
from linked_list import *

def k_tolast(k,ll):
	node = ll.head
	s = ll.size
	for i in range(s-k):
		if node is not None:
			node = node.next
		else:
			return
	return node


def main():
	k = 5
	ll = random_list(20)
	print ll
	print  k_tolast(k,ll)


if __name__ == '__main__':
	main()


	
	
