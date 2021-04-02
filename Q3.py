from Q2 import Queue


def binaryNumbers(n):
    x = Queue()

    x.enqueue(1)

    while n > 0:
        n -= 1
        num_1 = x.dequeue()
        print(num_1,end=" ")

        num_2 = num_1

        x.enqueue(str(num_1)+'0')
        x.enqueue(str(num_2)+'1')


binaryNumbers(10)