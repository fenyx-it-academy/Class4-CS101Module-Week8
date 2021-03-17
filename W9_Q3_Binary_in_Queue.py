# Given a positive number n, efficiently generate binary numbers
# between 1 and n using the queue data structure in linear time.

from __future__ import annotations


class ListNode:
    def __init__(self, data, next: ListNode = None, prev: ListNode = None) -> None:
        self.data = data
        self.prev = prev

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.size() == 0

    def add_last(self, value) -> None:
        if self.is_empty():

            self.head = self.tail = ListNode(data=value)
        else:

            node = ListNode(value, prev=self.tail)
            self.tail.next = node
        self.__size += 1


class Queue:
    def __init__(self) -> None:
        self.__list = LinkedList()

    def enqueue(self, value):
        self.__list.add_last(value)

def dec2bin():
    x = []
    n = int(input("enter n: "))
    for j in range(1, n+1):

        while j >= 2:
            b = j % 2
            x.append(str(b))
            j = j // 2

        x.append("1")
        y = ''.join(x[::-1])
        print(y, end=" ")
        r.enqueue(x)
        x = []

r = Queue()
dec2bin()
