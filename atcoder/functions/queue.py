class Queue(object):
    def __init__(self, size: int):
        self.head = 0
        self.tail = 0
        self.max = size
        self.array = [None]*size

    def enqueue(self, data: int) -> None:
        if (self.tail + 1) % self.max == self.head:
            raise Exception('queue is full')
        self.array[self.tail] = data
        self.tail = (self.tail + 1) % self.max

    def dequeue(self) -> int:
        if self.head == self.tail:
            raise Exception('queue is empty')
        v = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.max
        return v

if __name__ == "__main__":
    qu = Queue(3)
    qu.enqueue(1)
    qu.enqueue(2)
    try:
        qu.enqueue(3)
        qu.enqueue(4)
    except Exception as e:
        print(str(e))
    print(qu.dequeue())
    print(qu.dequeue())
    try:
        print(qu.dequeue())
    except Exception as e:
        print(str(e))