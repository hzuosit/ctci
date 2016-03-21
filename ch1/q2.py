#Given two string, check permutation 
#Sort and compare solution
class check:
	def checkPermu(self,s1,s2):
		if sorted(s1) == sorted(s2):
			print s1+' is permutation of '+s2
		else:
			print s1 +' is not a permutation of '+s2
# use dictionary to check the permutation
	def permuDic(self,s1,s2):
		d = {}
		for w in s1:
			if d[w] != 0:
				d[w]+=1
			else:

		

def main():
		s1 = 'abcdefg'
		s2 = 'fgcdbae'
		s3 = 'sadfasdfasdfa'
		c = check()
		c.checkPermu(s1,s2)
		c.checkPermu(s2,s3)
if __name__=='__main__':
		main()
