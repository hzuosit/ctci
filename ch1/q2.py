#Given two string, check permutation 
#Sort and compare solution
class check:
	def checkPermu(self,s1,s2):
		# sorted() use timsort which time complexity is O(nlogn),space O(n)
		if sorted(s1) == sorted(s2):
			print s1+' is permutation of '+s2
		else:
			print s1 +' is not a permutation of '+s2
# use dictionary to check the permutation which time comlexity is O(n), space O(n),which is better.
	def permuDic(self,s1,s2):
		if len(s1) != len(s2): # don't use set() here, altought time-complexity of set() is average O(1),but len() is                                        # actually O(1) in average and worst case,it's  more stable. 
			print  s1 +' is not a permutation of(dic situ1) '+s2 
			return
		d = {}
		for w in s1:
			if w in d:
				d[w]+=1
			else:
				d[w] =1
		
		for x in s2:
			if d[x] <= 0:
				print  s1 +' is not a permutation of(di situ2) '+s2
				return
			else:
				d[x]-=1
		print s1+' is a permutation of '+s2
		return
def main():
		s1 = 'aabbccdd'
		s2 = 'aaabcccd'
		s3 = 'sadfasdfasdfa'
		s4 = 'ababcdcd'
		c = check()
		c.checkPermu(s1,s2)
		c.checkPermu(s2,s3)
		c.checkPermu(s1,s4)
		d = check()
		d.permuDic(s2,s1)
		d.permuDic(s2,s3)
		d.permuDic(s1,s4)
if __name__=='__main__':
		main()
