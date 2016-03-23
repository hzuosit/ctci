#check palindrome permutation 
def string_Dic(s):
	d = {}
	for char in s:
		if char in d:
			d[char] +=1
		else:
			d[char] = 1
        return d

def check_odd(num):	
	if num % 2 == 1:
		return True
	else:
		return False

def checkPp(s):
	counter = 0
	d = string_Dic(''.join(s.split()).lower())
	for v in d.values():
		if check_odd(v):
			counter += 1
	
	if counter>1:
		print False
	else:
		print  True

def main():
	s = 'aabbcc'
	s1 = 'Tact Coa'
	s2 = 'man is huang lalalala'
	checkPp(s)
	checkPp(s1)
	checkPp(s2)
if __name__=='__main__':
	main()
