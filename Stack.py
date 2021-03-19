'''Lifo'''
class Stack:

    def __init__(self):
        self.empty_list = []

    def add(self, data):

        self.empty_list.append(data)
        return True
        

    def remove(self):
        if len(self.empty_list) <= 0:
            return ("No element in the empt_list")
        else:
            return self.empty_list.pop()

    def peek(self):     
	    return self.empty_list
 
 
obje=Stack()
obje.add(5)
obje.add(8)
obje.add(7)
obje.add(10)
obje.remove()
obje.remove()

print(obje.peek())
