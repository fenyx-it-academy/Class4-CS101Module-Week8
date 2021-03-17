#  Implement a stack that supports push and pop operations using standard enqueue and dequeue operations of the queue.

from __future__ import annotations


class ListNode:
    def __init__(self, data, next: ListNode = None, prev: ListNode = None) -> None:
        self.data = data
        self.next = next
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
            self.tail = node
        self.__size += 1

    def remove_last(self):
        if self.is_empty():
            print("There is no any node to remove in the list!")
            main_menu()
        temp = self.tail.data
        self.tail = self.tail.prev
        self.__size -= 1

        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        return temp

    def peek_last(self):  # kuyrugun degerini soyle
        if self.is_empty():
            print("There is no any node to display in the list!")
            main_menu()
        return self.tail.data


class Stack:
    def __init__(self) -> None:
        self.__list = LinkedList()
        self.head = None
        self.tail = None
        self.__size = 0

    def size(self):
        return self.__list.size()

    def is_empty(self):
        return self.__list.is_empty()

    def push(self, value):
        self.__list.add_last(value)

    def pop(self):
        return self.__list.remove_last()

    def peek(self):
        return self.__list.peek_last()


x = Stack()


def main_menu():
    while True:
        a = input("Choose your action: [1- Add Last   2- Remove Last  3- Display Last  4- Quit] ")

        if a == "1":
            a1 = input("Enter value: ")
            x.push(a1)
        elif a == "2":
            x.pop()
        elif a == "3":
            print(x.peek())
        elif a == "4":
            break
        else:
            print(" Wrong Entry")


main_menu()
