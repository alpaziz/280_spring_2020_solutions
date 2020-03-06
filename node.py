class Node:
	def __init__(self, data, nextPointer = None, previousPointer = None):
		self.data 				= data
		self.nextPointer 		= nextPointer
		self.previousPointer	= previousPointer

	def getData(self):
		return(self.data)

	def setData(self, nData):
		self.data = nData

	def getnextPointer(self):
		return(self.nextPointer)

	def setnextPointer(self, n):
		self.nextPointer = n

	def getPreviousPointer(self):
		return(self.previousPointer)

	def setPreviousPointer(self, p):
		self.previousPointer = p

def main():
	n = Node(data = 10000)

if __name__ == '__main__':
	main()

