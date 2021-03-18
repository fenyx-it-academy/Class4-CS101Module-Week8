
class Stack:                    #2 Class kullaniyoruz, Stack Classinda, Class queue methodlarini kullaniyoruz
    def __init__(self):         #Esasen cikarma islemi disinda fark yok
        self.q = Queue()        #Stackte en son gireni ilk cikarmak icin dequeu ve enqueue islemlerini kullaniyoruz

    def empty(self):
        print(self.q.empty())

    def push(self, data):
        self.q.enqueue(data)
        print(data, "is pushed")

    def pop(self):
        for element in range(self.q.get_size() - 1):  # toplam eleman sayisinin bir eksigi kadar cikarma ve cikani tekrar ekliyoruz
            dequeued = self.q.dequeue()  # dequeuing
            self.q.enqueue(dequeued)  # cikani tekrar ekliyoruz, ta ki son giren eleman en one gelinceye kadar
        print("{} is popped".format(self.q.dequeue()))  # Simdi en yeni giren eleman en one gecti ve dequeue islemi ile cikariliyor
                                                        # ama eklenmiyor, for dongusu disinda
    def size(self):
        print("{} is the  number of elements in stack".format(self.q.get_size()))

    def top(self):
        if not self.q.empty():
            print("{} is head of stack".format(self.q.top()))
        else:
            print("No Elements in Stack!!!")


class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def top(self):
        return (self.items[-1])

    def empty(self):
        return (self.items == [])

    def enqueue(self, data):
        self.size += 1
        self.items.append(data)

    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)

    def get_size(self):
        return self.size


s = Stack()
s.push(22)
s.push(33)
s.push(44)
s.push(55)
s.push(66)
s.size()
s.top()
s.pop()
s.pop()
s.pop()
s.empty()
s.size()
s.top()