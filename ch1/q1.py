#this is the solution with extra data structures
def isUnique(s):
		if len(s)==len(set(s)):
				print 'is unique'
		else:
				print 'is not unique'

#this is the solution without extra data structures
def merge_sort(l):
		if len(l)<=1:
				return l
		mid = len(l)/2
		left = merge_sort(l[:mid])
		right = merge_sort(l[mid:])
		return merge(left,right)

def merge(left,right):
		if not left:
				return right
		if not right:
				return left
		if left[0]<right[0]:
				return [left[0]]+merge(left[1:],right)
		return [right[0]]+merge(right[1:],left)
def main():
	#	isUnique('adfasdfq')
	l = [32,12,54,67,1,2,3,4]
	print  merge_sort(l)
	
if __name__ == '__main__':
		main()
