from question2 import Queue


class Stack:
    def __init__(self):
        self.queue_one = Queue()
        self.queue_two = Queue()

    def push(self, item):
        self.queue_two.enqueue(item)
        while not self.queue_one.empty():
            self.queue_two.enqueue(self.queue_one.dequeue())
        self.queue_one, self.queue_two = self.queue_two, self.queue_one

    def pop(self):
        if self.queue_one.empty():
            return
        front_item = self.queue_one.dequeue()
        return front_item


s = Stack()
stack_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in stack_list:
    s.push(item)
s.queue_one.queue_printer()
s.pop()
s.queue_one.queue_printer()
