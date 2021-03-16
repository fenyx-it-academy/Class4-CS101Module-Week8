'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2021 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210316]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

# Question 2:
# Implement a queue using a single linked list. (Hint: Enqueuing happens at the tail of the list, 
# and the dequeuing of items happens at the head of the list.)

class Node:
    
    """
    - Singly Linked List Node Class

    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def __repr__(self) -> str:
        return f"{self.data}"


class SLL:      # =========================================== Singly Linked List ====================================================
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__size = 0
        
    def size(self) -> int:
        return self.__size
    
    def is_empty(self) -> bool:
        return self.__size == 0
    
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
        
    def add_first(self,value) -> None:
        if self.is_empty():
            self.head = self.tail = Node(data=value)   
        else:
            node = Node(data=value)
            node.next_node = self.head
            self.head = node
        self.__size += 1 
        
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
        
    def remove_last(self):   
        """ removes the last element of the singly linked list
        """
        temp = self.head
        while(temp.next_node is not None):
            prev  = temp
            temp = temp.next_node
        prev.next_node = None
        self.__size -= 1
        
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
    
    
class QueueSLL:   # ============================================ Queue implementation ===============================================
    def __init__(self) -> None:
        self.__list = SLL()
    
    def size(self):
        return self.__list.size()
    
    def is_empty(self):
        return self.__list.is_empty()
    
    def enqueue(self,value):
        return self.__list.add_first(value)
    
    def dequeue(self):
        return self.__list.remove_last()
    
    def __repr__(self) -> str:
        # [35, 15, 25]
        elements = []
        for node in self.__list:
            elements.append(str(node))
        return "[ " + " , ".join(elements) + " ]"
        # return elements
    
print("Singly LinkedList implementation =================================")
a = SLL()
print("is_empty:",a.is_empty())
a.add(2)
a.add(4)
a.add(6)
a.add(8)
a.add(10)
print('size: ',a.size())
print('Single LL: ',a)
print("is_empty:",a.is_empty())

print("Queue implement. =================================================")
qs = QueueSLL()
print("is_empty:",qs.is_empty())
qs.enqueue(111)
qs.enqueue(222)
qs.enqueue(333)
qs.enqueue(444)
print(qs)
print('size:',qs.size())
qs.dequeue()
print("after dequeue >>>>>>>>> (FIFO)")
print('size:',qs.size())
print("is_empty:",qs.is_empty())
print(qs)
