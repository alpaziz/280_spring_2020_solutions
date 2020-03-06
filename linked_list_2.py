from node import Node

class LinkedList:
	def __init__(self, size = 0, head = None, tail = None):
		self.size = size
		self.head = head
		self.tail = tail

	def getSize(self):
		return(self.size)

	def setSize(self, s):
		self.size = s

	def getHead(self):
		return(self.head)

	def setHead(self, h):
		self.head = h

	def getTail(self):
		return(self.tail)

	def setTail(self, t):
		self.tail = t

	def isEmpty(self):
		if(self.getSize() > 0):
			return(False)
		return(True)

	def addNode(self, d):
		newNode = Node(data = d)

		# Simple Case
		if(self.isEmpty()):
			self.setHead(newNode)

		else:
			self.getTail().setnextPointer(newNode) 
			# t = self.getTail()
			# t.setnextPointer(newNode)

		self.setTail(newNode)
		self.size += 1 #self.size = self.size + 1


	def printLinkedList(self):
		currentNode = self.head
		while(currentNode != None): # currentNode != None
			print(currentNode.getData())
			currentNode = currentNode.getnextPointer()


def main():
	l = LinkedList()
	l.addNode(100)
	l.addNode(200)
	l.addNode("AU")
	l.addNode(10000000)
	l.addNode("GW")

	l.printLinkedList()



if __name__ == '__main__':
	main()