#Zero matrix

def zeroMatrix(x):
	N = len(x)
	M =len(x[0])
	checker  =[]
	for i in range(0,N):
		for j in range(0,M):
			if x[i][j] == 0:
				checker.append((i,j))
	for (a,b) in checker:
		for c in range(0,M):
			x[a][c] =0
		for c in range(0,N):
			x[c][b]=0
	return x

def main():
	x = [[1,0,2,1],[2,1,2,0],[2,3,4,5]]
	print zeroMatrix(x)
if __name__ == '__main__':
	main()
