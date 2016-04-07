#class stack
class stack:
	def __init__(self,size = 100, n =3):
		self.size = size
		self.num = n
		self.array = [None] * (self.size * n)
		self.pointer = [-1]*n

	def push(self,item,num = 0):
		if num > self.num - 1: return 'Exceeds number of stacks!'
		if self.pointer[num] >= self.size -1: return 'stack {} is out of place'.format(num)
		
		self.pointer[num] += 1
		index = self.size * num + self.pointer[num]
		self.array[index]=item

	def pop(self, num =0):
		if num > self.num: return 'Exceeds number of stacks!'
		if self.pointer[num]<0: return 'Stack is empty.'
	
		index = self.size * num + self.pointer[num]
		item = self.array[index]
		self.array[index] = None
		self.pointer[num] -= 1

	def __str__(self):
		result = ''
		for i in range(self.num):
			index = self.size * i
			result+="stack {}: {} \n".format(i, self.array[index:index+self.size])
		return result




