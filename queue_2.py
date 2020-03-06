from node import Node

class Queue:
	def __init__(self):
		self.size 	= 0
		self.front 	= None
		self.end 	= None

	def enqueue(self, newData):
		newNode = Node(data = newData)
		if(self.size == 0):
			self.front = newNode
		else:
			newNode.setnextPointer(self.end)
			self.end.setPreviousPointer(newNode)

		self.end   = newNode
		self.size+=1

	def dequeue(self):
		if(self.size == 0):
			print("The Queue is Empty!")
		else:
			print(self.front.getData())
			if(self.size > 1):
				old_front  = self.front 
				self.front = self.front.getPreviousPointer()
				self.front.setnextPointer(None)
				old_front.setPreviousPointer(None)
			self.size -=1
			#print(old_front)


def main():
	q = Queue()
	q.enqueue(100) 
	q.enqueue(200)
	q.enqueue(500)

	q.dequeue()
	q.dequeue()
	q.dequeue()

if __name__ == '__main__':
	main()