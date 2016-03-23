#Rotate Matrix
#zip() is amazing

def RMatrix(m):
	return zip(*m[::-1])

def main():
	m = [[1,2,3],[4,5,6],[7,8,9]]
	print RMatrix(m)

if __name__ == '__main__':
	main()

