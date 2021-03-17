'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2021 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210317]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# Question 1:
# Implement a stack that supports push and pop operations using standard enqueue and dequeue operations of the queue.

# Kuyruğun standart kuyruğa alma ve kuyruktan çıkarma işlemlerini kullanarak push ve pop işlemlerini destekleyen bir yığın uygulayın.

class Node:  
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def __repr__(self) -> str:
        return f"{self.data}"
    
    
class SinglyLinkedList:      # ======================================= Singly Linked List ================================================
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__size = 0
        
    def size(self) -> int:
        return self.__size
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def add(self,value) -> None:    # add last
        # edge case - empty list
        if self.is_empty():            
            self.head = self.tail = Node(data=value)
        else:
            # node olustur
            node = Node(data=value)
            # kuyrugun next i yap
            self.tail.next_node = node
            # node u kuyruk yap
            self.tail = node
        self.__size += 1
        
    def add_first(self, value) -> None:
        if self.is_empty():           
            self.head = self.tail = Node(data=value)
        else:
            node = Node(data=value)
            # self.head.prev = node
            node.next_node = self.head
            self.head = node
        self.__size += 1
        
    def remove_last(self):   
        """ removes the last element of the singly linked list
        """
        temp = self.head
        while(temp.next_node is not None):
            prev  = temp
            temp = temp.next_node
        prev.next_node = None
        self.__size -= 1
        
    def remove_first(self):
        """ removes the first element of the singly linked list
        """
        if self.is_empty():
            raise RuntimeError("Empty list: can not remove first(FIFO)")
        temp = self.head.data
        
        t = Node()
        t = self.head
        self.head = self.head.next_node
        t.next_node = None
        self.__size -= 1
        
        if self.is_empty():
            self.tail = None
        return temp    
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

    def __repr__(self) -> str:
        # [35, 15, 25]
        elements = []
        for node in self:
            elements.append(str(node.data))
        return "[ " + " --> ".join(elements) + " ]"
    
    
class Queue:        # =================================================== Queue ============================================================
    def __init__(self) -> None:
        self.__list = SinglyLinkedList()

    def size(self):
        return self.__list.size()

    def is_empty(self):
        return self.__list.is_empty()

    def enqueue(self, value):
        self.__list.add_first(value)

    def dequeue(self):
        return self.__list.remove_first()    
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node 
    
    def __repr__(self) -> str:
        # [35, 15, 25]
        elements = []
        for node in self.__list:
            elements.append(str(node.data))
        return "[ " + " --> ".join(elements) + " ]"
       
    
class Stack:             # ================================================= Stack ========================================================
    def __init__(self) -> None:        
        self.__list = Queue()
        
    def size(self):
        return self.__list.size()
        
    def is_empty() -> bool:
        return self.__list.is_empty()
    
    def push(self, value):
        self.__list.enqueue(value)

    def pop(self):
        return self.__list.dequeue()    
    
    def __repr__(self) -> str:
        # [35, 15, 25]
        elements = []
        for node in self.__list:
            elements.append(str(node.data))
        return "[ " + " --> ".join(elements) + " ]"
        # return elements

        
c = SinglyLinkedList()
print("singlyLL===========")
c.add(1)
c.add(2)
c.add(3)
print(c,"\n")

que = Queue()
print("Queue=============")
que.enqueue(4)
que.enqueue(5)
que.enqueue(6)
print(que,"\n")

s = Stack()
print("Stack=============")
print("size:",s.size())
s.push(111)
s.push(222)
s.push(333)
print("size:",s.size())
print(s)


        

    