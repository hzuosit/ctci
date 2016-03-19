#Given two string, check permutation 

#Sort and compare solution
class check:
		def checkPermu(s1,s2):
				if sorted(s1) == sorted(s2):
						print s1+' is permutation of '+s2
				else:
						print s1 +' is not a permutation of '+s2
        
def main():
		s1 = 'abcdefg'
		s2 = 'fgcdbae'
		s3 = 'sadfasdfasdfa'
		c = check()
		c.checkPermu(s1,s2)
if __name__=='__main__':
		main()
