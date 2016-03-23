#One Away
#time complexity is O(n) cause while loop 
def oneAway(s1,s2):
	if len(s1)<len(s2):
		s1,s2 = s2,s1
	if abs(len(s1)-len(s2))>1:
		return False
	else:
		i,j = 0,0
	        check = False
	        while i<len(s1) and j<len(s2):
			if s1[i] != s2[j]:
				if check:
					return False
			        check = True
			        if len(s1) == len(s2):
					j += 1
			        i+=1
		        else:
				i+=1
			        j+=1
	return True

def main():
	s1 = 'pale'
	s2= 'bale'
	s3 = 'pales'
	s4 = 'palesss'
	a=oneAway(s2,s1)
	b=oneAway(s1,s3)
	c=oneAway(s2,s3)
	d = oneAway(s1,s4)
	print a,b,c,d

if __name__ == '__main__':
	main()
