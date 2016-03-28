# Remove Dups

from linked_list import *
#The first approach use a buffer and it run in O(n) time
def removeDups(ll):
	if ll.head is None:
		return "Please input a valid linked list."

	node = ll.head
	container = [node.value]
	while node is not None:
		pre = node
		node = node.next
		if node is not None:
			if node.value not in container:
				container.append(node.value)
				
			else:
				#point to the next one
				pre.next = node.next
				node = pre
	return ll

def rd_no_buffer(ll):
# this function will work in O(N*N) time, without using a buffer. 
	if ll.head is None:
		return 'Please input a valid linked list.'
	c = ll.head
	r = c
	while c is not None:
		while r.next is not None:
			if c.value == r.next.value:
				r.next = r.next.next
			else:
				r = r.next
	        c = c.next
	return ll

def main():
	l = random_list(15)
	print l.__str__()
	print '\n'
	print removeDups(l)
	print '\n'
	print rd_no_buffer(l)

if __name__ =='__main__':
	main()
			

