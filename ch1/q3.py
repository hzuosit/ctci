#urlify 
# first method use insertion, however, the insert() time complexity is O(n),thus the for loop here will consume O(n*n), it's low efficiency.
def urlify(s):
	a = s.split()
	l = 2*len(a)-1
	for x in xrange(1,l,2):
		a.insert(x,'%20')
	print  ''.join(a)

#this is best way 
def urlify2(s):
	print  '%020'.join(s.split())

def main():
	s = 'asdf asdf awer add'
	urlify(s)
	k = 'qwe wl di siq so'
	urlify2(k)
if __name__ == "__main__":
	main()

	




