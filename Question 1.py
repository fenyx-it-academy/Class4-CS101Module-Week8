"""
Implement a stack that supports push and pop operations
using standard enqueue and dequeue operations of the queue.
"""

from collections import deque


class Stack:
    def __init__(self,size):
        self.size=size
        self.liste=deque ("")

    def push(self,item):
        self.liste.append (item)

    def pop(self):
        self.liste.pop ()

    def show(self):
        print (self.liste)


abc =Stack (6)

abc.push ("100")
abc.show ()
abc.push ("200")
abc.show ()
abc.push ("300")
abc.show ()
abc.push ("400")
abc.show ()
abc.push ("500")
abc.show ()
abc.push ("600")
abc.show ()

abc.pop ()
abc.show ()
abc.pop ()
abc.show ()
abc.pop ()
abc.show ()
abc.pop ()
abc.show ()
abc.pop ()
abc.show ()
abc.pop ()
abc.show ()