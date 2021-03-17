from queue import Queue

class Stack(Queue):
    '''Variant of Queue that retrieves most recently added entries first.'''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()


a=Stack()
a._put("ali")
print(a.queue)
a._put("ahmet")
print(a.queue)
a._put("mehmet")
print(a.queue)
print(a._get())
print(a.queue)
print(a._get())
print(a.queue)
print(a._get())
print(a.queue)