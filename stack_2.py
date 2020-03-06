from node import Node

class Stack:
	def __init__(self, top = None, size = 0):
		self.top  = top
		self.size = size


	def push(self, newData):
		newNode 	= Node(data = newData)
		if(self.size > 0):
			newNode.setnextPointer(self.top)
		self.top 	= newNode
		self.size 	+= 1

	def peak(self):
		return(self.top.getData())

	def pop(self):
		if(self.size > 0):
			print(self.top.getData())
			prev = self.top
			self.top = self.top.getnextPointer()
			prev.setnextPointer(None)
			self.size -= 1
		else:
			print("The stack is Empty!")

def main():
	s = Stack()
	s.push(100)
	s.push("American U")
	s.push("GW")

	# print("The size was: ", s.size)
	s.pop()
	s.pop()
	s.pop()
	s.pop()
	# print("The size is: ", s.size)
	# s.pop()


if __name__ == '__main__':
	main()

