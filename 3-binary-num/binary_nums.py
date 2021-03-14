from Queue import Queue


def binary_numbers(n):
    q = Queue()

    q.enqueue(1)

    while n > 0:
        n -= 1
        num1 = q.dequeue()
        print(num1)

        num2 = num1

        q.enqueue(str(num1)+'0')
        q.enqueue(str(num2)+'1')


binary_numbers(10000)
