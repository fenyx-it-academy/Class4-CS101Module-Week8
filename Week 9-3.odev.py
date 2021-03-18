from collections import deque
def generate(n):
    q = deque()
    q.append('1')

    for i in range(n):
        front = str(q.popleft())
        q.append(front + '0')
        q.append(front + '1')
        print(front, end=' ')
if __name__ == '__main__':
    n = 16
    generate(n)
