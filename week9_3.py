from collections import deque

    
def binary_number(n):
    binary_number = deque()    
    binary_number.append('1')

    for i in range(n):
        front = str(binary_number.popleft())
        binary_number.append(front + '0')
        binary_number.append(front + '1')
        print(front, end=' ')

binary_number(10)  




