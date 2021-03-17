'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2021 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210317]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

# Question 3:
# Given a positive number n, efficiently generate binary numbers between 1 and n using the queue data structure in linear time.

# Example Input : n = 10
# Output        : 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000

from collections import deque

def binary_number(n):
    binary_number = deque()    # class deque nun bir objesini olusturdum.
    binary_number.append('1')

    for i in range(n):
        front = str(binary_number.popleft())
        binary_number.append(front + '0')
        binary_number.append(front + '1')
        print(front, end=' ')

binary_number(16)  # fonc. cagrisi
    

