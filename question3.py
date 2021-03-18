from question2 import Queue


def binary(n):
    queue = Queue()
    queue.enqueue(1)
    for i in range(n):
        front = queue.dequeue()
        queue.enqueue(front * 10)
        queue.enqueue(front * 10 + 1)
        print(front, end=" ")


binary(10)