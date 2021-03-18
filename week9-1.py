class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, item = ''):
        self.item.append(item)
        pass

    def pop(self):
        self.item.pop()
        pass

if __name__ == "__main__":
    stack = Stack()

    stack.push("1")
    stack.push('2')


print(stack.item)

stack.pop()

print(stack.item)


