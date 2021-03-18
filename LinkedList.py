
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class Queue:

	def __init__(self):
		self.front = self.rear = None

	def isEmpty(self):
		return self.front == None

	def EnQueue(self, item):
		temp = Node(item)

		if self.rear == None:
			self.front = self.rear = temp
			return
		self.rear.next = temp
		self.rear = temp

	def DeQueue(self):

		if self.isEmpty():
			return

		temp = self.front
		self.front = temp.next

		if(self.front == None):
			self.rear = None

q = Queue()
q.EnQueue(11)
q.EnQueue(22)
q.DeQueue()
q.DeQueue()
q.DeQueue()
q.EnQueue(33)
q.EnQueue(44)
q.EnQueue(55)
q.DeQueue()
print("Queue Head " + str(q.front.data))
print("Queue Tail " + str(q.rear.data))