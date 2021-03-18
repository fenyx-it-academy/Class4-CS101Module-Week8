class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        node = Node(item)
        if self.rear == None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front == None:
            return
        node = self.front
        self.front = node.next
        if self.front == None:
            self.rear = None
        return node.data

    def empty(self):
        if self.front == None:
            return True
        return False

    def queue_printer(self):
        node = self.front
        while node:
            print(node.data, end=",")
            node = node.next
        print("\n")


if __name__ == "__main__":
    s = Queue()
    stack_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in stack_list:
        s.enqueue(item)
    s.queue_printer()
    s.dequeue()
    s.queue_printer()
