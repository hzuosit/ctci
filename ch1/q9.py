#String Rotation
#Do a trick: is s2 is rotation of s1, thus s1 must within s2+s2
def isSubstring(s1,s2):
	if len(s1)<len(s2):
		s1,s2 = s2,s1
	checker = [s1[i:i+len(s2)] for i in range(0,len(s1)-len(s2)+1)]
	if s2 in checker:
		return True
	return False

def stringRotation(s1,s2):
	s = s2 + s2
	if len(s1)!=len(s2):
		return False

	return isSubstring(s,s1)

def main():
	s1 = 'waterbottle'
	s2 = 'erbottlewat'
	print stringRotation(s1,s2)
if __name__ == '__main__':
	main()
