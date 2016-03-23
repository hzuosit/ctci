#String Compression:  go through the whole string and count the appearance of char
# time complexity O(n)
def strCompres(s):
	counter = 1
	l = []
	for i in range(1,len(s)):
		if s[i-1]!= s[i]:
			l.append(s[i-1]+str(counter))
			counter = 1
		else:
			counter += 1
	l.append(s[i]+str(counter))

	result = ''.join(l)
	if len(result)>len(s):
		return s
	else:
		return result

def main():
	s = 'aaaabbbcccddeeffg'
	s2 = 'abcdefg'
	print strCompres(s)
	print strCompres(s2)

if __name__ == '__main__':
	main()


