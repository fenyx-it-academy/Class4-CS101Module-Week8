# Implement a queue using a single linked list. (Hint: Enqueuing happens at the tail of the list,
# and the dequeuing of items happens at the head of the list.)

from __future__ import annotations


class ListNode:
    def __init__(self, data, next: ListNode = None) -> None:
        self.data = data
        self.next = next

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
            node = ListNode(value)
            self.tail.next = node
            self.tail = node
        self.__size += 1

    def remove_first(self):
        if self.is_empty():
            print("There is no any node to remove in the list!")
            main_menu()
        temp = self.head.data
        self.head = self.head.next
        self.__size -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        return temp

    def peek_first(self):
        if self.is_empty():
            print("There is no any node to display in the list!")
            main_menu()
        return self.head.data


class Queue:
    def __init__(self) -> None:
        self.__list = LinkedList()

    def enqueue(self, value):
        self.__list.add_last(value)

    def dequeue(self):
        return self.__list.remove_first()

    def peek(self):
        return self.__list.peek_first()


x = Queue()


def main_menu():
    while True:
        a = input("Choose your action: [1- Add Last   2- Remove Head  3- Display Head  4- Quit] ")

        if a == "1":
            a1 = input("Enter value: ")
            x.enqueue(a1)
        elif a == "2":
            x.dequeue()
        elif a == "3":
            print(x.peek())
        elif a == "4":
            break
        else:
            print(" Wrong Entry")


main_menu()
