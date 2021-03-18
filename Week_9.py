#!/usr/bin/env python
# coding: utf-8

# # Question 1:
# Implement a stack that supports push and pop operations using standard enqueue and dequeue operations of the queue.

# In[9]:


from queue import Queue 
  
class Stack: 
      
    def __init__(self): 
          
        # Two inbuilt queues  
        self.q1 = Queue() 
        self.q2 = Queue()  
              
        # To maintain current number  
        # of elements 
        self.curr_size = 0
  
    def push(self, x): 
        self.curr_size += 1
  
        # Push x first in empty q2  
        self.q2.put(x)  
  
        # Push all the remaining  
        # elements in q1 to q2.  
        while (not self.q1.empty()): 
            self.q2.put(self.q1.queue[0])  
            self.q1.get() 
  
        # swap the names of two queues  
        self.q = self.q1  
        self.q1 = self.q2  
        self.q2 = self.q 
  
    def pop(self): 
  
        # if no elements are there in q1  
        if (self.q1.empty()):  
            return
        self.q1.get()  
        self.curr_size -= 1
  
    def top(self): 
        if (self.q1.empty()): 
            return -1
        return self.q1.queue[0] 
  
    def size(self): 
        return self.curr_size 
  
s = Stack() 
s.push(1)  
s.push(2)  
s.push(3)  
  
print("current size: ", s.size()) 
print(s.top())  
s.pop()  
print(s.top())  
s.pop()  
print(s.top())  
  
print("current size: ", s.size())


# # Question 2:
# Implement a queue using a single linked list. (Hint: Enqueuing happens at the tail of the list, and the dequeuing of items happens at the head of the list.)

# In[8]:


class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def EnQueue(self, item): 
        temp = Node(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None

q = Queue() 
q.EnQueue(10) 
q.EnQueue(20) 
q.DeQueue() 
q.DeQueue() 
q.EnQueue(30) 
q.EnQueue(40) 
q.EnQueue(50)  
q.DeQueue()    
print("Queue Front " + str(q.front.data)) 
print("Queue Rear " + str(q.rear.data))


# # Question 3:
# Given a positive number n, efficiently generate binary numbers between 1 and n using the queue data structure in linear time.
# 
# Example:
# 
# Input:
# 
# n = 10
# 
# Output :
# 
# 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000

# In[12]:


from collections import deque
 
def generate(n):
 
    # create an empty queue and enqueue 1
    q = deque()
    q.append('1')
 
    # run `n` times
    for i in range(n):
        # remove the front element
        front = str(q.popleft())
 
        # append 0 and 1 to the front element of the queue and
        # enqueue both strings
        q.append(front + '0')
        q.append(front + '1')
 
        # print the front element
        print(front, end=' ')
 
 
n = 10
generate(n)


# In[ ]:




